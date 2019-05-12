A, B = [int(i) for i in input().split()]
large = max(A, B)

ans = A + B
if A != B:
    ans = large + large - 1

print(ans)



