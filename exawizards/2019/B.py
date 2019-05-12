N = int(input())
S = input()

r = 0
b = 0
for s in S:
    if s == "R":
        r += 1
    else:
        b += 1

ans = "No"
if r > b:
    ans = "Yes"

print(ans)

