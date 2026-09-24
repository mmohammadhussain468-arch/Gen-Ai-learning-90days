#math module
#sqrt
import math
print(math.sqrt(68))

#power
import math
print(math.pow(4,8))

#round up
import math
print(math.ceil(4.8))

#round down
import math
print(math.floor(0.3))

#random module
import random
print(random.randint(1,100))

#random choice
import random
fruits=["app","ora","man"]
print(random.choice(fruits))

#random choice+list
import random
name=["huss","fat","sad"]
winner=random.choice(name)
print("winner:",winner)

#p1
import math
print(math.sqrt(86))

#p2
import math
print(math.pow(3,4))

#p3
import math
print(math.ceil(7.2))

#p4
import math
print(math.floor(7.2))

#p5
import random
print(random.randint(1,50))

#p6
import random
fruits = ["Apple", "Banana", "Mango", "Orange"]
print(random.choice(fruits))

#p7
import random
names = ["Hussain", "Arun", "Rahul", "Vijay"]
print(random.choice(names))

#p8
import math 
print(math.sqrt(86))

#p9
import math as m
print(m.sqrt(9))
print(m.floor(9.9))

#p10
import math

def square_root(n):
    return math.sqrt(n)

print(square_root(100))

#p11-minii program
import random

number = random.randint(1, 10)

guess = int(input("Enter num: "))

if guess == number:
    print("u won")
else:
    print("wrong guess")