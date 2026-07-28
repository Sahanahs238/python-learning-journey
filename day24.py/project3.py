import random
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
length = int(input("enter the length of the password "))
password=""
sym = input("Do you want symbols? (yes/no): ")
if sym == "yes":
    characters+= "!@#$%^&"
    password+=random.choice(characters)
    print("your password is",password)
else:
    print(password)

for i in range(length):
    password+=random.choice(characters)
print("your password is",password)

