N, M = [int(i) for i in input().split()]
S = input()
T = input()

ans = -1

largeNum, smallNum = max(N, M), min(N, M)
longStr = S if N > M else T
shortStr = T if N > M else S
step = largeNum // smallNum

if largeNum % smallNum == 0:
    for si, li in enumerate(range(0, largeNum, step)):
        print(si, li)
        if shortStr[si] != longStr[li]:
            break
    else:
        ans = largeNum
else:
    devide = 1
    a = largeNum
    b = smallNum
    while True:
        a -= b
        if a == b:
            devide = a
            break
        else:
            c = a
            a = max(a, b)
            b = min(b, c)

    ans = largeNum * smallNum // devide
print(ans)
