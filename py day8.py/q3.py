dreamm = open("dream.txt", "w")
dreamm.write("My dream is to become a fitness coach.\n")
dreamm.close()

dreamm = open("dream.txt", "r")
content = dreamm.read()
print(content)

feel = input("How do you feel about your dream? ")

dreamm=open("dream.txt","a")
dreamm.write(feel + "\n")
dreamm.close()