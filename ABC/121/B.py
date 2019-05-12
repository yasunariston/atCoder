N, M, C = [int(i) for i in input().split()]
BList = [int(i) for i in input().split()]
ALists = [[int(i) for i in input().split()] for _ in range(N)]

ans = 0
for AList in ALists:
    point = C
    for i, A in enumerate(AList):
        point += A * BList[i]
    if point > 0:
        ans += 1

print(ans)

