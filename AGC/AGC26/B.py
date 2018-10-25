T = int(input())

for i in range(T):
    abcd = [int(i) for i in input().split()]
    a, b, c, d = abcd[0], abcd[1], abcd[2], abcd[3]
    ans = "No"

    if a >= b and d >= b:
        if c >= b:
            ans = "Yes"
        else:
            dif = d - b
            first = a % b
            



    print(ans)

