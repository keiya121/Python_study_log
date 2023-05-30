N = input()
A = list(map(int,input().split()))

for i in A:
    for j in A[A.index(i)+1:]:
        ans = abs(j-i)
        print(ans)
