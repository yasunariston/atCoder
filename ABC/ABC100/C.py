N = int(input())
a = [int(i) for i in input().split()]
count = 0

def half(num, count):
    count += 1
    if num % 2 == 0:
        count = half(num//2, count)
    return count

for num in a:
    if num % 2 == 0:
        count += half(num//2, 0)

print(count)
