S = input()
ACGT = ["A", "C", "G", "T"]

ans = 0
length = 0
for i in range(len(S)):
    if S[i] in ACGT:
        length += 1
        ans = max(ans, length)
    else:
        length = 0

print(ans)
