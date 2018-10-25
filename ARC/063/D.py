import numpy as np

N, T = np.array(input().split(), dtype="int")
A = np.array(input().split(), dtype="int")

sell = np.max(A)
max_profit = 0
ans = 0
for buy in range(N - 1):
    if A[buy] == sell:
        sell = np.max(A[buy+1:])

    profit = sell - A[buy]
    if profit > max_profit:
        max_profit = profit
        ans = 1
    elif profit == max_profit:
        ans += 1

print(min(ans, int(T / 2)))
