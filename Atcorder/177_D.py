class UNIONFIND:

    def __init__(self,n):
        self.n = n
        self.parents = [-1]*n

    def find(self,x):
        if self.parents[x] < 0:
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


N,M = map(int,input().split())
max = 0

UF = UNIONFIND(N)

for i in range(M):
    x,y = map(int,input().split())
    UF.union(x-1,y-1)

for i in range(N):
    if max < UF.size(i):
        max = UF.size(i)
    
print(max)


