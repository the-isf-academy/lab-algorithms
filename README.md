# Graph Algorithms Lab (Extension)
This lab extension offers students the challenge of writing BFS and DFS algorithms
to find a path between two vertices in a graph.

## Graphs and vertices
This lab uses a custom Graph object and Vertex objects to explore a graph.

### Vertex
The Vertex class stores information about a vertex including:
- it's label
- it's neighbors
- whether it has been visited or not

Create vertex:
```python
from graph import Vertex

vertexA = Vertex("A")
vertexB = Vertex("B")
```

And then add and remove neighbors of that vertex:
```python
vertexA.add_neighbor(vertexB)
vertexB.add_neighbor(vertexA)  #edge is now bi-directional

vertexB.remove_neighbor(vertexA)  #edge is now only from A -> B
```
You can get the label of the vertex by accessing the `label` property:
```python
vertexA.label
```

and get a list of the vertex's neighbors using the `neighbors` property:
```python
vertexA.neighbors
```

Finally, you can get or set the visited status of a Vertex using the `visited` property:
```python
vertexA = Vertex("A")

vertexA.visited = True
```

**NOTE: By default, vertices are unvisited.**

### Graph
Graph is a wrapper for a graph dictionary that allows the user to build graphs
by adding Vertex objects:
```python
from graph import Graph, Vertex

vertexA = Vertex("A")
graph = Graph()
graph.add_vertex(vertexA)
```

Graphs can also add edges between vertices:
```python
vertexA = Vertex("A")
vertexB = Vertex("B")
graph = Graph()
graph.add_vertex(vertexA)
graph.add_vertex(vertexB)
graph.add_edge(("A", "B"))
```
**NOTE: `add_edge()` assumes an undirected graph and will add a bidirectional edge."**

You can access vertices in the Graph using their labels:
```python
vertexA = Vertex("A")
vertexB = Vertex("B")
graph = Graph()
graph.add_vertex(vertexA)
graph.add_vertex(vertexB)

...

vertexA = graph["A"]
vertexB = graph["B"]
```

Graphs can also be generated from dictionaries or adjacency matrices:
```python
# dictionary representation
simple_graph_dict = {
        "a": ["a", "b"],
        "b": ["b", "a", "c"],
        "c": ["c", "b"],
        "d": ["d"]
        }
graph = Graph(graph_dict=simple_graph_dict)

#Adjacency matrix representation
simple_graph_matric = [
       [1, 1, 0, 0],
       [1, 1, 1, 0],
       [0, 1, 1, 0],
       [0, 0, 0, 1]
    ]
graph = Graph(graph_matrix=simple_graph_matrix)
```

You can reset the visited statues of every vertex in the graph using:
```python
simple_graph_matric = [
       [1, 1, 0, 0],
       [1, 1, 1, 0],
       [0, 1, 1, 0],
       [0, 0, 0, 1]
    ]
graph = Graph(graph_matrix=simple_graph_matrix)
vertex_a = graph["a"]
vertex_a.visited = True

...

graph.reset()
```

Finally, you can get the labels for all the nodes and edges of a graph in lists:
```python
simple_graph_matric = [
       [1, 1, 0, 0],
       [1, 1, 1, 0],
       [0, 1, 1, 0],
       [0, 0, 0, 1]
    ]
graph = Graph(graph_matrix=simple_graph_matrix)

vertices = graph.vertices()
edges = graph.edges()
```

## Search algorithms
We explored Depth-First Search (DFS) and Breadth-First Search (BFS) in class.

### DFS
DFS searchs one path until it can explore no further before trying another path.
Pseudocode:
```
Place first vertex in stack and mark as visited
While vertices in stack:
    If top vertex is end:
        Search complete
    else:
    If top vertex has unvisited neighbors:
        Pick unvisited neighbor vertex
        Mark neighbor vertex as visited
        Put neighbor vertex in stack
    else (if top vertex has no unvisited neighbors):
        Remove top vertex from stack
```

Note: Python uses [lists as stacks](https://docs.python.org/3.8/tutorial/datastructures.html#using-lists-as-stacks):
- create a stack using `stack_example = []`
- push into a stack using `stack_example.append()`
- pop from a stack using `stack_example.pop()`


### BFS
BFS searches mulitple paths at once, broadening the search out from the start
vertex one hop at a time.

Pseudocode:
```
Mark start as visited, put in path, and put path in queue
While paths in queue:
    If top vertex of first path is end:
        Search complete
    else:
    If top vertex of first path has unvisited neighbors:
        Pick unvisited neighbor vertex
        Mark neighbor vertex as visited
        Put neighbor vertex into new path and queue
    else (if first vertex has no unvisited neighbors):
        Remove first path from queue
```

Note: Python uses [a unique data structure for queues](https://docs.python.org/3.8/library/collections.html#collections.deque):
- create a queue using `queue_example = deque()`
- queue into a queue using `queue_example.append()`
- dequeue from a queue using `queue_example.popleft()`
