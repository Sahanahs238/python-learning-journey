file = open("notes.txt","w")
file.write("This is my first note.\n")
file.close()

file = open("notes.txt","r")
content = file.read()
print(content)
file.close()

file=open("notes.txt","a")
file.write("i love python programming.\n")
file.close()

file = open("notes.txt","r")
content = file.read()
print(content)
file.close()

