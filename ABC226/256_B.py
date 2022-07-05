N = int(input())
L = []

def return_int(x):
    return int(x)

for _ in range(N):
    A = input().split()
    L.append("".join(A))
    #print(L)

L = map(return_int,L)

print(L)

print(len(set(L)))