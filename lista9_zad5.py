import sys
from heapq import heapify, heappush,heappop
import time
import matplotlib.pyplot as plt

def dijkstra(G, start,end):
    inf = sys.maxsize
    node_data = {"A":{"cost": inf, "pred": []},
                 "B": {"cost": inf, "pred": []},
                 "C": {"cost": inf, "pred": []},
                 "D": {"cost": inf, "pred": []},
                 "E": {"cost": inf, "pred": []},
                 "F": {"cost": inf, "pred": []},
                 "G": {"cost": inf, "pred": []},
                 "H": {"cost": inf, "pred": []},
                 "I": {"cost": inf, "pred": []},
                 "J": {"cost": inf, "pred": []},
                 "K": {"cost": inf, "pred": []},
                 "L": {"cost": inf, "pred": []},
                 "M": {"cost": inf, "pred": []},
                 "N": {"cost": inf, "pred": []}}
    node_data[start]['cost'] = 0
    visited = []
    temp = start
    for i in range(13):
        if temp not in visited:
            visited.append(temp)
            min_heap = []
            for j in G[temp]:
                if j not in visited:
                    cost = node_data[temp]['cost'] + G[temp][j]
                    if cost < node_data[j]['cost']:
                        node_data[j]['cost'] = cost
                        node_data[j]['pred'] = node_data[temp]['pred'] + list(temp)
                    heappush(min_heap,(node_data[j]['cost'],j))
        heapify(min_heap)
        temp = min_heap[0][1]
    print('Najkrotszy dystans miedzy wierzcholkami: ', str(node_data[end]['cost']))
    print("Najkrotsza sciezka miedzy wierzcholkami: ", str(node_data[end]['pred'] + list(end)))

G = {"A": {"B": 2, "C": 4},
     "B": {"A": 2, "C":3,"D":8},
     "C": {"A": 4, "B":3, "E":5 ,"D":2},
     "D": {"B": 8, "C": 2, "E":11, "F":22},
     "E": {"C": 5, "D":11,"F":1, "G":3},
     "F": {"D": 22, "E": 1,"G": 8,"H": 2},
     "G": {"E": 3, "F": 8,"J":15},
     "H": {"F": 2, "I": 10, "J": 4},
     "I": {"H": 10, "K": 6},
     "J": {"H": 4, "G": 15, "L": 2, "K": 3},
     "K": {"I": 6, "J": 3, "M": 1},
     "L": {"J": 2, "N": 5,"M":9},
     "M": {"K": 1, "L": 9, "N": 7},
     "N": {"L": 5, "M": 7}
     }
print("Algorytm Dijkstry: ")
dijkstra(G,"A","N")
print("\n")



#--------------------------------------------------------------------------------------------------------
INF = 9999
def printSolution(V, distance):
    for i in range(V):
        for j in range(V):
            if(distance[i][j] == INF):
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")

def floydWarshall(V, W):
    """Algorytm Floyda Warshalla
        V - liczba wierzchołkow,
        W - ważona macierz sąsiedztwa W"""
    distance = W
    for k in range(V):
        for i in range(V):
            for j in range(V):
                distance[i][j] = min(
                    distance[i][j], distance[i][k]+distance[k][j])

    printSolution(V, distance)


W = [[0, 2, 4, INF, INF, INF,INF, INF,INF, INF,INF, INF,INF, INF],
     [2, 0, 3, 8, INF, INF,INF, INF,INF, INF,INF, INF,INF, INF],
     [4, 3, 0, 2, 5, INF,INF, INF,INF, INF,INF, INF,INF, INF],
     [INF, 8, 2, 0, 11, 22,INF, INF,INF, INF,INF, INF,INF, INF],
     [INF, INF, 5, 11, 0, 1,3,INF, INF,INF, INF,INF, INF,INF],
     [INF, INF, INF, 22, 1, 0,8,2,INF, INF,INF, INF,INF, INF],
     [INF, INF,INF, INF,3,8,0,INF, INF,15,INF, INF,INF, INF],
     [INF, INF,INF, INF,INF, 2,INF,0,10,4,INF, INF,INF, INF],
     [INF, INF,INF, INF,INF, INF,INF, 10,0,INF,6,INF, INF, INF],
     [INF, INF,INF, INF,INF, INF,15,4,INF,0,3,2,INF, INF],
     [INF, INF,INF, INF,INF, INF,INF, INF,6,3,0,INF, 1,INF],
     [INF, INF,INF, INF,INF, INF,INF, INF,INF, 2,INF,0,9,5],
     [INF, INF,INF, INF,INF, INF,INF, INF,INF, INF,1,9,0,7],
     [INF, INF,INF, INF,INF, INF,INF, INF,INF, INF,INF, 5,7,0]]

print("Algorytm Floyda-Warshalla \n "
      "Najkrotsze sciezki miedzy wierzcholkami: \n")
floydWarshall(6, W)
print("\n")


#---------------------------------------------------------------------------

times1 = []
for i in G.keys():
    start1 = time.time()
    dijkstra(G,"A",i)
    end1 = time.time()
    t1 = end1-start1
    times1.append(t1)

times2 = []
for i in range(len(W)):
    start2 = time.time()
    floydWarshall(i,W)
    end2 = time.time()
    t2 = end2-start2
    times2.append(t2)

fig,ax = plt.subplots(nrows=1, ncols=2,figsize=(15,8))
ax[0].plot(times1, linewidth = 3, color = 'purple')
ax[0].set_title("Algorytm Dijkstry")
ax[0].set_xlabel("Liczba krawedzi")
ax[0].set_ylabel("Czas działania")

ax[1].plot(times2, linewidth = 3, color = 'orange')
ax[1].set_title("Algorytm Floyda-Warshalla")
ax[1].set_xlabel("Liczba krawedzi")
ax[1].set_ylabel("Czas działania")

plt.suptitle("Wykres czasu dzialania algorytmów w zależności od rosnącej liczby krawedzi")
plt.show()

