import re

N = int(input())

numList = []
def plusNum(num, N):
    if num > N:
        return
    numList.append(num)
    for i in [3, 5, 7]:
        plusNum(int(str(num) + str(i)), N)

for num in [3, 5, 7]:
    plusNum(num, N)

ans = 0
for num in numList:
    num_str = str(num)
    count_3 = 0
    count_5 = 0
    count_7 = 0
    for i in range(len(num_str)):
        if num_str[i] == "3":
            count_3 += 1
        elif num_str[i] == "5":
            count_5 += 1
        elif num_str[i] == "7":
            count_7 += 1
        if count_3 >= 1 and count_5 >= 1 and count_7 >= 1:
            ans += 1
            break

print(ans)



