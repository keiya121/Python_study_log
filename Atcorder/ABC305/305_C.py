H,W = map(int,input().split())
S = [["." for _ in range(W+2)]]

for i in range(H):
    S.append(list("."+input()+"."))
S.append(["." for _ in range(W+2)])

for i in range(1,H+1):
    for j in range(1,W+1):
        point = 0
        if S[i][j] == ".":
            if S[i+1][j] == "#":
                point += 1
            if S[i-1][j] == "#":
                point += 1
            if S[i][j+1] == "#":
                point += 1
            if S[i][j-1] == "#":
                point += 1
            if point >= 2:
                print(i,j)
                exit()
            
