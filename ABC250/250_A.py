#問題文
# 縦 H 行、横 W 列のマス目があり、このうち上から i 個目、左から j 個目のマスを (i,j) と呼びます。
#このとき、マス (R,C) に辺で隣接するマスの個数を求めてください。

#ただし、ある 2 つのマス (a,b),(c,d) が辺で隣接するとは、 ∣a−c∣+∣b−d∣=1 (∣x∣ を x の絶対値とする) であることを言います。

#入力は全て整数
#1≤R≤H≤10
#1≤C≤W≤10



H,N = map(int,input().split())
R,C = map(int,input().split())
count = 0
 
if H>=R and R>1:
    count += 1
if H>=R+1:
    count += 1
if N>=C and C>1:
    count += 1
if N>=C+1:
    count += 1
 
print(count)