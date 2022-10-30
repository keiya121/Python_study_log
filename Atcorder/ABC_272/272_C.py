import itertools

N = int(input())
A = list(map(int,input().split()))
B = []

for pair in itertools.combinations(A,2):
    B.append(list(pair))

x = [sum(i) for i in B]

for i in x:
    if i % 2 == 0:
        B.append(i)
if len(B) >= 1:  
    print(max(B))
else:
    print(-1)





