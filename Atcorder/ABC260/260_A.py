S = list(input())
ans = []

for i in S:
    num = S.count(i)
    if num == 1:
        ans.append(i)

if len(ans) == 0:
    print(-1)
else:
    print(ans[0])





