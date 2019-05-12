import numpy as np
from sys import stdin
from collections import defaultdict
input = stdin.readline
N, W = list(map(int, input().split()))
wvList = [list(map(int, input().split())) for _ in range(N)]

v_sum = sum([wv[1] for wv in wvList])
V_list = np.ones(v_sum)*np.inf


v_dict = defaultdict(int)
v_dict[0]=0

for wv in wvList:
    w,v = wv
    for v_key in list(v_dict.keys()):
        val  = min( v_dict[v_key]+w if v_dict[v_key]+w <=W else np.inf,
                   v_dict[v_key+v] if (v_key+v) in v_dict.keys() and v_dict[v_key+v] != 0 else np.inf)
        if not np.isinf(val) and val != 0:
            v_dict[v_key+v] = val

print(max(v_dict.keys()))
