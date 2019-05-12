#coding:utf-8

N = int(input())
A = [int(i) for i in input().split()]
ans = 0
formula1 = 0
formula2 = 0
lastRight = 0

for left in range(N):
    rightOut = False
    if left > 0:
        formula1 ^= A[left - 1]
        formula2 -= A[left - 1]
    for right in range(lastRight, N):
        formula1 ^= A[right]
        formula2 += A[right]
        if formula1 != formula2:
            rightOut = True
            formula1 ^= A[right]
            formula2 -= A[right]
            break

    lastRight = max(left, right - rightOut) + 1
    ans += lastRight - left
print(ans)
