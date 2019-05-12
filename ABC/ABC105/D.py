import numpy as np

N, M = [int(i) for i in input().split()]
A = np.cumsum(np.array(input().split(), dtype=int)) % M
ans = 0

remainder = {}
for i in A:
    if i in remainder:
        remainder[i] += 1
    else:
        remainder[i] = 1

for key in remainder:
    ans += remainder[key] * (remainder[key] - 1) / 2

ans += remainder[0] if 0 in remainder else 0

print(int(ans))

'''
N, M = [int(i) for i in input().split()]
A = np.cumsum(np.array(input().split(), dtype=int))
ans = 0

for first in range(N):
    for last in range(first, N):
        if first == last:
            if A[first] % M == 0:
                ans += 1
        else:
            if (A[last] - A[first]) % M == 0:
                ans += 1

print(ans)
'''
