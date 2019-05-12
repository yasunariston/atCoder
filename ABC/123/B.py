ABCDE = [int(input()) for i in range(5)]
ABCDE.sort(key = lambda x : x % 10 if x % 10 != 0 else 10)

ans = 0
for i, element in enumerate(ABCDE):
    if i == 0:
        ans += element
    else:
        wait = 10 - element % 10 if element % 10 != 0 else 0
        ans += element + wait


print(ans)

