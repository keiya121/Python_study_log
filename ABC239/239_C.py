A = list(map(int,input().split()))
X = [A[0],A[2]]
Y = [A[1],A[3]]
P_X = [0,5,1,2,0,-5,-1,-2]
P_Y = [5,0,2,1,-5,0,-2,-1]
count = 0

for i in range(8):
    B = []
    for j in range(2):
        x = P_X[i] - X[j]
        y = P_Y[i] - Y[j]
        a = x//1
        b = y//1
        if x == a:
            B.append(a)
        if y == b:
            B.append(b)
    if len(B) == 4:
        count += 1
if count>=1:
    print('Yes')
else:
    print('No')

        
        

