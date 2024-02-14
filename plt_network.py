import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


def plt_network(cities, beta_matrix, node_size_vector, node_fill_percentage_vector):

    # Create a directed graph from the adjacency matrix
    G = nx.DiGraph()
    
    # Add nodes to the graph with labels and size
    for city, node_size, fill_percentage in zip(cities, node_size_vector, node_fill_percentage_vector):
        G.add_node(city, node_size=node_size, fill_percentage=fill_percentage)
    
    # Add weighted edges to the graph
    for i in range(len(cities)):
        for j in range(len(cities)):
            if i != j:
                weight = beta_matrix[i][j]
                if weight > 0:
                    G.add_edge(cities[i], cities[j], weight=weight)
    
    # Plot the directed graph
    pos = nx.planar_layout(G)  # You can choose a different layout if you prefer
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




# Define the adjacency matrix with weights
beta_matrix = np.round( [
    [1, 0.0, 0.0, 0.0], 
    [0.016, 1, 0.0, 0.0], 
    [0.1575, 0.0, 1, 7.5], 
    [0.0, 0.0, 1.7777777777777777, 1]
],2)

# Supply vectors for node size and node colors (with percentages)
N = [1000, 200, 150, 100]  # Modify these values as needed
r = [0.5999483812470671, 0.02616053587183521, 0.8032915172981273, 0.6044655869426754]

# Define the cities and their labels
cities = ["1", "2", "3", "4"]
plt_network(cities, beta_matrix, N, r)