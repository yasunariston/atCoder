xyabc = [int(i) for i in input().split()]

defaultX, defaultY = xyabc[0], xyabc[1]
for i, xy in enumerate(xyabc):
    xyabc[i] -= defaultX if i % 2 == 0 else defaultY

ans = abs(xyabc[2] * xyabc[5] - xyabc[3] * xyabc[4]) / 2
print(ans)
