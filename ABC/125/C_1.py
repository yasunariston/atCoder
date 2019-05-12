N = int(input())
AList = list(map(int, input().split()))

def getNum(a, b):
    while(True):
        if a == b:
            return a
        a, b = max(a, b), min(a, b)
        a -= b

ansList = []
for i in range(0, N-1):
    ansList.append(getNum(AList[i], AList[i+1]))

print(sorted(ansList, reverse=False)[1])
