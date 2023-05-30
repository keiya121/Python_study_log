N = int(input())
S = list(map(int, input().split()))

pos = 0

while True:

    flag = True

    for i in range(len(S) - 1):
        if abs(S[pos + abs(S[pos] - S[pos + 1]) - 1] - S[pos + abs(S[pos] - S[pos + 1]) - 1 + 1]) != 1:
            flag = False
            pos = i
            break

    if flag == True:
        break

    if S[pos] > S[pos + 1]:
        for x in range(abs(S[pos] - S[pos + 1]) - 1):
            S.insert(pos + 1, S[pos] - x)

    if S[pos] < S[pos + 1]:
        for y in range(abs(S[pos] - S[pos + 1]) - 1):
            S.insert(pos + 2, S[pos] + y + 1)

print(S)