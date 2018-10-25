ab = [int(i) for i in input().split()]
a, b = ab[0], ab[1]

ans = 'x'
if a + b == 15:
    ans = '+'
elif a * b == 15:
    ans = '*'

print(ans)
