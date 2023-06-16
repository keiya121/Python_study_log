N = int(input())
li = []
ans = []
for _ in range(N):
    li.append(list(input().split()))
    li[_][1]=int(li[_][1])

L = sorted(li, key=lambda x: x[1])
a = li.index(L[0])

for i in range(N):
    i += a
    if(i >= N):
        i -= N
    print(li[i][0])