N = int(input())
AList = list(map(int, input().split()))


def getNum(a, b):
    while(True):
        if a == b:
            return a
        a, b = max(a, b), min(a, b)
        a -= b

ans = max(AList)
AList = sorted(list(set(AList)))
if len(AList) >= 3:
    ansA = getNum(AList[0], AList[1])
    ansB = getNum(AList[1], AList[2])
    ansC = getNum(AList[2], AList[0])
    ansD, ansE = AList[0], AList[2]
    aFlag, bFlag, cFlag, dFlag, eFlag = True, True, True, True, True
    for num in AList:
        if num % ansA != 0:
            if not aFlag:
                ansA = 1
            aFlag = False
        if num % ansB != 0:
            if not bFlag:
                ansB = 1
            bFlag = False
        if num % ansC != 0:
            if not cFlag:
                ansC = 1
            cFlag = False
        if num % ansD != 0:
            if not dFlag:
                ansD = 1
            dFlag = False
        if num % ansE != 0:
            if not eFlag:
                ansE = 1
            eFlag = False
    ans = max(ansA, ansB, ansC, ansD, ansE)

print(ans)
