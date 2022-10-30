from functools import reduce
N = int(input())

if N == 0:
    print(1)

else:
    li = [i+1 for i in range(N)]
    def multi(a,b):
       return a*b
    ans = reduce(multi,li)

    print(ans)
    





