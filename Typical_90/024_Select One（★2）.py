N,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

def abs_return(x,y):
    return abs(y-x)

C = list(map(abs_return,A,B))
#print(C)

sum_C = sum(C)

if sum_C <= K and (K-sum_C)%2 == 0:
    print("Yes")
else:
    print("No")