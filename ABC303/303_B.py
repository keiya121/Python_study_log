N,M = map(int,input().split())
li = []
L = [[False]*N for _ in range(N)]#Falseで表を埋める。
ans = 0

for _ in range(M):
    li.append(list(map(int,input().split())))

for i in range(M):
    for j in range(N-1):
        cow = li[i][j]-1
        row = li[i][j+1]-1
        L[cow][row] = True

for i in range(N):
    for j in range(i+1,N):
        if (L[i][j] == False) and (L[j][i] == False):
            ans += 1

print(ans)
print(L)


