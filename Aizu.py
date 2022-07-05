
n = int(input())
S = list(map(int,input().split()))
q = int(input())
T = list(map(int,input().split()))
count = 0

for x in T:
    right = n
    left = 0
    while 1 < (right-left):
        mid = (right+left)//2
        if S[mid] <= x:
            left = mid
        else:
            right = mid
        #print(f'a{left} {mid} {right}')
        
    if S[left] == x:
        count += 1
    if S[right] == x:
        count += 1

print(count)
    

