N = int(input())
numList = []

def isPrime(num):
    retVal = True
    if num % 2 == 0:
        retVal = False
    else:
        for n in range(3, num//2, 2):
            if num % n == 0:
                retVal = False
                break
    return retVal

num = 6
for i in range(N):
    for prime in range(num+5, 55555, 5):
        if isPrime(prime):
            num = prime
            numList.append(prime)
            break

ans = " ".join(map(str, numList))
print(ans)

