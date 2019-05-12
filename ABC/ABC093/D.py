#coding: utf-8
import math

N = int(input())
ans = []

for query in range(N):
  AB = [int(i) for i in input().split()]
  border = math.floor(math.sqrt(AB[0] * AB[1]))
  ans.append((border - 1) * 2)

for i in range(len(ans)):
  print(ans[i])

