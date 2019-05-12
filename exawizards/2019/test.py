#分かりやすい解説記事
#https://betrue12.hateblo.jp/entry/2019/03/31/084642

from collections import defaultdict as dd
mod=10**9+7
N,X=map(int,input().split())
S=sorted(list(map(int,input().split())),reverse=True)
#print(S)
d = dd(int)
d[X] = 1
for i in range(N):
    new = dd(int)
    for X in d:
        new[X] += d[X]*(N-i-1)
        new[X] %= mod
        #print(X,new[X])
        new[X%S[i]] += d[X]
        new[X%S[i]] %= mod
    d = new
ans = 0
print(d)
for x in d:
    ans += x*d[x]
    ans %= mod
print(ans)

