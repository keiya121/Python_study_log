N = int(input())

d = 998244353
a = abs(d-N)

if N<a:
    ans = a+2
else:
    ans = a


print(ans)

