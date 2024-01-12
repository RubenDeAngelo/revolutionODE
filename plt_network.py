import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


def plt_network(cities, labels, beta_matrix, node_size_vector, node_fill_percentage_vector):

    # Create a directed graph from the adjacency matrix
    G = nx.DiGraph()
    
    # Add nodes to the graph with labels and size
    for city, label, node_size, fill_percentage in zip(cities, labels, node_size_vector, node_fill_percentage_vector):
        G.add_node(city, label=label, node_size=node_size, fill_percentage=fill_percentage)
    
    # Add weighted edges to the graph
    for i in range(len(cities)):
        for j in range(len(cities)):
            if i != j:
                weight = beta_matrix[i][j]
                if weight > 0:
                    G.add_edge(cities[i], cities[j], weight=weight)
    
    # Plot the directed graph
    pos = nx.spring_layout(G, seed=42)  # You can choose a different layout if you prefer
    edge_labels = nx.get_edge_attributes(G, 'weight')
    
    # Plot edges with varying thickness based on weights
    edge_widths = [G.edges[u, v]['weight'] for u, v in G.edges()]
    edge_widths = np.interp(edge_widths, (min(edge_widths), max(edge_widths)), (1, 5))  # Adjust thickness scaling as needed
    
    
    plt.figure(figsize=(10, 6))
    
    # Extract node sizes and fill percentages
    node_sizes = [G.nodes[node]['node_size'] for node in G.nodes()]
    fill_percentages = [G.nodes[node]['fill_percentage'] for node in G.nodes()]
    
    # Normalize node sizes to a reasonable range
    node_sizes = np.interp(node_sizes, (min(node_sizes), max(node_sizes)), (100, 1000))
    
    # Generate node colors based on fill percentages (e.g., shades of gray)
    node_colors = [((1 - fill_percentage), (1 - fill_percentage), (1 - fill_percentage)) for fill_percentage in fill_percentages]
    
    # Plot nodes with specified sizes and colors
    nx.draw(G, pos, with_labels=True, node_size=node_sizes, node_color=node_colors, width=edge_widths, connectionstyle='arc3,rad=0.13')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos = 0.7)
    plt.title("Directed Graph of Five Cities with Weights and Customized Node Sizes and Colors")
    plt.show()



# Define the cities and their labels
cities = ["City1", "City2", "City3", "City4", "City5"]
labels = [1, 2, 3, 4, 5]

# Define the adjacency matrix with weights
beta_matrix = [
    [1,  7.5,   3, 20, 0],
    [4,    1,   2, 0,  0],
    [0,    2,   1, 0, 40],
    [0.25, 0,   0, 1, 50],
    [0,    0, 1.2, 0, 1]
]

# Supply vectors for node size and node colors (with percentages)
N = [200, 300, 150, 250, 180]  # Modify these values as needed
r = [0.2, 0.4, 0.6, 0.8, 0.1]  # Modify these values as needed

plt_network(cities, labels, beta_matrix, N, r)