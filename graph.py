
#Graph data structure for input graph

from node import Node

class Graph:
    def __init__(self, n):
        self.numnodes = n
        self.vertices = [] #container for nodes
        self.edges = []
        for i in range(0,n):
            self.vertices.append(Node(i))
            self.edges.append([])
        self.max_edge_l = 0
        self.source = None
    def size(self):
        return self.numnodes

    #add edge to the graph
    def add_edge(self, head, tail, edge_length):
        self.edges[head].append((tail, edge_length)) # edges are a tuple of tail and edge length
        if edge_length > self.max_edge_l:
            self.max_edge_l= edge_length

    def neighbors(self, i):
        return self.edges[i]
    def vertices(self):
        return self.vertices
    def max_edge_length(self):
        return self.max_edge_l
    def update_distance(self, id, dist):
        self.vertices[id].distance = dist
    def get(self, i):
        return self.vertices[i]
    def update_parent(self,i, p):
        self.vertices[i].parent = self.vertices[p]
    def set_source(self, i):
        self.vertices[i].distance = 0
        self.source = self.vertices[i]
    def get_source(self):
        return self.source.id
    #return the length of arc (a,b)
    def find_arc_length(self, a,b):
        for e in self.edges[a]:
            if e[0] == b:
                return e[1]
