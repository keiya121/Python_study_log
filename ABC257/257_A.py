N,X = map(int,input().split())
if X >= N:
    alp = chr(-(-X//N) + 64)
    print(alp)
else:
    print("A")