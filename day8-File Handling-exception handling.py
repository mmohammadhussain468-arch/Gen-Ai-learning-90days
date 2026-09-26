#FileHandling
#write
with open("name.txt", "w") as file:
    file.write("Hello Bro")

#read
with open("name.txt", "r") as file:
    print(file.read())

#append
with open("name.txt", "a") as file:
    file.write("\nWelcome to AI")

#Exception Handling
#try + except
try:
    num=int(input("num:"))
    print(num)
except:
    print("invalid")
#Specific Error
try:
    p=int(input("enter num:"))
except ValueError:
    print("pls enter num")

#Division Error
try:
    a=10
    b=0

    print(a/b)
except ZeroDivisionError:
    print("can't divisible by zero")

#Multiple Exceptions
try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))

    print(a / b)

except ValueError:
    print("Enter numbers only")

except ZeroDivisionError:
    print("Cannot divide by zero")


#else
try:
    num = int(input("Enter number: "))

except ValueError:
    print("Invalid number")

else:
    print("You entered:", num)

#finally
try:
    num = int(input("Enter number: "))
    print(num)

except ValueError:
    print("Invalid input")

finally:
    print("Program finished")


#p1
with open("name.txt","w") as file:
    file.write("Hello Python")

#p2
with open("name.txt","r") as file:
    jt=(file.read())
    print(jt)

#p3
with open("name.txt","a") as file:
    file.write("\nGenAI")
    

#p4
with open("name.txt","a") as file:
    file.write("\nGenAI")
    file.write("\nPython")
    file.write("\nAgentic AI")
with open("name.txt", "r") as file:
    print(file.read())

#p5
with open("name.txt","w") as file:
    i=input("enter ur name:")
    file.write(i)

#p6
try:
    j=int(input("Enter number:"))
    print("okk")
except:
    print("invalid number")

#p7
try:
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    print(a/b)
except ZeroDivisionError:
    print("Cannot divide by zero")

#p8
try:
    p=int(input("Enter a num:"))
    print("Valid number")
except:
    print("invalid num:")
else:
    print("valid num")

#p9
try:
    p=int(input("Enter a num:"))
    print("Valid number")
except:
    print("pls enter num:")
finally:
    print("pg finished")

#p10
with open("name.txt","w") as file:
    name=int(input("Enter ur name:"))
    age=int(input("Enter ur age:"))
    course=int(input("Enter ur course:"))

with open("name.txt","w") as file:
    print(file.read())
