import math

N = int(input())
S = input()

strDict = {}
for i in range(N):
    if S[i] in strDict:
        strDict[S[i]] += 1
    else:
        strDict[S[i]] = 1

ans = 1
for s in strDict:
    ans *= strDict[s] + 1

ans -= 1
print(ans)
