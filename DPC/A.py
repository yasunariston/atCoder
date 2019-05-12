from statistics import mean

N = int(input())
a = [int(i) for i in input().split()]

a_mean = mean(a)

ans = 0
ans_dist = max(a)
for i, frame in enumerate(a):
    dist = abs(frame - a_mean)
    if dist < ans_dist:
        ans_dist = dist
        ans = i

print(ans)
