N = int(input())

ans = 0
aEnd = 0
bStart = 0
abBoth = 0
for _ in range(N):
    s = input()
    if s[0] == "B":
        bStart += 1
    if s[-1] == "A":
        aEnd += 1
        if s[0] == "B":
            abBoth += 1

    for i in range(len(s) - 1):
        if s[i:i+2] == "AB":
            ans += 1

ans += min(aEnd, bStart)
if abBoth != 0 and abBoth == aEnd == bStart:
    ans -= 1

print(ans)




