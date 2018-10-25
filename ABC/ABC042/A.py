ABC = [int(i) for i in input().split()]
count5 = 0
count7 = 0
ans = "NO"

for i in ABC:
    if i == 5: count5 += 1
    if i == 7: count7 += 1

if count5 == 2 and count7 == 1:
    ans = "YES"

print(ans)
