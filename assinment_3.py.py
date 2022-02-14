#question 1
str = input ('enter a string, ')
word = str.split()
count = {}
for  i in word:
    if i not in count.keys():
        count[i] =0
    count[i] = count[i] + 1
print(count)  # to find occurance of a word 

#question 2
year = int(input("enter the year :",))
month = int(input("enter the month :",))
date = int(input("enter the date :",))
if date<1 or date>31 or month<1 or month>12 or year<1800 or year>2025:
    print("wrong input")
else:
    if month in (1,3,5,7,8,10,12):
        if date ==31:
            date =1
            if month ==12:
                month=1
                year = year + 1
            else:
                month = month + 1
        else:
            date = date + 1
    elif month in (4,6,9,11):
        if date == 31:
            print('this month have 30 days\ninvalid date')
            exit()
        elif date ==30:
            date = 1
            month = month + 1
        else :
            date= date + 1
    else: # foe leap year
        if date<=29:
            if year%4==0:
                if date ==29:
                    date=1
                    month = month + 1
                else:date = date + 1
            else:
                if date ==29:
                    print("this is not a leap year")
                    exit()
                elif date == 28:
                    date = 1
                    month = month + 1
                else:
                     date = date + 1
    print("Next Date is :"+ str(date)+"/"+ str(month)+"/"+str(year)) # to find next date

# question 3
def square(list):
    sqr=[]
    for i in range(0, len(list)):
        a = [(list[i],list[i]**2)]
        sqr.append(a)
        i = i+ 1
    return sqr

lenght = int(input('Enter lenght of list:'))
list=[]
for i in range(0,lenght):
    element = int(input("Enter element of list :"))
    list.append(element)
    i = i + 1

print(square(list))

#question 4
print("enter your grade:")
grade = int(input())
if grade==10:
    print("your grade is 'A+' and Outstanding Performance")
elif grade==9:    
    print("your grade is 'A' and Exellent Performance")
elif grade==8:
    print("your grade is 'B+' and Very Good Performance")
elif grade==7:
    print("your grade is 'B' and Good Performance")
elif grade==6:
    print("your grade is 'C+' and Average Performance")
elif grade==5:
    print("your grade is 'C' and Below Average Performance")
elif grade==4:
    print("your grade is 'D' and Poor Performance")
else:
    print("Error")

# question 5
line = 6
for i in range(line):
    for j in range(i):
        print(' ',end='') # for printing spaces
    for j in range(2*(line-i)-1):
        print(chr(65 + j), end='') # for printing alphabet
        i = i+ 1
    print()

#question 6
dict1 = dict()
input1 = "Y"
while(input1=='Y'):
    name = str(input("enter name:"))
    sid = int(input("enter sid:"))
    dict1[sid]= name
    input1 = input("give Y to enter more sid in sictionary:")

print(dict1) # part A 

partb={k: v for k, v in sorted(dict1.items(), key=lambda item: item[1])} #part B
print(partb)

list1 = dict1.items()
sortedlist = sorted(list1)
print(sortedlist) #part c

entersid = int(input("Enter the SID : "))
print("The student with entered SID is")
print(dict1[entersid])  #part(d) 

#Question 7
term1 = int(input("Give a number-"))
term2 = int(input("Give a number-"))
sum = term1 + term2
series = [term1,term2]
n="y"
while(n=="y"):
    series.append(series[len(series)-1]+series[len(series)-2])
    print(series)
    n=input("Type y to continue and n to stop:")
print("The fibonacci series is")
print(series) 

#question 8
set1 = {1,2,3,4,5}
set2 = {2,4,6,8}
set3 = {1,5,9,13,17}

part1=set1.symmetric_difference(set2)
print(part1) #part a

part2 = set1^(set2^set3)
print(part2)#part b

part3 = (set1 & set2) | (set2 & set3) | (set3 & set1)
print(part3)#part c

new_set={1,2,3,4,5,6,7,8,9,10}
part4=new_set-set1 
print(part4) #part d

part5=new_set-(set1|set2|set3)
print(part5) #part e




        



     








