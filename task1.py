Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:01:55) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> p=float(input("enter principal amount:"))
enter principal amount:2
>>> r=float(input("enter rate of interest:"))
enter rate of interest:5
>>> t=float(input("enter time(in year):"))
enter time(in year):6
>>> si=(p*r*t)/100
>>> print("simple interest=",si)
simple interest= 0.6
>>> 
>>> a=int(input("enter first number:"))
enter first number:8
>>> b=int(input("enter second number:"))
enter second number:9
>>> print("maximum number is:",max(a,b))
maximum number is: 9
>>> 
>>> for i in range(1,6)
SyntaxError: invalid syntax
>>> for i in range(1,6):
    print(i)

    
1
2
3
4
5
>>> text=input("enter a string:")
enter a string: 4
>>> length=len(text)
>>> print("length of the string=",length)
length of the string= 2
>>> 
>>> print("welcome to python programming!")
welcome to python programming!
>>> text=input("enter a string:")
enter a string:6
>>> print("first charcter is :",text[0])
first charcter is : 6
>>> 
>>> text=input("enter a string:")
enter a string:6
>>> print("last charcter is:",text[-1])
last charcter is: 6
>>> 
>>> num=int(input("enter a number:"))
enter a number:7
>>> if num>0:
	print("number is positive")
	else:
		
SyntaxError: invalid syntax
>>> elif num<0
SyntaxError: invalid syntax
>>> elif num<o:
	
SyntaxError: invalid syntax
>>> num=int(input("enter a number: "))
enter a number: 23
>>> if num>0:
	print("number is positive")
elif num<0:
	print("number is negative")
else:
	print("number is zero")

	
number is positive
>>> 
>>> a=int(input("enter first number:"))
enter first number:6
>>> b=int(input("enter second number:"))
enter second number:8
>>> c=int(input("enter third number:"))
enter third number:9
>>> sum=a+b+c
>>> print("sum of three numbers=",sum)
sum of three numbers= 23
>>> 
>>> name=input("enter your name:")
enter your name:shruti
>>> print("hello",name)
hello shruti
>>> 