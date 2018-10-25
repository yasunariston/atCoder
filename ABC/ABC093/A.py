#coding:utf-8

S = input()
S_set = set()

for i in range(len(S)):
    S_set.add(S[i])

if len(S_set) >= 3:
    print("Yes")
else:
    print("No")
