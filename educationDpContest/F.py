import sys
import string, random
def randomname(n):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=n))

input = sys.stdin.readline
sList, tList = list(randomname(3000)), list(randomname(3000))

dp = [[""] * (len(tList) + 1) for _ in range(2)]
index = 0
for i, s in enumerate(sList, start=1):
    index = i % 2
    sameStr = ""
    for j, t in enumerate(tList, start=1):
        aboveStr = dp[index-1][j]
        if s == t:
            sameStr = dp[index-1][j-1] + s
        dp[index][j] = sameStr if len(sameStr) > len(aboveStr) else aboveStr

print(dp[index][-1])


"""

dp = [s_index][t_index] = count

axyb
abyxb

0 1 2 3 4 5 t
1 1 0 0 0 0
2 0 0 0 1 0
3 0 0 1 0 0
4 0 1 0 0 1
s

0 1 2 3 4 5 t
1 1 1 1 1 1
2 1 1 1 2 2
3 1 1 2 2 2
4 1 2 2 2 3
s

"""
