# This code was written by Andrew Shallue, and is a modification
# of code found in Chapter 6 of Problem Solving with Algorithms and Data
# Structures using Python, by Miller and Ranum

# Class definitions for graphs and graph vertices
# A vertex is an identifier and an adjacency list.

# A graph is a dictionary with keys being vertex identifiers
# and values being adjacency lists.

import sys

class Vertex:
    def __init__(self,num):
        self.id = num  #identifier
        self.adj = []  # list of adjacent vertices
        self.color = 'noColor'  # usefule to mark as visited
        self.count = 1

    # adds an adjacent vertex
    def addNeighbor(self,nbr):
        self.adj.append(nbr)

    # deletes a vertex from adjacency list
    def delNeighbor(self, nbr):
        self.adj.remove(nbr)

    def __str__(self):
        return str(self.id)

    # these are useful methods for managing vertex info
    def setColor(self,color):
        self.color = color
    def getColor(self):
        return self.color
    def getAdj(self):
        return self.adj
    def getId(self):
        return self.id

# this graph data structure is for unweighted, undirected graphs
# the connections are listed as part of each vertex (see above)
class Graph:
    def __init__(self):
        self.vertList = {}  # that's a dictionary, not a set
        self.numVertices = 0
        self.deletedVerts = {} # vertices we might want back, with connections

    def addVertex(self,key): # adds a vertex to the graph
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

   # deleting a vertex also involves deleting all edges connecting to it
    def delVertex(self, key):
        self.numVertices = self.numVertices - 1
        current = self.vertList[key]
        for v in current.getAdj():
            v.delNeighbor(current)

        self.deletedVerts[key] = self.vertList.pop(key)

    def getVertex(self,n): # checks whether vertex 'n' is in the graph
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def has_key(self,n):
        if n in self.vertList:
            return True

   # note this adds the edge both ways, so G is undirected
    def addEdge(self,f,t):
        if not f in self.vertList:
            nv = self.addVertex(f)
        if not t in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t])
        self.vertList[t].addNeighbor(self.vertList[f])

   # similarly we need to delete both ways.  Note vertices are not deleted
    def delEdge(self, f, t):
        self.vertList[f].delNeighbor(self.vertList[t])
        self.vertList[t].delNeighbor(self.vertList[f])

    def getVertices(self):
        return self.vertList.values()

    def __iter__(self):
        return self.vertList.itervalues()
