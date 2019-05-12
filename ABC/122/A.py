b = input()

ans = ""
for i in range(len(b)):
    if b[i] == "A":
        ans += "T"
    elif b[i] == "T":
        ans += "A"
    elif b[i] == "C":
        ans += "G"
    elif b[i] == "G":
        ans += "C"

print(ans)
