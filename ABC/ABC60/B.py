A, B, C = [int(i) for i in input().split()]
num = 0
apperedNum = []
ans = "NO"

while(True):
    num += A
    remain = num % B
    if remain == C:
        ans = "YES"
        break
    elif remain in apperedNum:
        break
    apperedNum.append(remain)

print(ans)
