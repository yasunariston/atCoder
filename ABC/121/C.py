N, M = [int(i) for i in input().split()]
ABList = [[int(i) for i in input().split()] for _ in range(N)]
ABList.sort(key=lambda x: x[0], reverse=False)

ans = 0
for AB in ABList:
    drink = min(AB[1], M)
    M -= drink
    ans += drink * AB[0]
    if M == 0:
        break

print(ans)
