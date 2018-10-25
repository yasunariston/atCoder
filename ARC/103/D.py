N = int(input())
xyList = [[int(i) for i in input().split()] for _ in range(N)]

def culcNumList(num):
    numList = [1]
    lastNum = 2
    while(True):
        if lastNum >= num:
            return numList
        numList.append(lastNum)
        lastNum *= 2

max_sum = 0
oddFlag = False
evenFlag = False
for xy in xyList:
    sum_xy = sum(xy)
    max_sum = max(sum_xy, max_sum)
    if sum_xy % 2 == 0: evenFlag = True
    else: oddFlag = True

if oddFlag and evenFlag:
    print(-1)
else:
    d = culcNumList(max_sum)[::-1]
    if evenFlag: d.append(1)
    print(len(d))
    print(" ".join([str(s) for s in d]))

    for xy in xyList:
        nowX, nowY = 0, 0
        ans = ""
        for arm in d:
            if abs(nowX - xy[0]) >= abs(nowY - xy[1]):
                if nowX > xy[0]:
                    ans += "L"
                    nowX -= arm
                else:
                    ans += "R"
                    nowX += arm
            else:
                if nowY > xy[1]:
                    ans += "D"
                    nowY -= arm
                else:
                    ans += "U"
                    nowY += arm
        print(ans)

