from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import StructType, StructField, StringType, DoubleType
from pyspark.ml.linalg import Vectors, VectorUDT
from pyspark.ml.classification import DecisionTreeClassifier
from pyspark.ml.feature import StringIndexer, VectorAssembler
from pyspark.sql import SparkSession
from pyspark.sql.functions import var_pop
from pyspark.sql.types import StructType, StructField, StringType, DoubleType

from .utils import replace_feature_indices_with_names
from .utils import parse_tree_structure
from .utils import round_off

import graphviz # type: ignore

@udf(returnType=VectorUDT())
def to_dense_vector(v):
    return Vectors.dense(v.toArray())

def get_multivariate_analysis(df, table_name, numerical_columns,id_columns=None, vif_analysis=1, decision_tree_analysis=1, target_column=None, depth=3):
    spark = SparkSession.builder.getOrCreate()

    # Drop the ID column if provided
    if id_columns:
        df = df.drop(*id_columns)

    vif_schema = StructType([
        StructField('Feature', StringType(), True),
        StructField('VIF', DoubleType(), True)
    ])
    # Drop the table if it exists
    spark.sql(f"DROP TABLE IF EXISTS {table_name}")

    if vif_analysis and numerical_columns:
        for column in numerical_columns:
            try:
                # Check for zero variance columns using Spark
                variance = df.select(var_pop(column)).collect()[0][0]
                if variance == 0:
                    print(f"Column '{column}' has zero variance and will be skipped. ")
                    #Explanation: Zero variance means that all values in the column are the same. 
                    #Such columns do not provide any useful information for multivariate analysis and can cause computational issues.
                    continue

                # Calculate R-squared sum for the current column using PySpark
                other_columns = [c for c in numerical_columns if c != column]
                r_squared_sum = sum([df.stat.corr(column, other_col)**2 for other_col in other_columns])

                # Calculate VIF
                if r_squared_sum == 1.0:
                    vif = float('inf')
                else:
                    vif = 1.0 / (1.0 - r_squared_sum)

                if vif == float('inf'):
                    print(f"VIF for column '{column}' is infinity, indicating perfect multicollinearity, and will be skipped. ")
                    #Explanation: Perfect multicollinearity means that the column is a perfect linear combination of other columns. 
                    # This makes the VIF infinite and invalidates the analysis.
                    continue

                new_row = spark.createDataFrame([(column, round_off(vif))], schema=vif_schema)
                new_row.write.option("mergeSchema", "true").saveAsTable(table_name, mode='append')
            except Exception as e:
                print(f"Error processing VIF for column '{column}': {e}")
        print(f"The results have been successfully saved to the table: {table_name}")


    if decision_tree_analysis and numerical_columns and target_column:
        try:
            string_indexer = StringIndexer(inputCol=target_column, outputCol="indexed_target")
            si_model = string_indexer.fit(df)
            df_indexed = si_model.transform(df)

            assembler_inputs = [col for col in numerical_columns if col != target_column]
            feature_assembler = VectorAssembler(inputCols=assembler_inputs, outputCol="features")
            df_features = feature_assembler.transform(df_indexed)

            df_features = df_features.withColumn("features_dense", to_dense_vector("features"))

            dt = DecisionTreeClassifier(labelCol="indexed_target", featuresCol="features_dense", maxDepth=depth)
            dt_model = dt.fit(df_features)

            print("Decision Tree Model of", target_column, ":")
            tree_model_readable = replace_feature_indices_with_names(dt_model.toDebugString, assembler_inputs)
            print(tree_model_readable)

            # Generate Graphviz representation
            dot_string = parse_tree_structure(tree_model_readable)

            # Visualize the decision tree using Graphviz
            graph = graphviz.Source(dot_string)
            graph.render("decision_tree", format="png")
            print("Decision tree rendered to decision_tree.png")
        except Exception as e:
            print(f"Error processing Decision Tree analysis: {e}")