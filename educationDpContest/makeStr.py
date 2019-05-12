import random, string

def randomname(n):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=n))

print("作成したい文字列の長さを入力してください。")
N = int(input())
print(randomname(N))



