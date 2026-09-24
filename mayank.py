# ### chapert=1
# # in this if yo want to run thios uou have to cooment out other code

# print ("hello world")

# # print sum function
# a=2
# b=5
# sum=(a+b)
# print(sum)

# # expresion execution 
# # 1. string and numeric value can operate togetrher with "*" repeat 
# a,b=2,3
# txt="@"
# print(a*b*txt)

# # string and tring can operate with "+" (concatination)
# a,b="2",3
# c="@"
# print ((a+c)*b)

# # numeric values can operate with all arthematic operaters
# a,b=2,3 
# c=4
# print(a+b*c)

# # arthematic expresion with integers and float wil result in float 
# a,b=10,5.0 
# c=a*b
# print(c)
       
# # result of two devision operators with two integers will be float
# a,b=1,2 
# c=a/b
# print(c)

# # integer division with float and int will give int displayed as float-->"//"
# a,b=1.5,3
# c=a//b
# print (c,a/b)

# # remainder is negitive when denomnaor is negitive
# a,b=-5,2
# c=a%b
# print(c)

# a,b=5,2
# c=a%b
# print(c)

# a,b=5,-2
# c=a%b
# print(c)

# # comment in python 
# # sinle line comment 
# """this 
# in multi line
#  comment"""

# # type conversion 
# # data type (value)
# a=float("123")
# print(type(a)) 

# # input in python
# a=input("what is your name:",)
# print ("welcome",a)

# #insert the sides of a square and then get its area -+
# a=float(input("sides of a square" ))
# b=2

# print (a*a)

# # to get input of two no and print their sum 
# a=int(input("first number:"))
# b=int(input("second number:"))

# sum=(a+b)
# print(sum) 

# # to find the average of two no.
# a=float(input("first number :"))
# b=float(input("second number :"))

# average=(a+b)/2
# print(average)

# # program to print if no. a is greater than or equal to b 
# a=int(input("first no."))
# b=int(input("second no."))
 
# print(a>=b)

# ### ch=2

# # find the length of users first name 
# a=input("first name :")
# print("length of your name :",len(a))

#  # slicing
# str="mayank"
# print(str[1:4])

# # negetive indexing
# str="apple"
# print(str[-3:-1])

# # string functions

# string="my name is mayank"

# # first function to confirm that your words ends with the word that you end 

# a=string.endswith("ank")
# print(a)

# # second function to capitalize first letter of a string
# a=string.capitalize()
# print(a)

# # third function to replace all occurance of old
# a=string.replace("mayank" , "jayant")
# print(a )

# #fourth function this is usde to find a particular word in the string "in the outpout you will get the index of the first letter of that word"  
# a=string.find("mayank")
# print(a)

# # fifth function count is the occurance of substring
# a=string.count("m")
# print(a)

# # find the signs of doller in a string
# a=input("what is your word :")
# print(a.count("$"))

# #  if statement  
# age=21
# if(age>=18): 
#     print("can vote")
#     print("can drive")
# # elif and ele statement

# light="green"
# if (light=="red"):
#     print("stop")
# elif(light=="green"):
#     print("go")
# elif(light=="yellow"):
#     print("look")

# else:
#     print("dont go ")
# print("light is broken")


# # program to give grade according to their marks
# a=int(input("marks:"))

# if(a >= 90):
#     print("grade=A")
# elif(a>=80 and a<90):
#     print("grade=B")
# elif(a>=70 and a<80):
#     print("grade=C")
# elif(a>=60 and a<70):
#     print("grade=D")
# else:
#     print("tera baccha fail hai teri tara")
# # to get to knoe abou that if you can drive or not 
# age=32

# if (age>=18):
#     if(age>=80):
#         print("cannot drive")
#     else:
#         print("can drive")
# else:
#     print("cannot drive")


# #  a program to find that a no entered is odd or even "we kow tthat no which is multiple of 2 divinding gives remender =2 so use modulo "
# a=int(input("the no. :"))
# if(a%2==0):
#     print("no. is even")
# else:
#     print("no. is odd")    
 
# #to find that which no. is the greatest no. out of the given three numbers's  
# a=int(input("first no"))
# b=int(input("second no"))
# c=int(input("third no"))
# if(a>b and a>c):
#     print("greater no. is:",a)   
# elif(b>a and b>c):
#     print("greater no. is:",b)
# elif(c>a and c>b):
#     print("greater no. is:",c)

# #to find that which no. is the greatest no. out of the given four numbers's  
# a=int(input("first no"))
# b=int(input("second no"))
# c=int(input("third no"))
# d=int(input("fourth no"))

# if(a>b and a>c and a>d):
#     print("the greatest no. is:",a)     
# if(b>a and b>c and b>d):
#     print("the greatest no. is:",b)   
# if(c>a and c>b and c>d):
#     print("the greatest no. is:",c)   
# if(d>a and d>b and d>c):
#     print("the greatest no. is:",d)       

# # which no. is the multple of 7
# a=int(input("write the number:"))
# if(a%7==0):
#     print(a,"is the multiple of 7")
# else:
#     print("this is not the multiple of 7")    



# ### ch=3
# # lists allow to assign value to any index 
# student=["karan",65.15,"delhi"]
# student[0]="mayank"
# print(student[0])

# # list slicing
# marks=[12,16,98,65,52]
# print(marks[1:5])

# # list methods 

# # input of your three favourit movie and stor them in a list
# movies=[]
# a=str(input("write your first fvourite movie"))
# b=str(input("write your second fvourite movie"))
# c=str(input("write your third fvourite movie"))
# movies.append(a)
# movies.append(b)
# movies.append(c)
# print(movies)

# """ a program to check if the list is a pelendrom 
# (pelendrom means if we pronounce from start it will pronounce same and if we pronounce backword it will also sound same)"""

# list=[]
# a=input("firt")
# b=input("second")
# c=input("third")
# d=input("fourth")
# list.append(a)
# list.append(b)
# list.append(c)
# list.append(d)
# copy1=list.copy()
# copy1.reverse()
# if(list==copy1):
#     print ("list is a pelendron")
# else:
#     print("no a pelendrom")


# # program to count the no. of students with thwe a grade in the touple
# tup=("c","d","a","a","b","b","a")
# a=tup.count("a")
# print(a)


# # to input values in a list and sout them a to d
# list=["c","d","a","a","b","b","a"]
# list.sort()
# print(list)


# ### ch=4

# #dictionary in python 

# info={
#     "name" : "appnacollege",
#     "subjects" : ["python","c","java"],
#     "topics" : ("dict","set"),
#     "age" : 35,
#     "is_adult" : True
# }

# print(info)
# print(type(info))


# # print any key of dictioary 

# info={
#     "name" : "appnacollege",
#     "subjects" : ["python","c","java"],
#     "topics" : ("dict","set"),
#     "age" : 35,
#     "is_adult" : True
# }
# info["name"]="mayank" #over write 
# info["surname"]="khapra" #made new key and assign a new value to it in dictionary
# print("surname")
# print("topics")
# print("age")
# print("name")

# # to make a null dictionary

# "null dict"={}

# # nested dictionary 

# student={
#     "name":"rahul kumar",
#     "subject" : {
#         "phy": 97,
#         "chem":98,
#         "math":95
    
#     }
# }

# # nested dictionary 

# print(student["subjec"]["chem"])

# # sets in python
# collection={1,2,2,2,"hello","world","world",4}

# print(collection)
# print(len(collection)) #total no. of items 

# collectin={} #it is a syntax of a empty dictionary

# print(type (collectin))

# collection=set() # write syntax of defining a null set 

# print(type(collection))


# # some questions to practice 
# # storing word menings in a dictionary 
# dict={
#     "table":["a peice of furniture","list of facts & figures"],
#     "cat":"a small animal"

# }
# print(dict)

# # program to find out how may classrooms are needed to study all of the subjects 
# set1={
#     "python","java","C++","python","javascript",
#     "java","python","java","c++","c"
# }

# print(len(set.union(set1)))

# marks={

# }

# a=int(input("enter phy:"))
# marks.update({"phy":a})
# a=int(input("enter chem:"))
# marks.update({"chem":a})
# a=int(input("enter math:"))
# marks.update({"math":a})

# print(marks)

# # to store 9 and 9'0 in a dictioary  

# values={
#     ("float",9.0),
#     ("int",9)
# }

# print(values)


####ch=5

# # loops in python 

# while True: 
#     print("hello") # creates infinite loop which does not end 

# # loop with finite value (while loop)

# i=1
# while i <= 5:
#     print("hello")
#     i += 1

# i=1
# while i <= 10000:
#     print("appnacolledge",i)
#     i += 1


# # print numbers from 1 to 5

# i=5
# while i >=1:
#     print(i)
#     i -=1

# print ("loop ended")

# # program to print numbers from 1 to 100

# i=1
# while i <=100:
#     print(i)

#     i +=1

# # program to print numbers from 100 to 1 

# i=100
# while i >=1:
#     print(i)

#     i -=1

# # program to print the multiplication table of number n let n be 4 

# i=1
# while i <=10:
#     print (i*4)
#     i+=1

# # print the element of following list using loop [1,4,9,16,25,36,49,68,81,100]
## """accessing the value of ist sepreatly is called travering """
# num= [1,4,9,16,25,36,49,64,81,100]
# idx =0 
# while idx <len(num):
#     print(num[idx]) # nums[0] , nums[1] , nums[2] ....
#     idx += 1

# # program to search for a number x in this touple using loop (1,4,9,16,25,36,49,68,81,100)

# nums =(1,4,9,16,25,36,49,68,81,100)

# x=36

# i=0 # initialisation 
# while i<len(nums):
#     if(nums[i]== x):
#         print ("found at idx",i)
    


# # to use the break keyword 

# nums =(1,4,9,16,25,36,49,68,81,100)

# x=36

# i=0 
# while i<len(nums):
#     if(nums[i]== x):
#         print ("found at idx",i)
#         break #if we want to break the ststement or stop the loop
#     else:
#         print("finding...")
#     i +=1

# print("end of loop")

# # to use the continue statement 

# i=0
# while i <= 5:
#     if(i==3):
#         i +=1
#         continue # if we want to skip something use continue 
#     print(i)        
#     i +=1

# (for loop)
veggies= ["tomato","brinjle","lady finger","cucumber"]

for val in veggies :
    print(val)

print("hello world")
