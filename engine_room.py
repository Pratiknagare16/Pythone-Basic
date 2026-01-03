# ================================
# Python Basics – Pratik
# ================================

A = "Pratik"
print(A)
print(type(A))

NUM = 43
FNNUM = 56 - 45.56
val = True

print(NUM)
print(type(NUM))

print(FNNUM)
print(type(FNNUM))

print(val)
print(type(val))


# -------------------------------
# Strings
# -------------------------------

st = 'A for Apple'
sty = "B for Ball"

print(st)
print(sty)

stu = 'C for Cat\'s'
print(stu)

print("Length of sty")
print(len(sty))

print(sty[0])
print(sty[7])


text = "Todays Topic pythone Basic!"

print(text[2:8])
print(text[6:])
print(text[5:])


Ri = "one Piece is Real"

print(Ri.upper())
print(Ri.lower())
print(Ri.title())

print(Ri.count("e"))
print(Ri.find('o'))     # position
print(sty.find('Z'))   # not present

print(Ri.replace('Real', 'unreal'))

new_Ri = Ri.replace('Real', 'unreal')
print(Ri)
print(new_Ri)

fruit = 'applllllleeeeeee'
print(fruit.replace('e', 'E'))
print(fruit.replace('z', 'E'))


# -------------------------------
# Strip & Split
# -------------------------------

msg = '   Hello World    '
print(msg)
print(msg.strip())

print(len(msg))
print(len(msg.strip()))
print(msg.count(' '))

address = '106, tsunade St, leaf'
print(address.split(','))

test = 'how are you doing'
print(test.split(' '))


# -------------------------------
# String Concatenation
# -------------------------------

Namm = 'Pratik'
Last_Name = 'Nagare'

Name = Namm + " " + Last_Name
print(Name)


# -------------------------------
# Arithmetic Operations
# -------------------------------

num1 = 34
num2 = 67

print(num1, num2)
print(type(num1), type(num2))

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num2 / num1)

print(num2 // num1)
print(num2 % num1)
print(3 ** 2)


# -------------------------------
# Comparison Operators
# -------------------------------

print(A == A)
print(1 == 2)

print(3 != 2)
print(3 > 2)
print(3 < 2)
print(3 >= 3)
print(3 >= 2)
print(3 <= 2)


# -------------------------------
# Assignment Operators
# -------------------------------

num = 34
print(num)

num += 1
print(num)

num -= 5
print(num)

num = 10
num **= 3
print(num)


# -------------------------------
# Logical Operators
# -------------------------------

print(True and True)
print(True and False)
print(False and True)
print(False and False)

print(True or False)
print(False or False)

print(not True)
print(not False)


# -------------------------------
# Math Functions
# -------------------------------

print(abs(-2344))
print(round(45.44))
print(round(3.453666, 2))


# -------------------------------
# If Conditions
# -------------------------------

x = 4
y = 3
if x > y:
    print('yes, x is indeed greater than y')


x = 14
y = 13
if x > y:
    print('yes, x is indeed greater than y')
    print('I want to be part of if clause as well, so I have given 4 indents before print()')

print('this statement is not part of if clause')


if 4 > 5:
    print('four is greater than five')
else:
    print('four is smaller than five')


# -------------------------------
# Nested If
# -------------------------------

x = 56
if x > 59:
    print('x is greater than 59')
    if x > 69:
        print('x is greater than 69')
        if x > 80:
            print('x is greater than 80')
        else:
            print('x is smaller than 80')
    else:
        print('x is smaller than 69')
else:
    print('x is smaller than 59')

student = ['Nagare','Patil','Kulkarni','Patil','Pande']

print(student)

print(type(student))

student.append('Sharma')
print(student)


student.insert(2, 'More')
print(student)


student.remove('Patil')
print(student)
  
student.pop(1)
print(student)


student.reverse()
print(student)



fruits = [['mango','apple','pineapple'], ['sitafal', 'orange']]
print(fruits)
print(len(fruits))


student = ('Pratik','Devag','sankul' ,'Prathmesh','vedant')

print(student)
print(type(student))

print(student[1])

print(student.index('Pratik'))



new = ('#$%^ ',)
new1 = ('banaba',)
new2 = ('mango','orange')
print(new + new1 + new2)


num = [1, 2, 3, 4] 
new = tuple(num)

print(num)
print(new)

num = (1, 2, 3, 4, 5, 6, 7)
print(num[-1])
print(num[-2])




company = { "name": "Tesla", "founder": 'Elon Musk', "established": 2003}
print('Compny details')
print(company)
print("Data type")
print(type(company))
print("Name of the Company")
print(company['name'])

print("    ")

print("Total detail in company dic")
print(len(company)) 


print("   ")

print("after adding Adding location ")
company['location'] = 'US'
print(company)


new = dict({'name': 'Apple', 'year': 1975, 'founder': 'Steve Jobs and Steve Woniak'})   

print(new)
print(type(new))

for item in new:              
  print(item)

for item in new:             
  print(item, new[item])    

for item, val in new.items():
  print(item, val)

for xyz in new.values():
  print(xyz)  


  #set 



setbasic = {"apple", "banana", "cherry","watermelon","devil fruit"}    # random order 
print(setbasic)  

print(len(setbasic))




set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False}

print(set1)
print(set2)
print(set3)



set4 = {"355","Pratik", True, 20, "Superman"}
print(set4)

#function 

def hello():                    
    print('hello world')

hello()              # calling the hello function
hello()                  # reuseable

def hello (name):
   print(f'hello {name}')


hello('John')
hello(12)



def StudentInfo (details):
   print(f'hello{details}')

hello("Pratik Nagare")
hello(11)
hello('B')
hello("Computer Engineering")
print(type(hello))

def addthis(first, second):
  print(first + second)

print("Addition of 12 and 13")

addthis(12, 13) 


def subthis(first, second):
   print(first - second)

print("substraction of 12 and 13")

subthis(12, 13) 

def multiplication(first , second):
   print(first * second)   

print("Multiplication of 12 and 13")
multiplication(12, 13) 

def division(first , second):
   print(first / second)   

print("division of 12 and 13")
division(12, 13) 



def hello_you(name):
    return (f'hello {name.upper()}')
print(hello_you('Students'))

def add():  
    a = 35 
    b = 56  
    c = a+b  
    return c  

print("The sum is:", add())



'''

# calculator using input

def add(a,b):  
    return a+b; 
print("Enter the Numbers For the Addition")
a = int(input("Enter a: "))    
b = int(input("Enter b: "))    
    
print("Sum = ",add(a,b)) 


def sub(a,b):  
    return a-b; 
print("Enter the Numbers For the Substraction")
a = int(input("Enter a: "))   
b = int(input("Enter b: "))    
    
print("Substraction = ",sub(a,b)) 


def div(a,b):  
    return a/b; 
print("Enter the Numbers For the division")
a = int(input("Enter a: "))   
b = int(input("Enter b: "))    
    
print("division = ",div(a,b)) 


def Multi(a,b):  
    return a*b; 


print("Enter the Numbers For the Multiplication")
a = int(input("Enter a: "))    # will give error if you pass string here
b = int(input("Enter b: "))    
    
print("Multi = ",Multi(a,b)) 


'''


# interest rate  finding
 


print("Calculation for the interest rate")

p = int(input("Enter the principle amount? "))    
r = float(input("Enter the rate of interest? "))   
t = int(input("Enter the time in years? "))

def simple_interest(p,t,r):    
    return (p*t*r)/100    

  
print("Simple Interest: ",simple_interest(p,r,t)) 