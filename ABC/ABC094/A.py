#coding: utf-8

ABX = [int(i) for i in input().split()]
A, B, X = ABX[0],  ABX[1],  ABX[2]

if A + B >= X and A <= X:
  print("YES")
else:
  print("NO")
