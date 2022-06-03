import numpy as np


class Graph:
    def __init__(self, U, V) -> None:
        """
        class for directed graph
        """
        self.edges = U
        self.nodes = V
        self.adjMatrix = self.AdjMatrix()
        self.incMatrix = self.incMatrix()

    def showList(self):
        return self.edges, self.nodes

    def AdjMatrix(self):
        """
        return Adjacency matrix
        """
        A = np.zeros((len(self.nodes), len(self.nodes)), dtype=np.int0)
        for i, j in self.edges:
            A[self.nodes.index(i)][self.nodes.index(j)] = 1
            # A[self.nodes.index(j)][self.nodes.index(i)] = 1 # if graph not directed
        return A
    def incMatrix(self):
        """
        return incident matrix
        """
        A = np.zeros((len(self.nodes), len(self.nodes)), dtype=np.int0)
        for i, j in self.edges:
            A[self.nodes.index(i)][self.nodes.index(j)] = 1
            A[self.nodes.index(j)][self.nodes.index(i)] = -1
        return A

U = [(12, 3), (45, 4)]
V = [12, 3, 45, 4, 6]
g = Graph(U, V)
g.showMatrix()
