#coding: utf-8

NMX = [int(i) for i in input().split()]
N, M, X = NMX[0],  NMX[1],  NMX[2]
fee_station = [int(i) for i in input().split()]

increase = 0
decrease = 0

for i in range(M):
  if fee_station[i] > X:
    increase += 1
  else:
    decrease += 1

print(min(increase, decrease))
