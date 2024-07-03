def round_off(num, dec=2):
    factor = 10 ** dec
    return int(num * factor) / factor

def replace_feature_indices_with_names(debug_string, feature_columns):
    for i, col_name in enumerate(feature_columns):
        debug_string = debug_string.replace(f"feature {i}", col_name)
    return debug_string

import re
def parse_tree_structure(tree_model_debug_string):
    lines = tree_model_debug_string.split("\n")
    dot_string = "digraph Tree {\n"
    stack = []
    node_counter = 0

    def get_node_id():
        nonlocal node_counter
        node_counter += 1
        return f"node{node_counter}"

    parent = None
    for line in lines:
        line = line.strip()
        if line.startswith("If") or line.startswith("Else"):
            condition = line.replace("If (", "").replace("Else (", "").strip().rstrip(")")
            node_id = get_node_id()
            dot_string += f'  {node_id} [label="{condition}"];\n'
            if parent:
                dot_string += f'  {parent} -> {node_id};\n'
            stack.append((node_id, parent))
            parent = node_id
        elif line.startswith("Predict"):
            prediction = line.replace("Predict: ", "").strip()
            gini = re.search(r'gini = ([0-9.]+)', line)
            samples = re.search(r'samples = ([0-9]+)', line)
            values = re.search(r'value = \[(.+?)\]', line)

            gini_value = gini.group(1) if gini else 'NA'
            samples_value = samples.group(1) if samples else 'NA'
            values_value = values.group(1) if values else 'NA'

            node_id = get_node_id()
            dot_string += f'  {node_id} [label="Predict: {prediction}\\ngini = {gini_value}\\nsamples = {samples_value}\\nvalues = [{values_value}]", shape=box];\n'
            dot_string += f'  {parent} -> {node_id};\n'
            parent = stack.pop()[1]
    dot_string += "}"
    return dot_string
