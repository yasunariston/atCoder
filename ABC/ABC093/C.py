#coding: utf-8
import numpy as np

ABC = [int(i) for i in input().split()]
diff1 = max(ABC) - min(ABC)
diff2 = max(ABC) - int(np.median(ABC))

count = (diff1 + diff2)//2
if not diff1 % 2 == diff2 % 2:
  count += 2

print(int(count))
