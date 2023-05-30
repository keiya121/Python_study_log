N,M = map(int,input().split())
a = list(map(int,input().split()))
ans = []


def read(x):
    global ans,a
    while(len(a) != 0):
      if x + 1 not in a:
          ans.append(x+1)
          if x not in ans:
              ans.append(x)
      else:
          a.remove(x)
          return(min(a))

read(min(a))
print(ans)

import torch
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

import json

