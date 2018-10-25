abcd = [int(i) for i in input().split()]
ans = "Yes"

ab, bc, ac = abs(abcd[1]-abcd[0]), abs(abcd[2]-abcd[1]), abs(abcd[2]-abcd[0])
d = abcd[3]

if ab > d or bc > d:
    ans = "No"
if ac <= d:
    ans = "Yes"

print(ans)
