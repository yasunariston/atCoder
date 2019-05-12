import math

N, P = [int(i) for i in input().split()]

max_num = 1
for i in range(1, P+1):
    nums = int(math.pow(i, N))
    if nums <= P:
        if P % nums == 0:
            max_num = i
    else:
        break

print(max_num)
