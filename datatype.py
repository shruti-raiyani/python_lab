Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x="hello world"
print(x);#str
hello world
x="20"
print(x);#int
20
x="20.5"
print(x); #float
20.5
x="1j"
print(x); #complex
1j
x=["orange","apple","banana"]
print(x); #list
['orange', 'apple', 'banana']
x=["orange","mango","apple"]
print(x);#tuple
['orange', 'mango', 'apple']
x="range(6)"
print(x); #range
range(6)
x={"name":"john","age":36}
print(x); #dict
{'name': 'john', 'age': 36}
x={"apple","mango","orange"}
print(x);#set
{'apple', 'orange', 'mango'}
x=frozenet( {"apple","banana","orange"})
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    x=frozenet( {"apple","banana","orange"})
NameError: name 'frozenet' is not defined. Did you mean: 'frozenset'?
x=frozenset({"apple","orange","banana"})
print(x) #frozenset
frozenset({'apple', 'orange', 'banana'})
x="True"
print(x); #bool
True
x=b"Hello"
print(x); #bytearray
b'Hello'
x=bytearray(5)
print(x); #bytearray
bytearray(b'\x00\x00\x00\x00\x00')
x=memoryview(bytes(5))
print(x); #memoryview
<memory at 0x00000245714A3D00>
x=None
print(x); #None
None
