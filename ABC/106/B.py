N = int(input())
ans = 0

for num in range(1, N+1, 2):
    divisor = 0
    for devide in range(1, N+1, 2):
        if num % devide == 0:
            divisor += 1
        if divisor > 8:
            break
    if divisor == 8:
        ans += 1

print(ans)
