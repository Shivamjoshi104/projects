def armstrong():
 a=int(input("enter the number :"))
 for x in range(1,10):
   for y in range(1,10):
      for z in range(1,10):
        if x**3+y**3+z**3==a:
         print("number is armgrastorm")
         return
 print("not")
armstrong()        
  
