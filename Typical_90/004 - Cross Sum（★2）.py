H,W = map(int,input().split())
A = []
B = []
X = []
Y = []
Z_li = []
Z = []

for l in range(H):
  A.append(list(map(int,input().split()))) #listの中にlist

for i in range(W):          #列の和をそれぞれ計算
  for j in range(H):
    B.append(A[j][i])
  x = sum(B)
  X.append(x)
  B = []

for m in range(H):          #行の和をそれぞれ計算
    y = sum(A[m])
    Y.append(y) 

#print(X)
#print(Y)

for p in range(H):
    for q in range(W):
        z = X[q] + Y[p] - A[p][q] #２回分足してるところを引く
        Z_li.append(z)
    Z.append(Z_li)
    Z_li = []

#print(Z)

for k in range(H):
    Z[k] = [str(s) for s in Z[k]] #joinはint型には使えないので、文字列型に変換
    print(' '.join(Z[k]))
