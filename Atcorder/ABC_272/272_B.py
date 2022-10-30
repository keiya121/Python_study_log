import itertools

N,M = map(int,input().split())
K = []
x = []
y = []
a = []
b = []
ans = "Yes"

li = [i+1 for i in range(N)]
for pair in itertools.combinations(li,2):
    x.append(list(pair))
for i in range(M):
    K.append(list(map(int,input().split())))

for i in range(M):
    if K[i][0] == N:
        break
    else:
        for pair in itertools.combinations(K[i][1:],2):
            y.append(list(pair))
            key = 1
if key == 1:
    for i in range(M):
        for j in range(M):
          if y[i] not in x[j]:
            ans = "No"
            break

print(ans)
