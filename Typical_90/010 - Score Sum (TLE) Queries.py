N = int(input())
C = []
L = []
ans = []
ans_1 = []
ans_11 = []
ans_2 = []
ans_22 = []
 
for i in range(N):
       C.append(list(map(int,input().split())))
Q = int(input())
for j in range(Q):
    L.append(list(map(int,input().split())))
    
#print(C)
#print(Q)
#print(L)
 
for m in range(Q):
    ans.append(C[L[m][0]-1:L[m][1]])
    for n in range(len(ans[m])):
        if ans[m][n][0] == 1:
            ans_1.append(ans[m][n][1])
        else:
            ans_2.append(ans[m][n][1])          
    ans_11.append(list(ans_1))
    ans_1 = []
    ans_22.append(list(ans_2))
    ans_2 = []
 
#print(ans_11)
#print(ans_22)
 
for t in range(len(ans_11)):
     print(str(sum(ans_11[t]))+" "+str(sum(ans_22[t])))