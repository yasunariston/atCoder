X, Y, Z, K = [int(i) for i in input().split()]
ABCList = [sorted([int(i) for i in input().split()], reverse=True) for _ in range(3)]

ansList = []
for i, A in enumerate(ABCList[0]):
    for j, B in enumerate(ABCList[1]):
        for k, C in enumerate(ABCList[2]):
            if (i + 1) * (j + 1) * (k + 1) <= K:
                ansList.append(A + B + C)
            else:
                break

for ans in sorted(ansList, reverse=True)[:K]:
    print(ans)

