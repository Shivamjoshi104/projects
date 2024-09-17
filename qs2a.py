def char():
 a=((input("enter string of length 1 batiz:")))
 vowel="aeiouAEIOU"
 if len(a)==1 :
      if a in vowel:
        print("true")
        return True
      else:
        print("False")
        return False 
 print("please enter the number of len 1")          

   
char() 

