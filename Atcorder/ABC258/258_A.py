K = int(input())
A = ["21","00"]

A[1] = int(A[1]) + K

if int(A[1]) >= 60:
    A[1] = K%60
    A[0] = int(A[0]) + K//60
if 0 <= int(A[1]) < 10:
        A[1] = str(A[1]).zfill(2)


def str_return(x):
    return str(x)

print(":".join(map(str_return,A)))