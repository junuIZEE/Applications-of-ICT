while True:
    print('Which opertion would you like to perform? \n')
    print(" 1.....Addition\n 2.....Subtraction\n 3.....Multiplication\n 4.....Division\n" \
      " 5.....Even/Odd check\n 6.....Percentage Calculation\n 7.....Exit")
    z = int(input())
    if z==1:
        a = int(input("Input a\n"))
        b = int(input("Input b\n"))
        print(a+b)
    elif z==2:
        a = int(input("Input a\n"))
        b = int(input("Input b\n"))
        print(a-b)    
    elif z==3:
        a = int(input("Input a\n"))
        b = int(input("Input b\n"))
        print(a*b)    
    elif z==4:
        a = int(input("Input a\n"))
        b = int(input("Input b\n"))
        print(a/b)  
    elif z==5:
        a = int(input("Input Number\n"))
        if a%2 ==0 :
            print("Number is Even")
        else :
            print("Number is Odd")
    elif z==6:
        a = int(input("Input Number:\n"))
        b = int(input("As a percentage of:\n"))
        print("RESULT:");print(a/b*100 ," %")
    elif z==7:
        print("Bye lol\n")
        break
