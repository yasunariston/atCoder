S = input()
ans = 0

lastColor = S[0]
for i in range(1, len(S)):
    if S[i] != lastColor:
        lastColor = S[i]
        ans += 1

print(ans)
