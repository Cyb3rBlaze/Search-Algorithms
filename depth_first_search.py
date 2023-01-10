from utils.graph import RandomGraph
from utils.animator import Animator


# random graph creation picked for traversal
graph = RandomGraph(20)
graph.visualize_raw_graph()

# make sure valid path exists
start_node = int(input("Please choose a starting node: "))
ending_node = int(input("Please choose an ending node: "))

# for visualization of path finding
animator = Animator()
# animator.animate(graph.get_raw_graph(), [start_node, ending_node])


'''
The idea behind depth first search is that we first look at one of the nodes connected to
the starting node. If the goal node is not found, we choose one of the nodes connected to
that new node. If the goal node is not found we repeat the same loop until a base node
with no unexplored connected nodes is found where one of the other unexplored nodes 
connected to the preceding node is explored.

The cycle repeats and boom we can find a path between the starting node + ending
node because we are exploring every single node with equal importance. This means
that the first discovered path wil not necessarily be the shortest path (assuming 
the paths aren't weighted).
'''

nodes = graph.get_nodes()
edges = graph.get_edges()

unexplored_edges = list(edges)
explored_paths = []

found = False

curr_node = start_node


def find_path(curr_node, end_node):
    # base case to check if node is found
    if curr_node == ending_node:
        return [curr_node]
        
    # easier formatting for processing
    curr_node_unexplored_edges = []

    # finding all edges/nodes connected to the current node
    for edge in edges:
        # if an edge is already explored, there is a faster path that has already been discovered
        if edge[0] == curr_node and edge in unexplored_edges:
            curr_node_unexplored_edges += [edge]
        if edge[1] == curr_node and edge in unexplored_edges:
            curr_node_unexplored_edges += [edge]

    print(curr_node_unexplored_edges)

    # exploring all connected edges with unexplored nodes
    for edge in curr_node_unexplored_edges:
        unexplored_edges.pop(unexplored_edges.index(edge))

        connected_node = None
        if edge[0] == curr_node:
            connected_node = edge[1]
        else:
            connected_node = edge[0]

        one_recursive_call = find_path(connected_node, end_node)

        if one_recursive_call != []:
            return [curr_node] + one_recursive_call
    
    return []

final_path = find_path(curr_node, ending_node)
print(final_path)
animator.animate(graph.get_raw_graph(), final_path)