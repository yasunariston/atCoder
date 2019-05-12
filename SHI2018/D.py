import networkx as nx
import math

nmst = [int(i) for i in input().split()]
n, m, s, t = nmst[0], nmst[1], nmst[2], nmst[3]

#trainの無向グラフ作成(yen, snookそれぞれ)
graphY = nx.Graph()
graphS = nx.Graph()
graphY.add_nodes_from(range(1, n + 1))
graphS.add_nodes_from(range(1, n + 1))

for i in range(m):
    train = input().split()
    c1, c2 = int(train[0]), int(train[1])
    yen, snook = int(train[2]), int(train[3])
    graphY.add_edge(c1, c2, weight=yen)
    graphS.add_edge(c1, c2, weight=snook)

#都市sからiへのminYen, tからiへのminSnookを求める
ansList = []
for i in range(1, n + 1):
    yen = nx.dijkstra_path_length(graphY, s, i)
    snook = nx.dijkstra_path_length(graphS, t, i)
    ans = yen + snook
    ansList.append(ans)

for i in range(i):
    ans = 1000000000000000 - min(ansList)
    print(ans)
    ansList.pop(0)
