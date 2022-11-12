N = int(input())
S_1 = [list(input()) for i in range(N)]
S = [S_1[j][0] + S_1[j][1] for j in range(N)]
key = 0
A = ["H","D","C","S"]
B = ["A","2","3","4","5","6","7","8","9","T","J","Q","K"]

for _ in range(N):
    if S_1[_][0] not in A:
        key = 1
        break 
    if S_1[_][1] not in B:
        key = 1
        break
    if S.count(S_1[_][0] + S_1[_][1]) >= 2:
        key = 1
        break

if key == 1:
    print("No")
else:
    print("Yes")

