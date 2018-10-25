S = input()
w = int(input())

ans = ""
for i in range(0, len(S), w):
    ans += S[i]

print(ans)
