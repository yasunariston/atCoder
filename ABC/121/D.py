import math

A, B = [int(i) for i in input().split()]
exclusiveA = 0
exclusiveB = 0
B += 1
for i in range(len(bin(B)) - 2):
    factorialNum = int(math.pow(2, i))
    numA = A // (factorialNum * 2) * factorialNum
    numA += max(A % (factorialNum * 2) - factorialNum, 0)
    numB = B // (factorialNum * 2) * factorialNum
    numB += max(B % (factorialNum * 2) - factorialNum, 0)
    if numA % 2 == 1:
        exclusiveA += factorialNum
    if numB % 2 == 1:
        exclusiveB += factorialNum

print(exclusiveB ^ exclusiveA)
