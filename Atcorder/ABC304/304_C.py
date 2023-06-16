import sys
input = sys.stdin.readline

class UNIONFIND:

    def __init__(self,n):
        self.n = n
        self.parents = [-1]*n

    def find(self,x):
        if self.parents[x] <0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    
    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        elif self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

N,D = map(int,input().split())
L = []

UF = UNIONFIND(N)

for i in range(N):
    L.append(list(map(int,input().split())))

for i in range(N):
    for j in range(i+1,N):
        dx = L[i][0] - L[j][0]
        dy = L[i][1] - L[j][1]
        if dx * dx + dy * dy <= D * D:
            UF.union(i,j)

X = UF.find(0)
for i in range(N):
    if X == UF.find(i):
        print("Yes")
    else:
        print("No")


            


