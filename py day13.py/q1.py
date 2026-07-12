file = open("myfile.txt","w")
file.write("hello sahana")
file.close()

file= open("myfile.txt","r")
content = file.read()
print(content)
file.close()

file =open("myfile.txt","a")
file.write(" ,u r so good on working on python")
file.close()

file = open("myfile.txt","r")
content = file.read()
print(content)
file.close()