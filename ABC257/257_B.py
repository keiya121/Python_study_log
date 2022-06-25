N,K,Q = map(int,input().split())
A = list((map(int,input().split())))
L = list((map(int,input().split())))

for i in L:
    if A[i-1] + 1 not in A and A[i-1] < N:
        A[i-1] += 1

def str_return(x):
    return str(x)

Ans = list(map(str_return,A))

print(" ".join(Ans))