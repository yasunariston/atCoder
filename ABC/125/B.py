N = int(input())
vList = list(map(int, input().split()))
cList = list(map(int, input().split()))

ans = 0
for i in range(N):
    if vList[i] - cList[i] > 0:
        ans += vList[i] - cList[i]

print(ans)

