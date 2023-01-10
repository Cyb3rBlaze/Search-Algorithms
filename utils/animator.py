# Pulled + modified from https://stackoverflow.com/questions/43646550/how-to-use-an-update-function-to-animate-a-networkx-graph-in-matplotlib-2-0-0

import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.animation


class Animator():
    def animate(self, graph, total_path, interval=500):
        # build plot
        fig, ax = plt.subplots(figsize=(6,6))

        # visualization specs
        pos = nx.spring_layout(graph)
        idx_colors = sns.cubehelix_palette(100, start=.5, rot=-.75)[::-1]
        idx_weights = [3, 2, 1]

        def update(num):
            ax.clear()

            animated_path = total_path[:num+1]

            # background nodes
            nx.draw_networkx_edges(graph, pos=pos, ax=ax, edge_color="gray")
            null_nodes = nx.draw_networkx_nodes(graph, pos=pos, nodelist=set(graph.nodes()) - set(animated_path), node_color="white",  ax=ax)
            null_nodes.set_edgecolor("black")

            # query nodes
            query_nodes = nx.draw_networkx_nodes(graph, pos=pos, nodelist=animated_path, node_color=idx_colors[:len(animated_path)], ax=ax)
            query_nodes.set_edgecolor("white")
            nx.draw_networkx_labels(graph, pos=pos, labels=dict(zip(animated_path, animated_path)),  font_color="white", ax=ax)
            edgelist = [animated_path[k:k+2] for k in range(len(animated_path) - 1)]
            nx.draw_networkx_edges(graph, pos=pos, edgelist=edgelist, width=idx_weights[:len(animated_path)], ax=ax)

            # scale plot ax
            ax.set_xticks([])
            ax.set_yticks([])

        ani = matplotlib.animation.FuncAnimation(fig, update, frames=len(total_path), interval=interval, repeat=True)
        plt.show()