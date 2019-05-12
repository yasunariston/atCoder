abList = []
for i in range(3):
    ab = [int(i) for i in input().split()]
    abList.append(ab)

visited = {}
for ab in abList:
    for i in ab:
        if i in visited:
            visited[i] += 1
        else:
            visited[i] = 1

ans = "YES"
for city in visited:
    if visited[city] == 0 or visited[city] > 2:
        ans = "NO"


print(ans)
