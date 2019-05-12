import math

N, K = [int(i) for i in input().split()]
ans = 0

if K == 1:
    ans = int(math.pow(N, 3))
if K % 2 == 1:
    ans = 
