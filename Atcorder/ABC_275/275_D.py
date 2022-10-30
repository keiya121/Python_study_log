from functools import lru_cache
import sys
from functools import lru_cache
sys.setrecursionlimit(10 ** 9)

N = int(input())

@lru_cache
def cul(a):
    if a == 0:
        return 1
    return cul(int(a/2)) + cul(int(a/3))

ans = cul(N)
print(ans)