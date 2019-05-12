N, X= [int(i) for i in input().split()]
abList = [[int(i) for i in input().split()] for _ in range(N)]

ans = 0
maxFace = 0
for ab in abList:
    ans += ab[0] * ab[1]
    maxFace = max(maxFace, ab[1])

ans += maxFace * X
print(ans)


