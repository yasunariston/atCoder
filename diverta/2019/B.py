R, G, B, N = map(int, input().split())

ans = 0
for i in range(N // R + 1):
    r = i * R
    for j in range(N // G + 1):
        g = j * G
        rest = N - (r + g)
        if rest >=  0 and rest % B == 0:
            ans += 1

print(ans)

