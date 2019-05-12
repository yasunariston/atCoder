N, M = [int(i) for i in input().split()]
X = [int(i) for i in input().split()]
X.sort()

diffList = [X[i+1] - X[i] for i in range(M - 1)]
diffList.sort()

ans = 0
if N - M < 0:
    ans += sum(diffList[:M - N])

print(ans)
