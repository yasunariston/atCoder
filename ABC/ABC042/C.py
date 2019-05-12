N, K = [int(i) for i in input().split()]
d = [s for s in input().split()]
ans = N

while(True):
    sAns = str(ans)
    for i in range(len(sAns)):
        if sAns[i] in d:
            ans += 1
            break
    else:
        break

print(ans)
