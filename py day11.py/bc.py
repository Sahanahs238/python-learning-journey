import random
number=random.randint(1,18)
user = int(input("guess the integer"))
if number==user:
   print("correct guess")
else:
   print("try next time")