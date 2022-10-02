N = int(input())
A = N//16
B = N%16

for _ in range(7):
    if A == 10 + _ :
        A = chr(65+_)
    if B == 10 + _ :
        B = chr(65+_)


li = []
li.append(str(A))
li.append(str(B))
print("".join(li))


