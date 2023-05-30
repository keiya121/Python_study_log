H,W = map(int,input().split())
A = []
B = []
j = 0
count = 0

flag = 0
for _ in range(H):
    A.append(list(input()))
for _ in range(H):
    B.append(list(input()))

if A == B:
    flag = 1

if flag == 0:
    while(1):
        if(count<H):
            for i in range(H):
                A[i][j] = A[i][(j+1)%W]
                j += 1
        if A == B:
            flag = 1
            break
        else{
            for i 
        }

if flag == 0:
    print("No")
else:
    print("yes")