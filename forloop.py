Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:01:55) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for i in range (1,6):
	print(i)

	
1
2
3
4
5
>>> for i in range(3):
	print("hello")

	
hello
hello
hello
>>> for in range (1,11):
	
SyntaxError: invalid syntax
>>> for i in range (1,11):
	print(i)

	
1
2
3
4
5
6
7
8
9
10
>>> for i in range (1,21)
SyntaxError: invalid syntax
>>> for i in range (1,21):
	if i % 2 ==0
	
SyntaxError: invalid syntax
>>> for i in range (1,21):
	if i % 2 ==0:
		print(i)

		
2
4
6
8
10
12
14
16
18
20
>>> for i in range (1,16):
	if i % 2 !=0:
		print(i)

		
1
3
5
7
9
11
13
15
>>> for i in range (1,11):
	print("s x",i,"=",5*i)

	
s x 1 = 5
s x 2 = 10
s x 3 = 15
s x 4 = 20
s x 5 = 25
s x 6 = 30
s x 7 = 35
s x 8 = 40
s x 9 = 45
s x 10 = 50
>>> 
>>> name="atmiya"
>>> name="atmiya"
>>> for letter in name:
	print(letter)

	
a
t
m
i
y
a
>>> total=0
>>> for i in range(1,6):
	total=total+1
	print("sum is:",total)

	
sum is: 1
sum is: 2
sum is: 3
sum is: 4
sum is: 5
>>> numbers=(10,20,30,40)
>>> for i in numbers:
	print(n)

	
Traceback (most recent call last):
  File "<pyshell#38>", line 2, in <module>
    print(n)
NameError: name 'n' is not defined
>>> numbers(10,20,30,40)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    numbers(10,20,30,40)
TypeError: 'tuple' object is not callable
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> numbers=(10,20,30,40)
>>> for i in numbers:
	print(number)

	
Traceback (most recent call last):
  File "<pyshell#43>", line 2, in <module>
    print(number)
NameError: name 'number' is not defined
>>> numbers=[10,20,30,40]
>>> for n in numbers:
	print(n)

	
10
20
30
40
>>> 