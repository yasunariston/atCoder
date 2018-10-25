NM = [int(i) for i in input().split()]
N, M = NM[0], NM[1]
cakes = [[int(i) for i in input().split()] for _ in range(N)]
ans = 0

for i in range(8):
    cakeList = []
    if i == 0:
        cakes.sort(key=lambda cake:cake[0]+cake[1]+cake[2])
    elif i == 1:
        cakes.sort(key=lambda cake:cake[0]+cake[1]-cake[2])
    elif i == 2:
        cakes.sort(key=lambda cake:cake[0]-cake[1]+cake[2])
    elif i == 3:
        cakes.sort(key=lambda cake:0-cake[0]+cake[1]+cake[2])
    elif i == 4:
        cakes.sort(key=lambda cake:cake[0]-cake[1]-cake[2])
    elif i == 5:
        cakes.sort(key=lambda cake:0-cake[0]+cake[1]-cake[2])
    elif i == 6:
        cakes.sort(key=lambda cake:0-cake[0]-cake[1]+cake[2])
    elif i == 7:
        cakes.sort(key=lambda cake:0-cake[0]-cake[1]-cake[2])
    cakes.reverse()

    x, y, z = 0, 0, 0
    for counta, cake in enumerate(cakes):
        if counta >= M:
            break
        x += cake[0]
        y += cake[1]
        z += cake[2]
    point = abs(x) + abs(y) + abs(z)

    if point > ans:
        ans = point
print(ans)
