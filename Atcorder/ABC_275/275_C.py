Li = []
for i in range(9):
    Li.append(list(input()))
dot = []

for i in range(9):
    for j in range(9):
        if Li[i][j]=='#':
            dot.append([i+1,j+1])
print(dot)

def des(x,y):
    return(round((x**2+y**2)**(1/2)))

for i in range(len(dot)):
    dot[i] = des(*dot[i])
print(dot)




