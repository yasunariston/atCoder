import math
N = int(input())

def retPlace(num):
    retVal = str(num % 2)
    num = math.ceil(num / (-2))
    if num != 0:
        retVal += retPlace(num)
    return retVal

ans = retPlace(N)
print(ans[::-1])
