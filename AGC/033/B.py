H, W, N = map(int, input().split())
sr, sc = map(int, input().split())
S, T = input(), input()

# border
lB, rB, uB, dB = 0, W + 1, 0, H + 1

ans = "YES"
for i, (s, t) in enumerate(zip(reversed(S), reversed(T))):
    if i != 0:
        if t == "R":
            lB = max(0, lB - 1)
        elif t == "L":
            rB = min(W + 1, rB + 1)
        elif t == "D":
            uB = max(0, uB - 1)
        elif t == "U":
            dB = min(H + 1, dB + 1)

    if s == "R":
        rB -= 1
    elif s == "L":
        lB += 1
    elif s == "D":
        dB -= 1
    elif s == "U":
        uB += 1

    if (rB - lB) == 1 or (dB - uB) == 1:
        ans = "NO"
        break

if not lB < sc < rB or not uB < sr < dB:
    ans = "NO"

print(ans)

