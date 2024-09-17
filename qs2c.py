#to made a histogram [4,9,7]
a=list(input("enter the number"))
if len(a)<=3:
    for x in a:
        c=int(x)
        print("*"*c,a)