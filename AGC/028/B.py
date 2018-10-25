N = int(input())
A = [int(i) for i in input().split()]
mod = 1000000007

#階乗計算
def factorial(num, count=1):
    for i in range(1, num+1):
        count *= i
    return count

#dpテーブル.未実装
dp = {}
def rmBlocks(A, count=0):
    #組み合わせパターン * Aのremoveコストを予め計算
    count += factorial(len(A)) * sum(A)

    #Aの長さが1以下なら終了
    if len(A) <= 1:
        return count

    #ブロックをiを起点に左右に切り分け再帰
    for i in range(len(A)):
        left = A[:i]
        right = A[i+1:]
        count += rmBlocks(left) + rmBlocks(right)
    #結果返却
    return count % mod

ans = rmBlocks(A)
print(ans)

