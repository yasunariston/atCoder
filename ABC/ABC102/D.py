from itertools import accumulate

N = int(input())
a = list(accumulate([int(i) for i in input().split()]))
l, r = 0, 1
ans = float("inf")
for i in range(1, N-2):
    while abs(a[i] - 2 * a[l+1]) < abs(a[i] - 2 * a[l]): l += 1
    while abs(a[-1] - 2 * a[r+1] + a[i]) < abs(a[-1] - 2 * a[r] + a[i]): r += 1
    t = [a[l], a[i] - a[l], a[r] - a[i], a[-1] - a[r]]
    ans = min(ans, max(t) - min(t))
print(ans)


'''
#Original

import queue

N = int(input())
ll, lr = a[1] - a[0], a[2] - a[1]
A = [int(i) for i in input().split()]

a = [0]
sum_A = 0
for i in range(N):
    sum_A += A[i]
    a.append(sum_A)

ll, lr = queue.Queue(), queue.Queue()
rl, rr = queue.Queue(), queue.Queue()
ll.put(a[1] - a[0]), lr.put(a[2] - a[1])

#右の初期最適解を求める


ans = float("inf")
for i in range(2, N - 1):


print(a)
'''
