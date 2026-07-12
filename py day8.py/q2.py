file2 = open("myname.txt","w")
file2.write("My name is Sahana.\n")
file2.close()

file2 = open("myname.txt","r")
content = file2.read()
print(content)
file2.close()

file2=open("myname.txt","a")
file2.write("I want to become a Software Engineer.")
file2.close()

file2 = open("myname.txt","r")
content = file2.read()
print(content)
file2.close()