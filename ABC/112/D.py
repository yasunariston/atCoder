import math
N, M = [int(i) for i in input().split()]

ans = 1

sosu = True if M % 2 == 1 else False

if M % 2 == 1:
    sqrt = int(math.ceil(math.sqrt(M)))
    for i in range(3, sqrt, 2):
        if M % i == 0:
            sosu = False
            break

if sosu == False:
    for i in range(N, M):
        if M % i == 0:
            ans = M / i
            break


print(int(ans))

