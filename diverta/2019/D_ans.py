N = int(input())

ans = 0
for i in range(1, N):
    mod = N % i
    quo = N // i
    if mod == quo:
        print(i, quo, mod)
        ans += i

print(ans)

