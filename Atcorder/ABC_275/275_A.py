N = int(input())
A = list(map(int,input().split()))

a = max(A)
ans = A.index(a)
print(ans+1)