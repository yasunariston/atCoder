import numpy as np

N = int(input())
a = np.array(sorted([int(num) - i for i, num in enumerate(input().split())]))

if N % 2 == 0:
    center = int(N/2-1) if a[int(N/2-1)] >= a[int(N/2)] else int(N/2)
else:
    center = int((N-1)/2)

a = np.abs(a - a[center])
print(sum(a))
