# graph.py
#
# Author: Narayana Chikkam
# Adapted for cs10 by Jacob Wolf

import string

class Vertex(object):
    def __init__(self, label, neighbors=None):
        """ initializes a vertex object with a label. Initially,
        the visited value is set to False.
        """
        self.label = label
        self.neighbors = set()
        if neighbors:
            for neighbor in neighbors:
                self.add_neighbor(neighbor)
        self.visited = False

    def add_neighbor(self, neighbor):
        self.neighbors.add(neighbor)

    def remove_neighbor(self, neighbor):
        self.neighbors.remove(neighbor)

    def __str__(self):
        res = "{{vertex: {}}}".format(self.label)
        return res

    def __repr__(self):
        return ("{{vertex: {}}}".format(self.label))

class Graph(object):

    def __init__(self, graph_dict=None, graph_matrix=None):
        """ initializes a graph object
            If no dictionary or None is given,
            an empty dictionary will be used
        """
        self.__graph_dict = {}
        if graph_dict:
            for vertex in graph_dict.keys():
                vertex_obj = Vertex(vertex)
                self.__graph_dict[vertex] = vertex_obj
            for vertex, neighbors in graph_dict.items():
                vertex = self[vertex]
                for neighbor in neighbors:
                    neighbor = self[neighbor]
                    vertex.add_neighbor(neighbor)
        elif graph_matrix:
            for i, letter in zip(range(len(graph_matrix)), string.ascii_lowercase):
                vertex_obj = Vertex(letter)
                self.__graph_dict[letter] = vertex_obj
            for neighbors, letter in zip(graph_matrix, string.ascii_lowercase):
                vertex = self[letter]
                for connected, letter in zip(neighbors, string.ascii_lowercase):
                    if connected:
                        neighbor = self[letter]
                        vertex.add_neighbor(neighbor)

    def vertices(self):
        """ returns the labels for the vertices of a graph """
        return list(self.__graph_dict.keys())

    def edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """ If the Vertex "vertex" is not in
            self.__graph_dict, a key with the vertex label
            with the vertex is added to the dictionary.
            Otherwise nothing has to be done.
        """
        if vertex.label not in self.vertices():
            self.__graph_dict[vertex.label] = vertex

    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list;
            between two vertices can be multiple edges!
        """
        edge = set(edge)
        (label1, label2) = tuple(edge)
        if label1 in self.vertices() and label2 in self.vertices():
            vertex1 = self[label1]
            vertex2 = self[label2]
            vertex1.add_edge(vertex2)
            vertex2.add_edge(vertex1) # assume undirected

    def reset(self):
        """Resets the vertices visited properties in the graph to prepare for a new search.
        """
        for vertex in self.__graph_dict.values():
            vertex.visited = False

    def __generate_edges(self):
        """ A static method generating the edges of the
            graph "graph". Edges are represented as sets
            with one (a loop back to the vertex) or two
            vertices
        """
        edges = []
        for vertex in self.__graph_dict.values():
            for neighbor in vertex.neighbors:
                if {neighbor.label, vertex.label} not in edges:
                    edges.append({vertex.label, neighbor.label})
        return edges

    def __getitem__(self, label):
        """ returns the Vertex with the given label or 
        None if no such Vertex exists
        """
        try:
            return self.__graph_dict[label]
        except:
            raise KeyError("Vertex {} does not exist in graph".format(label))

    def __iter__(self):
        return iter(self.__graph_dict.values())

    def __str__(self):
        res = "vertices: "
        for k in self.vertices():
            res += str(k) + ", "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + ", "
        return res
