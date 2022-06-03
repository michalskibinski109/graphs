from re import L
import numpy as np


class DirectedGraph:
    def __init__(self, E, N) -> None:
        """
        class for directed graph
        """
        self.edges = E
        self.nodes = N
        self.adjMatrixRep = self.adjMatrix()
        self.incMatrixRep = self.incMatrix()

    def showList(self):
        return self.edges, self.nodes

    def adjMatrix(self):
        """
        return Adjacency matrix
        """
        A = np.full((len(self.nodes), len(self.nodes)), 0, dtype=float)
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

    def shortestPath(self, u=0, v=0):
        """
        shortest path algorithm using matrix multiplication
        """
        n = len(self.nodes)
        # wszedzie gdzie nie istnieje polaczenie bezposrednie inf
        C = np.where(self.adjMatrixRep == 0.0, np.inf, self.adjMatrixRep)
        np.fill_diagonal(C, 0)  # zera na diagonalach
        for _ in range(n):
            for i in range(n):
                for j in range(n):
                    for k in range(n):
                        C[i, j] = min(C[i, j], C[i, k]+C[k, j])
        return(int(C[self.nodes.index(u), self.nodes.index(v)]))




E = [(12, 3), (45, 4), (3, 6), (6, 4), (4, 45), (45, 12)]
N = [12, 3, 45, 4, 6]
g = DirectedGraph(E, N)
print(g.shortestPath(12, 6))
