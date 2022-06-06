import math
import matplotlib.pyplot as plt
import networkx as nx
import pprint


class Graph:
    def __init__(self):
        self.nodes = list()
        self.edges = list()
        self.edges_dict = dict()
        self.distance_matrix = None
        self.next_matrix = None

    def add_node(self, node: str):
        self.nodes.append(node)

    def add_edge(self, edge: list):
        self.edges.append(edge)
        self.edges.append([edge[1], edge[0], edge[2]])
        if edge[0] not in self.edges_dict.keys():
            self.edges_dict[edge[0]] = list()
        if edge[1] not in self.edges_dict.keys():
            self.edges_dict[edge[1]] = list()
        if edge[1] not in self.edges_dict[edge[0]]:
            self.edges_dict[edge[0]].append((edge[1], edge[2]))
        if edge[0] not in self.edges_dict[edge[1]]:
            self.edges_dict[edge[1]].append((edge[0], edge[2]))

    def make_distance_matrix(self):
        self.distance_matrix = list()
        for _ in range(len(self.nodes)):
            self.distance_matrix.append(list())
        for i in range(len(self.nodes)):
            for j in range(len(self.nodes)):
                self.distance_matrix[i].append(math.inf)

        for edge in self.edges:
            self.distance_matrix[edge[0]][edge[1]] = edge[2]

    def make_next_matrix(self):
        self.next_matrix = list()
        for _ in range(len(self.nodes)):
            self.next_matrix.append(list())
        for i in range(len(self.nodes)):
            for j in range(len(self.nodes)):
                self.next_matrix[i].append(None)

        for i in range(len(self.nodes)):
            for j in range(len(self.nodes)):
                if self.distance_matrix[i][j] != math.inf:
                    self.next_matrix[i][j] = j

    def floyd_warshall(self):
        self.make_distance_matrix()
        self.make_next_matrix()
        for i in range(len(self.nodes)):
            for j in range(len(self.nodes)):
                for k in range(len(self.nodes)):
                    if self.distance_matrix[j][i] == math.inf or self.distance_matrix[i][k] == math.inf:
                        continue
                    if self.distance_matrix[j][k] > (self.distance_matrix[j][i] + self.distance_matrix[i][k]):
                        self.distance_matrix[j][k] = self.distance_matrix[j][i] + self.distance_matrix[i][k]
                        self.next_matrix[j][k] = self.next_matrix[j][i]

    def shortest_path(self, source: int, target: int):
        self.floyd_warshall()
        if self.next_matrix[source][target] is None:
            return [None, None]

        path = list()
        path.append(source)
        while source != target:
            source = self.next_matrix[source][target]
            path.append(source)

        return path, self.distance_matrix[path[0]][target]


def visualize_graph(graph):
    g1 = nx.Graph()
    g1.add_nodes_from(graph.nodes)
    pos = nx.spring_layout(g1)
    edges_list = [[item[0], item[1]] for item in graph.edges]
    weight_edges = {(item[0], item[1]): item[2] for item in graph.edges}
    g1.add_edges_from(edges_list)
    nx.draw(g1, pos, with_labels=True)
    nx.draw_networkx_edge_labels(g1, pos, edge_labels=weight_edges)
    plt.show()


if __name__ == "__main__":
    g = Graph()
    with open("graph_info/zad2nodes.txt") as f:
        nodes = f.read().split()
        for n in nodes:
            g.add_node(int(n))
    with open("graph_info/zad2edges.txt") as f:
        edges = f.readlines()
        for c in range(len(edges)):
            edges[c] = edges[c].split()
        for ed in edges:
            to_add = [int(item) for item in ed]
            g.add_edge(to_add)

    print(g.shortest_path(4, 3))
    visualize_graph(g)
