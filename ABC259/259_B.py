import math 
a,b,d = map(int,input().split())
rad = math.radians(d)

af_a = a*math.cos(rad) - b*math.sin(rad)
af_b = a*math.sin(rad) + b*math.cos(rad)

print(f'{af_a} {af_b}')