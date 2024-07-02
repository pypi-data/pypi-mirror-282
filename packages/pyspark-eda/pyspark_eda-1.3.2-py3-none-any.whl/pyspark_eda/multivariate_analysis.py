from pyspark.sql import SparkSession
from pyspark.sql.functions import col, udf
from pyspark.sql.types import StructType, StructField, StringType, DoubleType
from pyspark.ml.linalg import Vectors, VectorUDT
from pyspark.ml.classification import DecisionTreeClassifier
from pyspark.ml.feature import StringIndexer, VectorAssembler
from pyspark.sql import Row
from pyspark.ml.regression import LinearRegression
from .utils import replace_feature_indices_with_names
from .utils import parse_tree_structure

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
                y = column
                x = [col for col in numerical_columns if col != column]

                # Prepare data for linear regression
                df_lr = df.select(*x, col(y).alias("label"))
                df_lr = df_lr.rdd.map(lambda row: Row(label=row[-1], features=Vectors.dense(row[:-1]))).toDF()

                # Fit linear regression mode
                lr = LinearRegression(featuresCol="features", labelCol="label")
                lr_model = lr.fit(df_lr)

                # Calculate R^2
                r2 = lr_model.summary.r2

                # Calculate VIF
                vif = round(1 / (1 - r2), 2)

                vif_df = spark.createDataFrame([(y, vif)], schema=vif_schema)
                vif_df.write.option("mergeSchema", "true").saveAsTable(table_name, mode='append')
            except Exception as e:
                print(f"Error processing VIF for column {column}: {e}")
        
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