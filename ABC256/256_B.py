N = int(input())
A = list(map(int,input().split()))
P = 0
Masu = []
exc = []
exc_copy = []

for j in range(N):
    Masu.append(0)
    if len(exc) >= 1:
        for l in range(len(exc)):
            Masu.remove(exc[l])
    Masu = [x+A[j] for x in Masu]
    exc = []
    print(Masu)
    for i in range(len(Masu)):
        if Masu[i] > 3:
            exc.append(Masu[i])
            exc_copy.append(exc[0:])
        
P += len(exc_copy)
            
print(P)
