N = int(input())
S = input()

white, black, lastBlack = 0, 0, 0
blackFlag = False
for i in range(N):
    if S[i] == "." and blackFlag:
        white += 1
        lastBlack = 0
    if S[i] == "#":
        black += 1
        lastBlack += 1
        blackFlag = True

print(min(white, black - lastBlack))

