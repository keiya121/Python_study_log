A,B,C,D,E,F = map(int,input().split())

ans = ((A*B*C) - (D*E*F))%998244353
print(ans)