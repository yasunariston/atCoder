S = input()

i = 0
ans = 999
while(i <= len(S) - 3):
    num = int(S[i:i+3])
    if abs(num - 753) < ans:
        ans = abs(num - 753)
    i += 1

print(ans)

