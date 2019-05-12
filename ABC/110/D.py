import math
N, M = [int(i) for i in input().split()]

def factoring(num):
    factor = {}

    while True:
        if num % 2 == 0:
            if 2 in factor:
                factor[2] += 1
            else:
                factor[2] = 1
        else:
            break

    for i in range(3, math.ceil(math.sqrt(M)), 2):
        if num % i == 0:


    return factor

ans = 1
factor = factoring(M)


print(factor)


'''
2 2 3 3 5 5 7 = 6300

3, 12
(1, 1, 12) = 3
(1, 2, 6) = 6
(1, 3, 4) = 6
(2, 2, 3) = 3

3, 343
(1, 1, 343) = 3
(1, 7, 49) = 6
(7, 7, 7) = 1
'''

