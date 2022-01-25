# question 1
given ='Pythone is a case sensitive language'
print(len(given)) #part a
print(given[::-1]) #part b
print(given[11:-9]) # part c
print(given.replace('a case sensitive', 'object oriented')) #part d
print(given.index("a")) # part e
print(given.replace(" " , "" )) # part f

#question 2
Name =" ABC"
sid = "2110XXXX"
department_name = 'XYZ'
CGPA =9.9
temp = "Hey,{0} Here!\nMy SID is {1}\nI am from {2} department and my CGPA is {3} "
original = temp.format(Name,sid,department_name,CGPA)
print(original)

# question 3
a= 56
b= 10
print (a&b) #part a
print (a|b) #part b
print(a^b)  #part c
print(a<<2,b<<2) #part d
print(a>>2, b>>4) #part e

#question 4
print("enter the first number :")
num1 = int(input())
print("enter the second number :")
num2 = int(input())
print("enter the third number :")
num3 = int(input())
if (num1 >= num2) and (num1 >= num3):
 largest = num1
elif (num2 >= num1) and (num2 >= num3):
 greatest = num2
else:
 greatest = num3
print("The greatest number is :",greatest )

#question 5
print('enter your name:')
name1 =str(input())
names =['jack', 'bob', 'henry', 'petric','leon', 'ada','albert']
if name1 in names :
    print('yes')
else:
    print('no')    

       

#question 6
print("enter the first side of triangle :")
side1 =int(input())        
print("enter the second side of triangle :")
side2 =int(input())        
print("enter the third side of triangle :")        
side3 =int(input())        
if (side1>=side2+side3) or (side2>=side1+side3) or (side3>=side1+side2) :
    print("no")
else:
    print("yes")




    