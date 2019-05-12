NX = input().split()
N, X = int(NX[0]), int(NX[1])
donut_list = []
for i in range(N):
    donut_list.append(int(input()))

X -= sum(donut_list)
min_donut = min(donut_list)
ans = N + X // min_donut

print(ans)
