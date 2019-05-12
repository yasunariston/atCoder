N = int(input())
ans = "No"
i7 = 0


while(True):
    N -= i7 * 7
    if N < 0:
        break
    if N % 4 == 0 or N == 0:
        ans = "Yes"
        break
    i7 += 1

print(ans)
