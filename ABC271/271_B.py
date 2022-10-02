N,Q = map(int,input().split())
Li = []
li = []
for _ in range(N):
    A = list(map(int,(input().split())))
    Li.append(A)
for _ in range(Q):
    B = list(map(int,(input().split())))
    li.append(B)

#print(Li)
#print(li)



for i in range(Q):
    print(Li[li[i][0]-1][li[i][1]])