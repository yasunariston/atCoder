N = int(input())

ans = N - 1 if N != 2 else 0
for i in range(2, int(N ** 0.5) + 1):
    if N % i == 0:
        a = N // i
        b = i
        if N // (a-1) == N % (a-1):
            ans += a-1
        if N // (b-1) == N % (b-1):
            ans += b-1

print(ans)

