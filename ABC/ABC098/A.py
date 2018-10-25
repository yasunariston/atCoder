#coding: utf-8

AB = [int (i) for i in input().split()]
A, B = AB[0], AB[1]

ans = max(A + B, A - B, A * B)
print(ans)
