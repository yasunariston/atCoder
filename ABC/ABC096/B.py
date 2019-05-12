abc = [int(i) for i in  input().split()]
k = int(input())

max_num = max(abc)
others = sum(abc) - max_num
for i in range(k):
    max_num *= 2

print(max_num + others)
