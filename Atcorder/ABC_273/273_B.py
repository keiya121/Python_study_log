X,K = map(int,input().split())
X = str(X)
li = list(X)
key = 0

def return_int(x):
    return int(x)

def return_str(x):
    return str(x)

X = list(map(return_int,X))

for i in range(K):
    if len(X) >= 2:
        if X[(len(X) - (i+1))] >= 5:
            X[(len(X) - (i+1))] = 0
            X[len(X)-i-2] += 1
        else:
            X[(len(X) - (i+1))] = 0

        if X[len(X)-(i+1)] == 10:
            X[len(X)-(i+2)] += 1
            X[len(X)-(i+1)] = 0

        if X[0] == 10:
            key = 1
            X[0] = 0

if len(X) != 1:
    X = list(map(return_str,X))
    if key == 1:
        print("1" + "".join(X))
    else:
        print("".join(X))

else:
    if int(X[0])>=5:
        print(10)
    else:
        print(0)

