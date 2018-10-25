#coding:utf-8
import numpy as np

n = int(input())
comb_list = [int(i) for i in input().split()]

max_num = max(comb_list)
idx = np.abs(np.asarray(comb_list) - (max_num / 2)).argmin()
ans = comb_list[idx]
if ans == max_num:
  ans = 0

print(max_num, ans)
