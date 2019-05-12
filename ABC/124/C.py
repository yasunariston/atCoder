S = input()
N = len(S)

str01 = "01" * (N // 2)
str10 = "10" * (N // 2)
if N % 2 == 1:
    str01 += "0"
    str10 += "1"

ans01 = 0
ans10 = 0
for i in range(N):
    if S[i] != str01[i]:
        ans01 += 1
    if S[i] != str10[i]:
        ans10 += 1

print(min(ans01, ans10))

