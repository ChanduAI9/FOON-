import re
import networkx as nx
import matplotlib.pyplot as plt

def load_foon_from_file(file_path):
    """Load and clean FOON data from a file."""
    with open(file_path, 'r') as f:
        lines = f.readlines()
    units = []
    current_unit = []
    for line in lines:
        # Clean the line: remove non-alphanumeric characters, extra spaces, and normalize text
        line = re.sub(r'[^\w\s]', '', line).strip().lower()
        line = re.sub(r'\s+', ' ', line)  # Normalize multiple spaces to a single space
        if line == '\\' or line == '':
            if current_unit:
                units.append(current_unit)
            current_unit = []
        else:
            current_unit.append(line)
    return units

def foon_to_graph(foon_data):
    """Convert FOON data to graph nodes and links."""
    nodes = []
    links = []
    node_set = set()  # Use a set to avoid duplicate nodes

    for unit in foon_data:
        previous_object = None
        for line in unit:
            if line.startswith('o'):  # Object
                object_name = line.split()[1]
                if object_name not in node_set:
                    nodes.append({"id": object_name})
                    node_set.add(object_name)
                previous_object = object_name

            elif line.startswith('m'):  # Manipulation (edge)
                if previous_object:  # There is an object before manipulation
                    manipulation = line.split()[1]
                    links.append({"source": previous_object, "target": manipulation})
                    previous_object = manipulation

            elif line.startswith('s'):  # State (optional for visualization)
                continue  # Skip for basic graph

    return {"nodes": nodes, "links": links}

def visualize_graph(graph_data):
    """Visualize the FOON graph using NetworkX and Matplotlib."""
    G = nx.DiGraph()

    # Add nodes
    for node in graph_data['nodes']:
        G.add_node(node['id'])

    # Add edges
    for link in graph_data['links']:
        G.add_edge(link['source'], link['target'])

    # Draw the graph using Matplotlib
    plt.figure(figsize=(8, 6))
    nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=10, font_weight='bold')
    plt.title('FOON Graph Visualization')
    plt.show()

# Example usage
if __name__ == "__main__":
    # Load FOON data from your files
    foon_data = load_foon_from_file('foon_data.txt')

    # Convert FOON data to graph format
    foon_graph = foon_to_graph(foon_data)

    # Visualize the graph
    visualize_graph(foon_graph)
