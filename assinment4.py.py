#question 1
def Towerofhanoi(n,Start,Extra,End):
    if n>0:
        Towerofhanoi(n-1,Start,End,Extra)
        print("Transfer disk from",Start,"to",End)
        Towerofhanoi(n-1,Extra,Start,End)
        
Towerofhanoi(3,"A","B","C")  

#question 2
# Pascal's triangle using iteration
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
# for making nCr function
def ncr(n,r):
    x=factorial(n)/(factorial(n-r)*factorial(r))
    return int(x)    

row=int(input("Enter the nunber of rows:"))
i=1
while i<=row:
    print(" "*(row-i),end="")
    j=0
    while j<i:
        print(ncr(i-1,j)," ",end="")
        j+=1
    print("\n")
    i+=1   

#question 3
#part a
def func(a,b):
    quotient=a//b
    remainder=a%b
    print("The quotient is",quotient)
    print("The remainder is",remainder)
    result=[quotient,remainder]
    return result

a=int(input("Enter your first number:"))
b=int(input("Enter your second number:"))
result=func(a,b)
print(result)
print("Callable:",callable(func))

#part b
print("a is zero:",a==0)
print("b is zero:",b==0)
print("quotient is zero:",result[0]==0)
print("remainder is zero:",result[1]==0)
if(a==0):
    print("a is zero")

#part c
list1=[]
for i in result:
    if i>4:
        list1.append(i)
print("The values greater than 4 are:",list1)

#part d
aset=set(list1)
print(aset)

#part e
immutable_set=frozenset(aset)
print("The required immutable set",immutable_set)

#part f
maxval=0
for i in immutable_set:
    if i>maxval:
        maxval=i
print("The required max value is:",maxval)
print("The required hash value is:",hash(maxval))

#question 4

class Student:
    def __init__(self,name,rollnumber):
        self.name=name
        self.rollnumber=rollnumber
    def __del__(self):
        print("Object has been destroyed")

obj1=Student("kuldeep singh",21104063)
print(obj1.name)
print(obj1.rollnumber) 
print("Object has been destroyed")

#question 5

class EmployeeDetails:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def func(self):
        print("Name of employee is:",self.name,"and salary is:",self.salary)

Emp1=EmployeeDetails("Mehak",40000)
Emp2=EmployeeDetails("Ashok",50000)
Emp3=EmployeeDetails("Viren",60000)
Emp1.func()
Emp2.func()
Emp3.func()

#part a
#updating salary of Mehak
Emp1.salary=70000
print("The updated salary of Mehak is:",Emp1.salary)

#part b
#deleting the record of Viren
del Emp3
print("The record of Viren has been deleted") 

#question 6
#using the concept of anagrams

def anagram(word):
    if len(word)==1:
        return [word]
    partial_words=anagram(word[1:])
    char=word[0]
    list1=[]
    for perm in partial_words:
        for i in range(len(perm)+1):
            list1.append(perm[:i]+char+perm[i:])
    return list1      


George_word=input("Enter the word by George:")
Possible_words=anagram(George_word)
Barbie_word=input("Enter word by Barbie:")
print("Possible Words are:",Possible_words)
print("If Barbie's word is present in the list , then their friendship is real.")

if Barbie_word in Possible_words:
    print("Their Friendship is real.")
else:
    print("Their Friendship is fake.")




