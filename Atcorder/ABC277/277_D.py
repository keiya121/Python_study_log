import sys
sys.setrecursionlimit(2*10 ** 5)

N,M = map(int,input().split())
A = list(map(int,input().split()))
X = list(A)
ans = []

def soli(i):
    global X
    del X[X.index(i)]
    if i in X:
        return(soli(i))
    elif (i+1) % M in X:
        return(soli((i+1)%M)) 
    else:
        return sum(X)

for i in A:
    X = list(A)
    ans.append(soli(i))

print(min(ans))




