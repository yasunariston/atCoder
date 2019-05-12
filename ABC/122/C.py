N, Q = [int(i) for i in input().split()]
S = input()
lrList = [[int(i) for i in input().split()] for _ in range(Q)]

ACNum = 0
ACList = [0]
for i in range(1, len(S)):
    if S[i - 1:i + 1] == "AC":
        ACNum += 1
    ACList.append(ACNum)

for q in range(Q):
    l, r = lrList[q][0], lrList[q][1]
    ans = ACList[r - 1] - ACList[l - 1]
    print(ans)
