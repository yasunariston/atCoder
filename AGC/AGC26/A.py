N = int(input())
a = [int(i) for i in input().split()]

ans = 0

count = 1
pre_num = a[0]
for i in range(1, len(a)):
    if a[i] == pre_num:
        count += 1
    else:
        ans += count // 2
        count = 1
        pre_num = a[i]
ans += count // 2
print(ans)
