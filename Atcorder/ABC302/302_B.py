H,W = map(int,input().split())
S = [input() for i in range(H)]

print(S)


target_char = "s"

pos = [list((i,s.index(target_char))) for i,s in enumerate(S) if target_char in s]
print(pos)

for i in range(len(pos)):
    if S[i][pos[i][2]] == "n":                     #左にあるか
        print("aaa")
        break

