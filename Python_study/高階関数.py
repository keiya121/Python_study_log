from functools import reduce#reduceを使うときはfunctoolsからimport

A = [8,3,2,6,-4]

def twice(x):
    return(x*2)
def sr(x):
    return(str(x))

B = list(map(twice,A))
C = list(map(sr,B))#joinを使うために文字列に
print(" ".join(C))

def multiply(a,b):
    return a*b

D = reduce(multiply,A)#リストの各要素をかけ合わせる。
print(D)

def tasu1(x):
    return x+1

def san_baisu_hantei(x):
    return x % 3 == 0

print(san_baisu_hantei(6)) #TrueかFalse

map_object_E = map(tasu1,A)
E = list(filter(san_baisu_hantei,map_object_E))#第2引数には、mapオブジェクトやfilterオブジェクトもとれる。
                                               #Aの各要素に１を足したものが３の倍数かフィルタリング。
E_2 = list(map(sr,E))
print("　".join(E_2))