def palindrome():
    a=int(input("enter the number batiz:"))
    b=int(str(a)[::-1])
    if a==b:
        print("number is palidrome")
    else:
        print("number is not palidrome")    
palindrome()    