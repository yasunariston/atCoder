N = int(input())
field = [["." for _ in range(N)] for _ in range(N)]

for x in range(N):
    for y in range(N):
        if ((x+1) + 2*(y+1)) % 5 == 0:
            field[x][y] = "X"

for x in range(N):
    for y in range(N):
        if field[x][y] == ".":
            left = field[x][max(0, y-1)]
            right = field[x][min(y+1, N-1)]
            over = field[max(0, x-1)][y]
            under = field[min(x+1, N-1)][y]
            if left != "X" and right != "X" and over != "X" and under != "X":
                field[x][y] = "X"

for sList in field:
    print("".join(sList))
