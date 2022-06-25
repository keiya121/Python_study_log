N  = int(input())
li = []
s = set()


for _ in range(N):
    li.append(input())

for i in li:
    a = len(s)
    s.add(i)
    b = len(s)
    if a != b:
        print(li.index(i) + 1)





