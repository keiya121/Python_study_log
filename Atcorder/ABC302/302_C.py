N,M = map(int,input().split())
S = [input() for i in range(N)]
print(S)

totals = [sum(ord(char) for char in string) for string in S]

