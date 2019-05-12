N, M = [int(i) for i in input().split()]
pList = []
for _ in range(N):
    pList.append(int(input()))

pList.sort(reverse=True)
min_rest = M
for _i1 in range(N):
    restList = []
    rest_i1 = rest - pList[_i1]
    



ans = str(M - min_rest)
print(ans)
