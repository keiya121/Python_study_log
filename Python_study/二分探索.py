A,B,N = map(int,input().split())

def result(x):
    return A*int(x) + B*len(x)

high = 10**9
low = 0
mid = (high + low) //2

while 1 < high - low:
    mid_price = result(str(mid))
    if mid_price <= N:
        low = mid
    else:
        high = mid
    mid = (high + low) //2

print(low)

