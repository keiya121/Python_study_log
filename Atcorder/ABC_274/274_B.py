H,W = map(int,input().split())
C = []
tmp = []
C_2 = []
ans = []
for _ in range(H):
    C.append(list(input()))

for i in range(W):
    for j in range(H):
      tmp.append(C[j][i])
    C_2.append(list(tmp))
    tmp = []

for _ in range(W):
    ans.append(str(C_2[_].count("#")))

print(" ".join(ans))

