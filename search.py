from graph import Graph, Vertex

graph_dict = {
        "a": ["a", "b"],
        "b": ["b", "a", "c"],
        "c": ["c", "b"]
        }

graph = Graph(graph_dict)
print(graph)

for vertex in graph:
    print(vertex)

def dfs(start, end, graph):
    stack = []
    start_vertex = graph[start]
    stack.push(start_vertex)
    start_vertex.visited = True
    while len(stack) > 0:
        top = stack[len(stack)-1]
        if top.label == end:
            return stack
        else:
            unvisited = []
            for neighbor in top.neighbors:
                if not neighbor.visited:
                    unvisited.append(neighbor)
            if len(unvisited) > 0 :
                neighbor = random.sample(unvisited, 1)
                neighbor.visted = True
                stack.push(neighbor)
            else:
                stack.pop()
