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
The idea behind breadth first search is that we first look at all the nodes connected
to the starting node. If the goal node is not found, we choose one of the nodes and look
at all the connecting nodes to that node. If the goal node is not found we repeat the
same loop with the other nodes that haven't been explored yet which are connected to the
ORIGINAL starting node.

The cycle repeats and boom we can find a path between the starting node + ending
node because we are exploring every single node with equal importance. This means
that the first discovered path WILL be the shortest path (assuming the paths aren't 
weighted).
'''

nodes = graph.get_nodes()
edges = graph.get_edges()

unexplored_nodes = list(nodes)
explored_paths = [[start_node]]

found = False

curr_node = start_node
currently_exploring_nodes = [start_node]

unexplored_nodes.pop(unexplored_nodes.index(curr_node))

final_path = []


while not found:
    # adding unexplored nodes to back and looking from front to go through in right order
    curr_node = currently_exploring_nodes[0]
    currently_exploring_nodes.pop(0)

    # found loop break case
    if curr_node == ending_node:
        found = True
        for path in explored_paths:
            if path[-1] == ending_node:
                final_path = path
                break

    # easier formatting for processing
    curr_node_unexplored_edges = []

    # finding all edges/nodes connected to the current node
    for edge in edges:
        # if an edge is already explored, there is a faster path that has already been discovered
        if edge[0] == curr_node and edge[1] in unexplored_nodes:
            curr_node_unexplored_edges += [(curr_node, edge[1])]
        if edge[1] == curr_node and edge[0] in unexplored_nodes:
            curr_node_unexplored_edges += [(curr_node, edge[0])]

    curr_path_index = None

    for curr_node_edges in curr_node_unexplored_edges:
        # queue up to end of list
        if curr_node_edges[1] in unexplored_nodes:
            currently_exploring_nodes += [curr_node_edges[1]]
            unexplored_nodes.pop(unexplored_nodes.index(curr_node_edges[1]))
        # update paths list
        for i in range(len(explored_paths)):
            # checking if final node in path is equal to curr_node to update only those paths
            if explored_paths[i][len(explored_paths[i])-1] == curr_node:
                explored_paths += [explored_paths[i] + [curr_node_edges[1]]]
                curr_path_index = i
                break
    
    # removing only if path is available
    if curr_path_index != None:
        explored_paths.pop(curr_path_index)

print("Final path: ")
print(final_path)

animator.animate(graph.get_raw_graph(), final_path)