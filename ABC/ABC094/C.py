#coding: utf-8
import math

N = int(input())
original_list = [int(i) for i in input().split()]
sorted_list = sorted(original_list)
min_midian = sorted_list[int(N / 2) - 1]
max_midian = sorted_list[int(N / 2)]

for i in range(N):
  if min_midian >= original_list[i]:
    print(max_midian)
  else:
    print(min_midian)
