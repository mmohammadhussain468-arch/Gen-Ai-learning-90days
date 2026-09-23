#add
def add(a,b):
    print(a+b)
add(0,9)
add(0,1)

#sub
def sub(a,b):
    print(a-b)
sub(9,7)
sub(1,0)

#p1
def hello():
    print("hello bro")
hello()
#p2
def greet(name):
    print("Hello",name)
greet("hussain")

#p3
def add(a,b):
    print(a+b)
add(20,30)
add(10,15)

#p4
def mul(c,d):
    print(c*d)
mul(3,3)
mul(0,0)

#p5
def sub(g,p):
    print(g-p)
sub(0,0)
sub(7,2)

#p6
def square(n):
   return n*n
print(square(5))

#p7
def check_num(n):
    if n >=0:
        print("positive")
    else:
        print("negative")

check_num(8)

#p8
def check_age(age):
    if age>=18:
        print("adult")
    else:
        print("minor")
check_age(20)

#p9
def greet(name="bro"):
    print("hello",name)
greet()

#p10
def student(name,marks):
    print("Name:",name)
    print("marks:",marks)
student("bro",95)