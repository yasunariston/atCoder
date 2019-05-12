from collections import defaultdict

N = int(input())
abList = [list(map(int, input().split())) for _ in range(N-1)]

# 木構造の関係リスト作成
treeDict = defaultdict(list)
for a, b in abList:
    treeDict[a].append(b)
    treeDict[b].append(a)

# コストの辞書と疑似キューを作成
costDict = defaultdict(int)
treeQ = set()

# 葉(端)のコストを1にし、隣接ノードをキューに格納
for node in treeDict:
    if len(treeDict[node]) == 1:
        costDict[node] = 1
        treeQ.add(treeDict[node][0])

# 1つを除く隣接ノードにコストが設定されている(!= 0)場合、
# 隣接ノードの最大コスト + 1 でコストを設定し、コスト未設定のノードをキューに格納。
# 上記をキューに値が入らなくなるまで繰り返す。
node = 1
while(treeQ):
    tQ = set()
    costList = []
    for node in treeQ:
        if costDict[node] != 0: break
        decidedFlg = True
        cost = -1
        qNode = -1
        for nextNode in treeDict[node]:
            nextCost = costDict[nextNode]
            if nextCost == 0:
                # 隣接ノードがコスト未設定ならキューに格納
                # 隣接ノードが2つコスト未設定ならbreak
                if not decidedFlg:
                    cost = -1
                    qNode = -1
                    break
                decidedFlg = False
                qNode = nextNode
            else:
                # コストが設定されていれば大きいコストで更新
                cost = max(cost, nextCost + 1)

        if cost != -1:
            costList.append((node, cost))
        if qNode != -1:
            tQ.add(qNode)

    for cost in costList:
        costDict[cost[0]] = cost[1]
    treeQ = tQ


# コストが設定されていないノードを頂点として直径を図る
firstLen, secondLen = 0, 0
for nextNode in treeDict[node]:
    cost = costDict[nextNode]
    if cost > firstLen:
        secondLen = firstLen
        firstLen = cost
    elif cost > secondLen:
        secondLen = cost

diameter = firstLen + secondLen + 1
ans = "First" if diameter % 3 != 2 else "Second"
print(ans)

