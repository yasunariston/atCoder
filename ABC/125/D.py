N = int(input())
AList = list(map(int, input().split()))

absAList = [abs(i) for i in AList]
ans = sum(absAList)
if len([i for i in AList if i < 0]) % 2 == 1:
    ans -= min(absAList) * 2

print(ans)

