X, Y, Z, K = [int(i) for i in input().split()]
ABCList = [sorted([int(i) for i in input().split()], reverse=True) for _ in range(3)]

ABSum = sorted([i + j for i in ABCList[0] for j in ABCList[1]], reverse=True)[:K]
for ans in sorted([i + j for i in ABSum for j in ABCList[2]], reverse=True)[:K]:
    print(ans)
