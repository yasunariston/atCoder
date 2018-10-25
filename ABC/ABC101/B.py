N = input()
ans = "No"
sn = 0

for i in range(len(N)):
    sn += int(N[i])

if int(N) % sn == 0:
    ans = "Yes"

print(ans)
