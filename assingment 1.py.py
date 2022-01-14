#question 1
a=int(input('number1 :'))
b=int(input('number2 :'))
c=int(input('number3 :')) 
average=(a+b+c)/3
print(average) 

#question 2
gross_income = int(input("enter the gross income: ")) 
dependent = int(input("enter dependent: "))
standard_deduction = 10000
dependent_deduction_amount = dependent * 3000
taxable_income = gross_income - standard_deduction 
tax = float((20/100) * (taxable_income)) - dependent_deduction_amount # tax is 20% of taxable_income
print("Your income tax : ", tax) 

#question 3
Student_Details = []
SID = int(input("enter your SID : "))
Name = str(input("enter Name : "))
Gender = str(input("enter Gender : "))
Course_Name = str(input("enter Course Name : "))
CGPA = float(input("enter your CGPA : "))
Student_Details.append(SID)
Student_Details.append(Name)
Student_Details.append(Gender)
Student_Details.append(Course_Name)
Student_Details.append(CGPA)
print("Student_Details : " , Student_Details ) 

#question 4
Marks1 = int(input("enter the marks of first student : "))
Marks2 = int(input("enter the marks of second student : "))
Marks3 = int(input("enter the marks of third student : "))
Marks4 = int(input("enter the marks of fourth student : "))
Marks5 = int(input("enter the marks of fifth student : "))
Marks = [Marks1,Marks2,Marks3,Marks4,Marks5]
Marks.sort()
print(Marks)

#question 5
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#part a
del color[3]
print("after deleting 4th item , new list is : ",color)
#part b
color = ['Red', 'Green','White', 'Black', 'Pink', 'Yellow']
color[3] = color[4]= 'Purple'
print("Answer for part B :",color[0:4]+color[5:1])
