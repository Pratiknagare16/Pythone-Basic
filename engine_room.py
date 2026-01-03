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




# interest rate  finding
 


print("Calculation for the interest rate")

p = int(input("Enter the principle amount? "))    
r = float(input("Enter the rate of interest? "))   
t = int(input("Enter the time in years? "))

def simple_interest(p,t,r):    
    return (p*t*r)/100    

  
print("Simple Interest: ",simple_interest(p,r,t)) 











#  If Else



# even odd


n = int(input(" Enter a number to check:"))

if n % 2 == 0:
  print("this is  even number.")
if n % 2 != 0:
  print("this is  an odd number.")
if n == 0:
  print("The number is neither even nor odd. Rather you entered Zero.")



# largest  number 

a = int(input("Enter the Value of a: "));  
b = int(input("Enter the Value of b: "));  
c = int(input("Enter the Value of c: "));  

if a>b and a>c:  
    print("a is largest input.");  
if b>a and b>c:  
    print("b is largest input.");  
if c>a and c>b:  
    print("c is largest input."); 

# marks check

marks = int(input("Enter the marks? "))  

if marks > 85 and marks <= 100:  
   print("Congrats ! you scored grade A ...")  
elif marks > 60 and marks <= 85:  
   print("You scored grade B + ...")  
elif marks > 40 and marks <= 60:  
   print("You scored grade B ...")  
elif (marks > 30 and marks <= 40):  
   print("You scored grade C ...")  
else:  
   print("Sorry you are fail !!") 

# loop in loop nested loop

print("Nested Loop Checking")

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")






# for LOOP


team_member = ['Pratik', 'Prathmesh', 'Vedant', 'devang','Shankul']

for members in team_member:
    print(members)




Name = 'Pratik Nagare'
for i in Name:
  print(i)




team_detail = {'name': 'GESCOE CODERS', 'Leader':'PANDE', 'Totol Members': 5, }

for item in team_detail:
    print(item, team_detail[item])


print('Loop for the count upto the 9')
for i in range(10):  
  print(i)

print('Loop for the print 0 t0 99')

for i in range(1,100):   
  print(i)



print("------ For the Continue ------- ")

adress = ['Nashik','Mumbai','Kolkata','Delhi','Karnataka','Pune','kedarnath','Kashmeer']

for location in adress:
    if location == 'Pune':
        continue
    print(location)


print("--------For the Break-------")

adress = ['Nashik','Mumbai','Kolkata','Delhi','Karnataka','Pune','kedarnath','Kashmeer']

for location in adress:
    if location == 'Pune':
        break 
    print(location)




# Squ of Number

num = [1, 2, 3, 4, 5, 6, 7 , 8 ,9 , 10]

def sqr(item):
  return item * item

for i in num:
  print(i, sqr(i))




  # mutiplication table by input


num = int(input("Enter the number "))  
for i in range(1,11):  
    c = num * i  
    print(f"{num} x {i} '    |    ' {c}")   



Subject  = ["math", "Coding", "Phy"] 
time = ["10 to 12 ", "12 to 2 ", "3 to 5"] 

for x in Subject:
  for y in time:
    print(x, y)





A = int(input("Enter the RollNO "))

nums = [1, 23, 32, 34, 36, 67, 69, 89, 99]  
count = 0;  
for item in nums:  
    count = count + 1
    if item == A :  
        print("Roll NO matched")  
        break
print("found at", count, "location")


#while loop
print("For the X")

x = 1
while x < 5:       
    print(x)
    x += 1      

print("For the Y")

y = 5
while y < 15:
    print(y)
    y += 1


print("for the X again with Break")

x = 1
while x < 10:
    if x == 4:
        break
    print(x)
    x += 1

print("for the Y again with break")

y = 5
while y < 15:
    if y == 9:
        break
    print(y)
    y += 1



while True:
    name = input('Input name: ')
    if name == 'stop':
        break
    elif name =='':
        break
    print("Your name is:", name)




i = 0  
str1 = 'One Piece Is related To Treasure'  
  
while i < len(str1):   
    if str1[i] == 't':   
        i += 1  
        break  
    print('Current Letter :', str1[i])   
    i += 1 


i = 0  
str2 = 'Ham saat saat hai is old film'  
  
while i < len(str2):   
    if str2[i] == 'o':   
        i += 1  
        break  
    print('Current Letter :', str2[i])   
    i += 1 