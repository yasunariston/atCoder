A, B, C = [s for s in input().split()]
ans = "NO"

if A[-1] == B[0] and B[-1] == C[0]:
    ans = "YES"

print(ans)
