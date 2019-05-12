N = int(input())
hList = [int(i) for i in input().split()]

ans = 0
height = 1
while(True):
    endFlag = True
    waterFlag = False
    for h in hList:
        if h >= height:
            if not waterFlag:
                ans += 1
            endFlag = False
            waterFlag = True
        elif h < height:
            waterFlag = False

    height += 1
    if endFlag:
        break

print(ans)

