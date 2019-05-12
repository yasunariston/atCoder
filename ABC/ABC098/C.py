#coding:utf-8

'''TLE
N = int(input())
S = input()
ans = N

for reader in range(N):
    changer = 0
    for i in range(N):
        if (reader < i and S[i] == "E")\
        or (reader > i and S[i] == "W"):
            changer += 1
    if changer < ans:
        ans = changer

print(ans)
'''

N = int(input())
S = input()
ans = 0

for i in range(N):
    if S[i] == "E":
        ans += 1
min_ans = ans

for reader in range(1, N):
    minus = 0
    if S[reader] == "E":
        minus = 1
    if S[reader - 1] == "W":
        ans += 1
    elif S[reader - 1] == "E":
        ans -= 1
    if ans - minus < min_ans:
        min_ans = ans - minus
        count = reader

print(min_ans)
