N,W = map(int,input().split())
li = []
val = []
weight = []

for _ in range(N):
    li.append(input().split())
    val.append(int(li[_][0]))
    weight.append(int(li[_][1]))

#print(val)
#print(weight)

dp = [[0 for _ in range(W+1)] for _ in range(N+1)]

for i in range(N):
    for j in range(W+1):
        if weight[i] <= j:
            dp[i+1][j] = max(dp[i][j-weight[i]] + val[i],dp[i][j])
        else:
            dp[i+1][j] = dp[i][j]

print(dp[-1][-1])

