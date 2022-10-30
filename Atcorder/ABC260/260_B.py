N,X,Y,Z = map(int,input().split())
math = list(map(int,input().split()))
eng = list(map(int,input().split()))
total = []
ans = []
gokaku = []
for _ in range(N):
    total.append(math[_]+eng[_])
math_s = sorted(math,reverse=True)
eng_s = sorted(eng,reverse=True)

def ret(x):
    return str(x)

for _ in range(X):
    ans.append(math_s[_])
a = set(ans)

for _ in a:
    A = [i for i, x in enumerate(math) if x == _]
print(A)
print(gokaku)
print(ans)
