s = input()
k = int(input())
ans = 0

sum_num = 0
for i in range(len(s)):
    num = int(s[i])
    if num == 1:
        sum_num += 1
        if sum_num >= k:
            ans = 1
            break
    else:
        ans = num
        break

print(ans)
