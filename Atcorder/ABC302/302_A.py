A,B = map(int,input().split())

ans = A//B
if(A%B != 0):
    ans += 1

print(ans)

