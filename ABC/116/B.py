s = int(input())

numList = [s]
count = 0
ans = 2
while(True):
    nextNum = numList[count] / 2 if numList[count] % 2 == 0 else numList[count] * 3 + 1

    if nextNum in numList:
        print(ans)
        break
    numList.append(nextNum)
    count += 1
    ans += 1

