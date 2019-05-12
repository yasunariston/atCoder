N = int(input())
S = input()

ans = 0
for i in range(N):
    X, Y = set(), set()
    for j in range(N):
        if j < i:
            X.add(S[j])
        else:
            Y.add(S[j])

    same = len(X & Y)
    if same > ans:
        ans = same
print(ans)
