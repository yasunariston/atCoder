N = int(input())
AList = list(map(int, input().split()))

def getNum(a, b):
    while(True):
        if a == 0:
            return b
        a, b = max(a, b), min(a, b)
        a %= b

leftGBC, rightGBC= [AList[0]], [AList[-1]]
for i in range(1, N):
    leftGBC.append(getNum(leftGBC[i - 1], AList[i]))
for i in range(1, N):
    rightGBC.append(getNum(rightGBC[i - 1], AList[N - i - 1]))

rightGBC.reverse()

ans = max(leftGBC[-2], rightGBC[1])
for i in range(0, N-2):
    ans = max(getNum(leftGBC[i], rightGBC[i + 2]), ans)

print(ans)

