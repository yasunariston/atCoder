N = int(input())
aList = [int(input()) for _ in range(N)]

ans = "first"
for a in aList:
    if a % 2 == 1:
        break
else:
    ans = "second"

print(ans)
