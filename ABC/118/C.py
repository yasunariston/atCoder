N = int(input())
A = [int(i) for i in input().split()]
A.sort(reverse = True)

def calc(a, b):
    largeNum = max(a, b)
    smallNum = min(a, b)
    while(largeNum != 0 and smallNum != 0):
        largeNum %= smallNum
        x = largeNum
        largeNum = smallNum
        smallNum = x
    return max(smallNum, largeNum)

ans = 1
for i in range(0, N - 1):
    a = calc(A[i], A[i+1])
    A[i], A[i+1] = a, a
    if a == 1:
        break
else:
    ans = min(A)

print(ans)




