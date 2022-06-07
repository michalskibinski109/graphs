import networkx as nx
import matplotlib.pyplot as plt


class Graph:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges

    def visualize(self):
        g = nx.DiGraph()
        g.add_edges_from(self.edges)
        nx.draw(g, with_labels=True)
        plt.show()

    # Funkcja rekurencyjna używana przez topologicalSort
    def recursive_sort(self, s, visited, sort_list, neighbours):
        # Oznaczamy wszystkie wierchołki jako odwiedzone
        visited[s] = True
        # Recur dla wszystkich wierzchołków sąsiadujących z tym wierzchołkiem
        for i in neighbours[s]:
            if visited[i] == 0:
                self.recursive_sort(i, visited, sort_list, neighbours)
        # Wstawiamy bieżący wierzchołek do stosu, który przechowuje wynik
        sort_list.insert(0, s)

    # Funkcja do sortowania topologicznego. Używa rekurencji topologicalSortUtil()
    def topological_sorting(self):

        def make_neighbours(nodes, edges): #tworzymy słownik, który przechowuje wyjscia z danych wierzchlkow (krawedzie)
            neighbours_dict = {node: [] for node in nodes}
            for edge in edges:
                neighbours_dict[edge[0]].append(edge[1])
            return neighbours_dict

        visited = [False] * len(self.nodes) # Oznacz wszystkie wierzchołki jako nieodwiedzone
        sort_list = list()
        neighbours = make_neighbours(self.nodes, self.edges)
        #Wywołujemy rekurencyjną funkcję pomocniczą, aby zapisać Topological
        #Sortuj zaczynając od wszystkich wierzchołków jeden po drugim
        for v in self.nodes:
            if visited[v] == False:
                self.recursive_sort(v, visited, sort_list, neighbours)
        #zawartość stosu
        return sort_list

    def total_time(self, order=None):
        if order is None:
            order = self.topological_sorting()
        time = 0
        time_dict = {}
        for node in order:
            time_dict[node] = time
            time += node
        return time_dict


if __name__ == "__main__":
    nodes_list = [0, 1, 2, 3, 4, 5, 6]
    edges_list = [(0, 1),
                  (1, 2),
                  (3, 2),
                  (3, 1),
                  (3, 2),
                  (3, 4),
                  (4, 5),
                  (4, 6),
                  (6, 5)]

    visualizing = True
    graph = Graph(nodes_list, edges_list)

    if visualizing:
        graph.visualize()

    order_list = graph.topological_sorting()
    print(order_list)

    print("time", graph.total_time(order_list))
