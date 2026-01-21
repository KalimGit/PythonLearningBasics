print("Hello World!")

x,y,z="Oranges","Grapes","Apples"
print(x,end= ' '); print(y);print(type(z));
x=y=z="Oranges"
print(x);print(y);print(z);

#Unpacking
fruits=["orange","Banana","Apple"]
x,y,z=fruits
print(x,end=' ');print(y,end=' ');print(z);
x,*y=fruits
print(x);print(y) #displayed remaining items as list

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

#List is a collection of different datatypes which is ordered and changeable. Allows duplicate members.
thisList=["apple","banana","cherry"]
thisList[1:3] = ["watermelon"]
print(thisList) #apple,watermelon

thisList=["apple","banana","cherry"]
thisList.insert(2,"watermelon") #apple,banana,watermelon,cherry

thisList.remove("watermelon")#removes only first occurence

thisList.append("orange") #apple,banana,cherry,orange

thisList=["apple","banana","cherry"]
tropical=["mango","pineapple","papaya"]
thisList.extend(tropical)
print(thisList) # apple,banana,cherry,mango,pineapple,papaya

thisList.pop(1) #Remove specified index item or last item if not provided index value.

del thisList[0] #remove first item 
del thisList # Delete the entire list
#thisList.clear() #clears the list

thisList=["apple","banana","cherry"]
[print(x) for x in thisList] #loop using list comprehension

thisList.sort(reverse=True) #sort list in reverse
thisList.sort(key = str.lower) #case insensitive sort

newList = thisList.copy()
newList = list(thisList)
newList = thisList[:] #above 3 way to copy list

#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
thisTuple=("apple","banana","cherry")
thisTupel=("apple",) #one item tuple. must have comma.OW not a tuple.
#As tuple is unchangeable (ie., immutable) any insert,append has to done by convering it to list and then back to tuple.

del thisTuple #deltes the tuple entirely


#Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#Dictionary is a collection which is ordered** and changeable. No duplicate members.**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.