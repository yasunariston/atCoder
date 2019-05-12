N, M = [int(i) for i in input().split()]
idx = 0
ipyList = []
for i in range(M):
    idx += 1
    ipy = [int(i) for i in input().split()]
    ipy.insert(0, idx)
    ipyList.append(ipy)

ipyList = sorted(ipyList, key=lambda ipy: ipy[2])
cityMap = {}
for ipy in ipyList:
    if ipy[1] in cityMap.keys():
        cityMap[ipy[1]] += 1
    else:
        cityMap[ipy[1]] = 1
    ipy[2] = cityMap[ipy[1]]

ipyList = sorted(ipyList, key=lambda ipy: ipy[0])
for ipy in ipyList:
    print(str(ipy[1]).zfill(6) + str(ipy[2]).zfill(6))

