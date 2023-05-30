N = int(input())
S = list(input())

if N >= 2:
    if S.count("T") > S.count("A"):
        print("T")
    elif S.count("T") < S.count("A"):
        print("A")
    else:
        if S[N-1] == "T":
          print("A")
        elif S[N-1] == "A":
            print("T")
          
else:
    print(S[0])