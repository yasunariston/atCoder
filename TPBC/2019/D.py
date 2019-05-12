N = int(input())
aList = [int(input()) for _ in range(N)]

sumA = sum(aList)
dp = [[] for _ in range(N)]

"""
  1 1 1 2
0 0 0 0 0
1 1 1 1 1
2
3
4


"""
