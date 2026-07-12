student = { "name": "sahana", 
           "age": 20 ,
           "dream": "fitness coach"}
for key in student:
    print(key, ":", student[key])

student["location"] = "earth"
print(student)

student["age"]= 19
print(student)