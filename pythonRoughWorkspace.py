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


#Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.*But can add and remove item.
thisSet={"apple","banana","cherry"}
print(thisSet)

thisSet.add("Orange")
tropical={"pineapple","mango"}
thisSet.update(tropical) # values in both sets are appended

thisSet.remove("banana") #If item not present, then throws error. To avoid this, use discard()
thisSet.discard("jj")
thisSet.clear()
del thisSet #If printing after del will raise error as not defined.same behavior for List too.
#common operations in Set
#set1.union(set2); set1.union(set2,set3) - Used to combine two sets
#set1 | set2 | set3 - Used to combine set with set or set with list and so on.
#set3 = set1.intersection(set2) - find common item between sets and return
#set1.intersection_update(set2) - find common and update the existin set1. Do not return new set.
#set3 = set1.difference(set2) - find items present in set1 and not in set2
#set1.difference_update(set2)
#set1.symmetric_difference(set2) - find items not present in both sets. Use also like set1 ^ set2.

set1 = frozenset({"apple","banana","orange"}) #like immutable set.


#Dictionary is a collection which is ordered** and changeable. No duplicate members.**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
thisDict={"brand":"Ford","model":"Mustang","Year":1975,"Year":2000}
thisDict["model"]  
thisDict.get("model")
thisDict.keys() #dict_keys(['brand', 'model', 'year'])
thisDict.values() #dict_values(['Ford', 'Mustang', 1964])

if(5>2): pass

for x in range(6):
    print(x)
else:
    print("Finally Finished!") #else won't execute if break is used to stop the loop

#Function Decorator
def changecase(func):
  def myinner(x):
    return func(x).upper()
  return myinner

@changecase
#@addgreeting  #the decoarator are called in reverse order starting from the one close to function
def myfunction(nam):
  return "Hello " + nam

print(myfunction("John"))    

#functools.wraps - to preserve original function name and doc
import functools
def changecas(func):
    @functools.wraps(func)
    def myinner():
        return func().upper()
    return myinner
@changecas
def myfunction():
    print("Hello,Kaleem")

#Python Lambda
#can have any number of arguments but only one expression
x = lambda a,b,c:a+b+c
print(x(5,2,2)) #9
#Lambda with map, filter and sorted
numbers=[1,2,3,4,5]
doubled=list(map(lambda x: x*2,numbers)) #
print(doubled) #[2,4,6,8,10]
oddnumbers=list(filter(lambda x:x%2!=0, numbers))
print(oddnumbers) #[1,3,5]
items=("ape","scooter","Jeep")
sorteditems=sorted(items,key=lambda x:len(x)) # sort by length
print(sorteditems)

import datetime
x = datetime.datetime.now()
print(x)
y = datetime.datetime(2025,8,26)
print(y.year)
print(y.strftime("%A"))
print(y.strftime("%a"))
print(y.strftime("%B"))
print(y.strftime("%b"))

import json
jsonInput = '{"name":"Kaleem","gender":"male"}'
parsedJson = json.loads(jsonInput) #to convert json to python object (ie., dictonary)
print(parsedJson)
jsonOutput = json.dumps(parsedJson) #to convert python dict to json
print(jsonOutput)

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# sort the result alphabetically by keys:
print(json.dumps(parsedJson, indent=4, sort_keys=True))

import re #for regex. refer more examples
#   pip install <packageName>
try:
  print("Hello")
  raise TypeError("Only Integers are allowed")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
finally:
  print("finally block")

#String formatting using f-string
txt = f'This is {52:.2f} inches'
print(txt)

#OOPS
class Vehicle:
  t="Vehicle"
  def __init__(self,name,model):
    self.name = name
    self.__model = model #Private instance property
  def printCarDetail(self):
    print(f'The {self.t} name is {self.name}.Model - {self.__model}')
c = Vehicle("Corolla","1995")
c.printCarDetail()