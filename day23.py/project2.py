
import random
secret_number=random.randint(1,10)
attempts=0
while True:
    user_guess = int(input("enter your guess:"))
    attempts+=1;
    if(user_guess<secret_number):
        print("the number is smaller!")
        attempts+=1
    elif(user_guess>secret_number):
        print("the number is greater!")
        attempts += 1
    else:
        print("congragulations, you got itt!")
        print("you guessed within attemps",attempts)
        break
    
        
