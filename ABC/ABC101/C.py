NK = [int(i) for i in input().split()]
N, K = NK[0], NK[1]
A = input()
ans = (N - K) // (K - 1) + 1
if (N - K) % (K - 1) != 0:
    ans += 1

print(ans)
