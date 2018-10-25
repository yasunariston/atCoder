s = input()
t = input()
ans = "No"

for s_index  in range(len(s)):
    for t_index in range(len(t)):
        flag = True
        index = (s_index + t_index) % len(s)
        if s[index] != t[t_index]:
            flag = False
            break
    if flag:
        ans = "Yes"
        break

print(ans)
