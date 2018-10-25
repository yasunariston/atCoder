import math

DN = [int(i) for i in input().split()]
D, N = DN[0], DN[1]

print(int(math.pow(100, D)) * N)
