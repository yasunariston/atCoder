import math

def dijkstra(nmst):
    n, m, s, t = nmst[0] - 1, nmst[1] - 1, nmst[2] - 1, nmst[3] - 1
    unserched_list = list(range(n)) #未探索ノード
    distance = [math.inf] * n #各ノード間の距離リスト
    distance[s] = 0 #スタートノードの距離は0
    previous_nodes = [-1] * n #最短経路でそのノードの一つ前に到達するノードリスト

    while(len(unsearched_nodes) != 0): #未探索ノードがなくなるまで繰り返す
        #未探索ノードのうち、distanceが最小のものの選択
        posible_min_distance = math.inf



if __name__ == "__main__":
    nmst = input().split()
    route_list = []


    dijkstra(nmst)

