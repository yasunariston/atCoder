hw = [int(i) for i in input().split()]
ans = "Yes"

#low efficientcy
field = ["." * (hw[1] + 2)]
for h_i in range(hw[0]):
    field.append("." + input() + ".")
field.append("." * (hw[1] + 2))

for h_i in range(1, hw[0] + 1):
    if ans == "No":
        break
    for w_i in range(1, hw[1] + 1):
        if field[h_i][w_i] == "#":
            if field[h_i - 1][w_i] == "#" or field[h_i + 1][w_i] == "#"\
            or field[h_i][w_i - 1] == "#" or field[h_i][w_i + 1] == "#":
                continue
            ans = "No"
            break
print(ans)
