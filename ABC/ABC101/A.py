eatStr = input()
plus, minus = 0, 0
for i in range(len(eatStr)):
    if eatStr[i] == "+":
        plus += 1
    elif eatStr[i] == "-":
        minus += 1

print(plus - minus)
