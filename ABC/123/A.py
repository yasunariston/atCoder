abcde = [int(input()) for i in range(5)]
k = int(input())

ans = "Yay!"
for element in abcde:
    if element > k:
        ans = ":("

print(ans)


