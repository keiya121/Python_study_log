N = input()
l = len(N)

dx = 0
dy = 0

if(l == 2):
    if 3<=int(N[1])<5:
        dx = 5
    elif 5<=int(N[1])<=7:
        dx = -5
    print(round(int(N),-1)+dx)
elif(l==1):
    if 3<=int(N)<5:
        dy = 5
    elif 5<=int(N)<=7:
        dy = -5
    print(round(int(N),-1)+dy)
else:
    print(N)
