
sentence=(input("enter sentence")).lower()
alphabet=("qwertyuiopasdfghjklzxcvbnm")
sentence_set=set(sentence)
for x in alphabet:
    if x not in sentence_set:
      print("sentence not  pangram")
print("pangram ha")        
          