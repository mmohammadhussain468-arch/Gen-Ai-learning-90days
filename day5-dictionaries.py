student={"name":"hussain",
         "age":20,
         "dep":"ai&ds"}

print(student["age"])


#add item
car={"model":"m4",
     "yr":1991}
car["launch"]=1992
print(car)

#value change
car={"model":"m4",
     "yr":1991,
     "launch":1999}

car["launch"]=2000
print(car)

#remove item
student={"name":"vvv",
         "age":99,
         "cls":"A"}
student.pop("age")
print(student)

#dict length
student={"name":"uuu",
         "dep":"ooo",
         "sec":"B"}
print(len(student))

#check 
student={"name":"uuu",
         "dep":"ooo",
         "sec":"B"}
if "dep" in student:
    print("dep is available")

#Dictionary + for loop
student={"name":"hussain",
         "age":20,
         "dep":"ai&ds"}
for key in student:
    print(key)

#Keys + Values print
student={"name":"hussain",
         "age":20,
         "dep":"ai&ds"}
for key,value in student.items():
    print(key,value)

#p1
student={"name":"ccc"
         ,"age":90,
         "marks":20}
print(student)

#p2
student={"name":"ccc"
         ,"age":90,
         "marks":20}
print(student["name"])
print(student["age"])
print(student["marks"])

#p3
student={"name":"ccc"
         ,"age":90,
         "marks":20}
student["marks"]=95
print(student)

#p4
student={"name":"ccc"
         ,"age":90,
         "marks":20}
student["course"]="Agentic Ai"
print(student)

#p5
student={"name":"ccc"
         ,"age":90,
         "marks":20}
student.pop("age")
print(student)

#p6
student={"name":"ccc"
         ,"age":90,
         "marks":20}
print(len(student))

#p7
student={"name":"ccc"
         ,"age":90,
         "marks":20}
if "name" in student:
    print("name available")

#p8
student={"name":"ccc"
         ,"age":90,
         "marks":20}
for key in student:
    print(key)

#p9
student={"name":"ccc"
         ,"age":90,
         "marks":20}
for key,value in student.items():
    print(key,value)

#p10
student = {
    "name": "Hussain",
    "age": 21,
    "marks": 95,
    "course": "Agentic AI"
}
for key,values in student.items():
    print(key,values)