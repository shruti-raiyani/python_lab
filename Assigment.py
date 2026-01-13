Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print("hello world")
hello world

a = input("enter the value: ")
enter the value: 50
b= input("enter the value:")
enter the value: 50
sum= int(a)+int(b)
print (sum)
100

num= int (input("enter the value"))
enter the value 20

if(num%2==0):
    print("this number is even")
else:
    print("this number is odd")

    
this number is even

year=int(input("enter the year"))
enter the year 2005
if(year=%4==0 and year%100!=0):
    
SyntaxError: invalid syntax
year=int(input("enter the year"))
enter the year2005
if
SyntaxError: invalid syntax
year=int(input("enter the year"))
enter the year 2005
if(year %4==0 and year%100!=0):
    print("leap year")
else:
    print("not a leap year")

    
not a leap year

import math
print(math.pi)
3.141592653589793

print("the constant value of gravity is :",gravity)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    print("the constant value of gravity is :",gravity)
NameError: name 'gravity' is not defined
pi=3.14159
gravity=9.8
print("the constant value of gravtity is:",gravtity)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    print("the constant value of gravtity is:",gravtity)
NameError: name 'gravtity' is not defined. Did you mean: 'gravity'?

pi=3.14
gravity=9.8
print("the constant value of gravity",gravity)
the constant value of gravity 9.8

num=5
square=num**2
print(f"the square of {num} is {square}")
the square of 5 is 25

import math
def calculate_circle_area(radius):
    return math.pi*(radius**2)
r=7
SyntaxError: invalid syntax
print(f"area:{calculate_circle_area(r)}")
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    print(f"area:{calculate_circle_area(r)}")
NameError: name 'calculate_circle_area' is not defined
x=10
y=10.5
z="hello"
a=[1,2,3]
print(type(x))
<class 'int'>
print(type(y))
<class 'float'>
print(type(z))
<class 'str'>
print(type(a))
<class 'list'>

import math
print(math.cei(4.1))
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    print(math.cei(4.1))
AttributeError: module 'math' has no attribute 'cei'. Did you mean: 'ceil'?
import math
print(math.ceil(4.1))
5
print(math.floor(4.9))
4

print(pow(2,3))
8

num=float(input("Enter a number:"))
Enter a number:3
if num>0:
    print("the number is positive.")
    elif num < 0:
        
SyntaxError: invalid syntax
