R, G, B = [int(i) - 1 for i in input().split()]

def moveCount(num):
    return num

def deleteCount(num):
    return num * (-1)

rl, rr, gl, gr, bl, br = 0, 0, 0, 0, 0, 0
ans = 0

if R % 2 == 1:
    rl += 1
    ans += moveCount(rl)
for _ in range(R // 2):
    rl += 1
    rr += 1
    ans += moveCount(rl) + moveCount(rr)

if B % 2 == 1:
    br += 1
    ans += moveCount(br)
for _ in range(B // 2):
    bl += 1
    br += 1
    ans += moveCount(bl) + moveCount(br)


if G % 2 == 1:
    gr += 1
    ans += moveCount(gr)
for _ in range(G // 2):
    if rr + gl <= 98:
        gl += 1
        ans += moveCount(gl)

    if gr + bl <= 98:
        gr +=1
        ans += moveCount(gr)

print(rl, rr, gl, gr, bl, br)
print(ans)


