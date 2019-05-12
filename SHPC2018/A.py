import math

c, d = [int(i) for i in input().split()]

ans = 0
i = 0
while(True):
    multiply = math.pow(2, i)
    left, right = 140 * multiply, 170 * multiply
    if left < d:
        ans += min(max(0, right - c), right - left, d - left, d - c)
    else:
        break
    i += 1
print(int(ans))
