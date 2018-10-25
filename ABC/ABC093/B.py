#coding:utf-8

ABK = [int(i) for i in input().split()]
A, B, K = ABK[0], ABK[1], ABK[2]

if (B - A)/2 >= K:
  for i in range(A, A+K):
    print(i)
  for i in range(B-K+1, B+1):
    print(i)

else:
  for i in range(A, B+1):
    print(i)

