R, C = [int(i) for i in input().split()]
X, Y = [int(i) for i in input().split()]
D, L = [int(i) for i in input().split()]
mod = 10 ** 9 + 7

#RCとXYが取りうる組み合わせ
RC_XY = (R - X + 1) * (C - Y + 1)

#XYとDLが取りうる組み合わせ(X * Y = D + L)
XY_DL = 0
#パスカルの三角形
D_L = D + L

beforePascal = []
for i in range(D_L):
    pascal = [1]
    for j in range(1, len(beforePascal)):
        pascal.append((beforePascal[j-1] + beforePascal[j]) % mod)
    pascal.append(1)
    beforePascal = pascal.copy()

ans = int(RC_XY * pascal[D] % mod)
print(ans)

