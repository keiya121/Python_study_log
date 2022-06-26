# https://atcoder.jp/contests/abc146/tasks/abc146_c 問題


A,B,N = map(int,input().split())

def result(x):
    return A*int(x) + B*len(x)

high = 10**9
low = 0
mid = (high + low) //2

while 1 < high - low:  # highとlow の差分が1より大きい間　境目を見つける。
    mid_price = result(str(mid))
    if mid_price <= N:
        low = mid
    else:
        high = mid
    mid = (high + low) //2

print(low)

