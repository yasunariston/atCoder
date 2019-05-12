K, A, B = [int(i) for i in input().split()]

bisk = 1
if A + 2 <= B:
    pon = A - bisk
    bisk += K if A > K else pon
    K -= K if A > K else pon
    bisk += (B - A) * (K // 2)
    K %= 2

bisk += K
print(bisk)

