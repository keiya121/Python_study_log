a = [10,29,7,5,2,9,18]
b = list(a)
a.sort()


right = len(a) - 1
left = 0
mid = (right+left)//2

def result(x):
    return a[x]

while 1 < (right - left):
    mid_value = result(mid)
    if mid_value < 9:
        left = mid
    else:
        right = mid
    mid = (right+left)//2
print(a)
print(b)
print(right)


    
