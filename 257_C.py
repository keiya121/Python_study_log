N = int(input())
S = int(input())
W = list(map(int,input().split()))
W.sort()
X = 55

right = N-1
left = 0
mid = (right + left)//2

def w_cul(x):
    return W[x]

while (right-left) > 1:
    if w_cul(mid) <= X:
        left = mid
    else:
        right = mid
    mid = (right + left)//2

judged_num = N - right
print(judged_num)


    




