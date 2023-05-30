M_1 = 20
M_2 = 35
e = 11
d = 11
N = 60

def encry(M,e,N):
    C = (M**e) % N
    return C 

def decry(C,d,N):
    M = (C**d) % N
    return M

C_1 = encry(M_1,e,N)
ans_M1 = decry(C_1,d,N)

C_2 = encry(M_2,e,N)
ans_M2 = decry(C_2,d,N)

print(C_1,ans_M1)
print(C_2,ans_M2)