N = int(input())
L = []
ind = []
max_n = 0
ans = []

def str_return(x):
    return str(x)

for i in range(N):
    L.append(list(map(int,input())))
    a = max(L[i])
    ind.append(L[i].index(a))
    if max_n < a:
        max_n = a

ans.append(max_n)

print(L)
print(max_n)
print(ind)
print("".join(map(str_return,ans)))



