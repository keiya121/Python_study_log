A,B = map(int,input().split())

s_1 = [1,3,5,7]
s_2 = [2,3,6,7]
s_3 = [4,5,6,7]

ans = [1,1,1]

if A not in s_1 and B not in s_1:
    ans[0] = 0
if A not in s_2 and B not in s_2:
    ans[1] = 0
if A not in s_3 and B not in s_3:
    ans[2] = 0

ans = 1*ans[0] + 2*ans[1] + 4*ans[2]

print(ans)





