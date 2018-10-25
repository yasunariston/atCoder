import math

N = int(input())
ans = N

def getMaxNine(num):
    max_nine = 0
    for i in range(1 + N):
        nine_pow = math.pow(9, i)
        if nine_pow >= num:
            max_nine = nime_pow
        else:
            return max_nine

def getMaxSix(num):
    max_six = 0
    for i in range(N):
        six_pow = math.pow(6, i)
        if six_pow >= num:
            max_six = six_pow
        else:
            return max_six


def decrease(rest, count):
    global ans
    if rest == 0:
        if count < ans:
            ans = count
        return

    max_nine = getMaxNine(rest)
    decrease(rest - max_nine, count)
    max_six = getMaxSix(rest)
    decrease(rest - max_six, count)

decrease(N, 0)
print(ans)

