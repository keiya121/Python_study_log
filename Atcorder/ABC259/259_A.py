N,M,X,T,D = map(int,input().split())

if X <= M <= N:
    print(T)
else:
    ori = T - D*X
    print(ori + D*M)