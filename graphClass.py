from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from collections import defaultdict
from networkx.drawing.nx_pydot import graphviz_layout
np.random.seed(1)

class DirectedGraph:
    def __init__(self, E, N) -> None:
        """
        class for directed graph
        """
        self.edges = E
        self.nodes = N
        self.adjMatrixRep = self.adjMatrix()
        self.incMatrixRep = self.incMatrix()
        self.graph = self.dictFunc()
        self.G = nx.DiGraph()
        self.G.add_edges_from(E)
        self.dfsPath = []

    def dictFunc(self):
        graph = defaultdict(list)
        for (u, v) in self.edges:
            graph[u].append(v)
        return graph
    def __str__(self):
        return str(f'edges: {self.edges}\nnodes: {self.nodes}')

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
        return((C[self.nodes.index(u), self.nodes.index(v)]))

    def dfs(self, node, visited = set()):  #function for dfs 
        if node not in visited:
            print(node)
            self.dfsPath.append(node)
            visited.add(node)
            for neighbour in self.graph[node]:
                self.dfs(neighbour, visited)
    
    def bfs(self, node, visited = []):
        queue = []
        visited.append(node)
        queue.append(node)

        while queue:
            s = queue.pop(0) 
            print (s, end = " ") 

            for neighbour in self.graph[s]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
        return visited
                
                
    def plot(self, path = []):


        
        if len(path) == 0: 
            path.append(-1)
        visitedNodes = []
        for e, currNode in enumerate(path):
            visitedNodes.append(currNode)
            pos = graphviz_layout(self.G, prog="dot")
            values = [.8 if node in visitedNodes else .9 for node in self.G.nodes()]
            nx.draw_networkx_nodes(self.G,pos, 
                       node_color = values, node_size = 500)
            nx.draw_networkx_labels(self.G, pos)
            nx.draw_networkx_edges(self.G, pos, arrows=True)
            plt.title(str(f'{e + 1} step'))
            plt.show()


E = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('E', 'F'), ('C', 'G')]
N = ['A', 'B', 'C', 'D','E','F', 'G']
g = DirectedGraph(E, N)
### zadanie 1 #####

# print(g.adjMatrixRep)
# print(g.incMatrixRep)
# print(g)
# print(g.shortestPath('A', 'C'))

#### zad 2 ###
g.dfs('A')
g.plot(g.dfsPath)
g.plot(g.bfs('A'))
