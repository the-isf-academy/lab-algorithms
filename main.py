from graph import Graph, Vertex
from search import dfs, bfs, dfs0a, dfs0b, dfs1

mtr = {
        "syp": ["syp", "sheung wan"],
        "sheung wan": ["sheung wan", "syp", "central"],
        "central": ["central", "sheung wan", "admiralty"],
        "admiralty": ["admiralty", "central", "tst", "ocean park", "wan chai"],
        "ocean park": ["ocean park", "admiralty"],
        "wan chai": ["wan chai", "admiralty"],
        "tst": ["tst", "admiralty", "jordan"],
        "jordan": ["jordan", "tst"]
    }

simple_graph = {
        "a": ["a", "b"],
        "b": ["b", "a", "c"],
        "c": ["c", "b"],
        "d": ["d"]
        }

loop_matrix = [
        [0, 1, 0, 0, 0, 0, 1, 0],
        [1, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 1, 0],
        [1, 0, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 0]
        ]

# Basic search tests on simple graph
print("Basic searches:")
graph = Graph(graph_dict=simple_graph)
print(graph)
print(' -> '.join(map(str, dfs1("a", "c", graph))))
graph.reset()
print(' -> '.join(map(str, dfs1("a", "a", graph))))  # Same start/end
graph.reset()
print(' -> '.join(map(str, dfs1("a", "d", graph))))  # No path exists
# #
# # # Search path from SYP to Jordan in MTR graph from slides
print("\nMTR graph searches:")
graph = Graph(graph_dict=mtr)
print(graph)
print(' -> '.join(map(str, bfs("syp", "jordan", graph))))
#
# # Loop graph from C.2
print("\nLoop graph searches:")
graph = Graph(graph_matrix=loop_matrix)
print(graph)
print(' -> '.join(map(str, bfs("h", "a", graph))))
graph.reset()
print(' -> '.join(map(str, dfs0b("h", "a", graph))))
#
#
# # ADD YOUR OWN SEARCHES HERE
# print("\nAdditional searches:")
