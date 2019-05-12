N = int(input())
originStr = "123456"

quotient = (N // 5) % 6
mod = N % 5
sortedStr = originStr[quotient:] + originStr[:quotient]
ans = "{0}{1}{2}".format(sortedStr[1:mod + 1], sortedStr[0], sortedStr[mod + 1:])

print(ans)

