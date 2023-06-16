N = int(input())

if(10**8<=N<=10**9-1):
    tmp = N//10**6
    print(int(tmp*10**6))
elif(10**7<=N<=10**8-1):
    tmp = N//10**5
    print(int(tmp*10**5))
elif(10**6<=N<=10**7-1):
    tmp = N//10**4
    print(int(tmp*10**4))
elif(10**5<=N<=10**6-1):
    tmp = N//10**3
    print(int(tmp*10**3))
elif(10**4<=N<=10**5-1):
    tmp = N//10**2
    print(int(tmp*10**2))
elif(10**3<=N<=10**4-1):
    tmp = N//10**1
    print(int(tmp*10))
else:
    print(N)