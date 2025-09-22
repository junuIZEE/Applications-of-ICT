min=0
max=100
marks=int(input())
if min<= marks <=max:
    if marks >=90:
        print("A")
    elif marks>=75:
        print("B")
    elif marks>=60:
        print("C")
    elif marks>=50:
        print("D")
    else:
        print("F")
else:
        print("invalid Number")        