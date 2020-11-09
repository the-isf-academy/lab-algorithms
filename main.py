from graph import Graph, Vertex
from search import dfs, bfs

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

graph = Graph(graph_dict=mtr)
print(graph)

for vertex in graph:
    print(vertex)

print(' -> '.join(map(str, dfs("syp", "jordan", graph))))

graph = Graph(graph_matrix=loop_matrix)
print(' -> '.join(map(str, dfs("a", "h", graph))))
graph.reset_graph()
print(' -> '.join(map(str, bfs("a", "h", graph))))

graph = Graph(graph_dict=simple_graph)
print(' -> '.join(map(str, bfs("a", "d", graph))))
