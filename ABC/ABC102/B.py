N = int(input())
a = [int(i) for i in input().split()]

ans = max(a) - min(a)
print(ans)
