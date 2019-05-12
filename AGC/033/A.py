H, W = map(int, input().split())
func = (lambda x: 1 if x == "#" else 0)
field = [[func(i) for i in input()] for _ in range(H)]
blackQ = []

for i, wField in enumerate(field):
    for j, w in enumerate(wField):
        if w == 1:
            blackQ.append((i, j))

ans = 0
while(True):
    bQ = []
    for _ in range(len(blackQ)):
        i, j = blackQ.pop()
        if i - 1 >= 0 and field[i-1][j] != 1:
            field[i-1][j] = 1
            bQ.append((i - 1, j))
        if i + 1 <= H - 1 and field[i+1][j] != 1:
            field[i+1][j] = 1
            bQ.append((i + 1, j))
        if j - 1 >= 0 and field[i][j-1] != 1:
            field[i][j-1] = 1
            bQ.append((i, j - 1))
        if j + 1 <= W - 1 and field[i][j + 1] != 1:
            field[i][j+1] = 1
            bQ.append((i, j + 1))

    if len(bQ) == 0:
        break

    ans += 1
    blackQ = bQ

print(ans)

