import networkx as nx
import random
import matplotlib.pyplot as plt


class RandomGraph():
    # graph object creation
    def __init__(self, nodes, partition=2, path_weight_range=(1.5, 3)):
        graph = nx.Graph()
        graph.add_nodes_from([i for i in range(nodes)])

        edges = []
        for i in range(partition):
            for j in range(nodes):
                val = random.randint(0, nodes)
                skip = False
                for edge in edges:
                    if edge[1] == val and edge[0] == j or edge[0] == val and edge[1] == j:
                        skip = True
                if j != val and skip == False:
                    edges += [(j, val, random.uniform(*path_weight_range))]

        graph.add_weighted_edges_from(edges)

        self.graph = graph
    

    # GETTERS
    def get_nodes(self):
        return self.graph.nodes

    def get_edges(self):
        return self.graph.edges
    
    def get_raw_graph(self):
        return self.graph
        

    # visualization function
    def visualize_raw_graph(self):
        plt.subplot(111)
        nx.draw(self.graph, with_labels=True)
        plt.show()