import math

N = int(input())
min_road = N
ABCDE = [int(input()) for _ in range(5)]
for i, element in enumerate(ABCDE):
    min_road = min(min_road, element)

ans = int(math.ceil(N / min_road)) + 4
print(ans)

