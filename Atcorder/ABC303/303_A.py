N = int(input())
S = input()
T = input()

flag = 0

for i in range(N):
     a = S[i] == T[i]    
     b = (S[i] == '0' and T[i] == 'o')
     c = (S[i] == '1' and T[i] == 'l')
     d = (S[i] == 'o' and T[i] == '0')
     e = (S[i] == 'l' and T[i] == '1')

     if (a == False) and (b == False) and (c == False) and (d == False) and (e == False):
          flag = 1
          break
     
if flag == 0:
    print("Yes")
else:
     print("No")
          