N = int(input())
A = [int(i) for i in input().split()]

ans = 0
zeroFlag = False
for i in range(len(A)):
    if A[i] == 0:
        if zeroFlag and A[i-1] != 0:
            ans = -1
            break
        else:
            zeroFlag = True
    else:


