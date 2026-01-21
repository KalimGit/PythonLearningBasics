print("Hello World!")

x,y,z="Oranges","Grapes","Apples"
print(x,end= ' '); print(y);print(type(z));
x=y=z="Oranges"
print(x);print(y);print(z);

#Unpacking
fruits=["orange","Banana","Apple"]
x,y,z=fruits
print(x,end=' ');print(y,end=' ');print(z);

x="Python"; y="is"; Z="awesome";
print(x,y,z)
print(x+y+z)

x=5;y="John";
#print(x+y); #TypeError: unsupported operand type(s) for +: 'int' and 'str'

#Global scope keyword
def myfunc():
    global x
    x = "fantastic"
myfunc()
print("Python is ",x)

#List, Tuple
x= range(10)
print(x) #range(0,10)
print(list(x)) #0,1,2,...9

#Random number in python
import random
print(random.randrange(1,10))

#String are array of unicode characters
for x in "banana":
    print(x)
print(len("banana"))

#check if "free" present in sting
txt="The best things in life are free!"
print("free" in txt) #True. Can also be used with IF
print("joy" not in txt) #True. can also be used with IF

#String slicing
b="Hello, World!"
print(b[2:5]) #llo
print(b[:5]) #Hello
print(b[2:]) #llo, World!
print(b[-5:-2]) #orl
print(b.upper()); print(b.lower()); print(b.strip());
print(b.replace("H","J"))
print(b.split(","))

#combining str and int in variable(F-String)
age=36
txt = f"My name is John, I am {age}"
print(txt)

print(isinstance(x,int))

#Operators unique in python
print(12/5) #2.4
print(12//5) #2 .This operator is called floor division
#Chain comparison operator
x=5
print(1 < x < 10)
print(1 < x and x <10)

# is vs ==   ; Very important to note.Diff than Java.
x=[1,2,3]
y=[1,2,3]
print(x == y) #checks if values of both vairable equal
print(x is y) # checks if both variables point to same object in memory