N = int(input())
A = list(map(int,input().split()))
x = [1]
count = 1
li = [0,0,0]
for i in A:
    x.remove(i)
    li.append(i)
    x.append(2*count)
    x.append(2*count+1)
    count += 1

ameba_amount = max(x)

ans = [i+1 for i in range(ameba_amount)]

ans[0] = 0
ans[1] = 1
ans[2] = 1

for i in range(3,ameba_amount):
    ans[i] = li 

print(ans)




