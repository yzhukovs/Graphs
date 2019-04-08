"""
Simple graph implementation
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        #pass  # TODO
    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()

    def add_directed_edge(self, vertex_1, vertex_2):
        if vertex_1 in self.vertices and vertex_2 in self.vertices:
            self.vertices[vertex_1].add(vertex_2)
            self.vertices[vertex_2].add(vertex_1)        