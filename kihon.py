""" print(0b11)
print(0o11)
print(0x11)

print(bin(17))
print(oct(17))
print(hex(17)) """

#tupleは変更不可

""" dic = {"Keiya":511,"Yuka":1211}
print(dic["Keiya"]) """

""" a = [1,2,5,3]
b =sorted(a)
print(b)#1,2,3,5
print(a)#1,2,5,3
a.sort()
print(a)#1,2,3,5 """

""" a = [4,5,6,7,8]
print(a[-3])
##########6########## """

""" a = 0b1110
a = a>>1
print(a) """


""" for i in range(8):
    for j in range(4):
        print("a",end="")
    print()   """    #end=""とすることで、横方向にprintできる。print()とすることで、jのループが終わった時点で改行。
                     #print()がないと、横に32個aと出力される。end=""がないとaが縦に来る。

""" a = [9,8,9,9]
for i in range(4):
    print(a[i],end = "")
    a[i]=str(a[i])
print()
print("".join(a)) """ #joinはendでかける

""" a = [1,"aaa","pika"]
del a[2]
print(a) """ #delは添え字で消す。

for i in range(5):
    print('{0:d} {1:4b}'.format(i,i+1))



