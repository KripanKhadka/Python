# def hello(name="Guest",message="good night"):
#     print(f"the name is {name} and have a {message}")
# hello()
# hello("kripan","Good morning")
# hello("Kripan")
# hello("TenZ")# positional argument sakkisakepaxi matra default argument

# def hello(a,b):
#     print(a+b)

# hello(20,30)


#what input does the user take for that we take variable length arguement

# def hello(*a):
#     print(a)
#     print(type(a))

# hello(2+3)# hence the variable lenth argument is tuple



# def sum(*n):
#     total=0
#     for x in n:
#         total=total+x
#     print("the sum is: ",total)

# sum(10+20+30)



# def f(a, *Args):
#     print(a)
#     print(*Args)

# f(10,20,3,4,5) variabl length argument can only come one time

# def f(**kwargs):
#     print(a)
#     print(type(a))

# f()
# f(a=10,b=30,c=30)


# def hello(**kwargs):
#     for k,v in kwargs.items():
#         print(k,"-----",v)

# hello (a=10,b=20)


# def hello(*args,**kwargs):
#     print(args)
#     print(kwargs)

# hello(10,20,30,40,a=50,b=60,)

#args uses * and kwargs uses **
#args is variable lenth arguments
#kwargs is variable length  keyword argument
# args is tuples and kwargs is an dictioary


#types of varaibale(functional programmig)
#global variable and local variable
#global variable is written outside a function i can access global variable from anywhere

# a=10
# def hello(name):
#     print("the name is:",name)
#     print(a)

# hello("kri")
# print(a)


#the variable that is declared inside a function

# def hello(num):
#     a=10
#     print(num+10)
#     print(a)


# hello(10)
# print(a)


# def hello(num):
#     global a# its must be declared before the  variable is given value
#     a=10
#     print(num+a)

# hello(10)
# print(a)


# def hel(num):
#     print(a)
#     print(num)

# hel(5)

# a=10
# def f():
#     global a
#     a=20
#     print(a)

# f()



# a=10
# def f():
#     global a
#     a=777
#     print(a)
#     print(globals().get('a'))

# f()



#RECURSIVE FUNCTION: which callss itself to be recursion it must have termination criteria and in per turn i must close to termination criteria
# count=0
# def f(n):
#     global count
#     count=count+1
#     if n==0:
#         result=1
#     else:
#         result=n*f(n-1)
#     return result


# a=f(9)
# print(a)
# print(count)





#Anonymous function(lamda function)-> has no name
#short term function only one time functionsometimes we can declare a function without name



# def square(n):
#     return n*n

# print(square(5))


#syntax:  (lambda n:n*n)

# s=lambda n:n*n
# print("the square is",s(4))
# print("the square is",s(5))


# s=lambda a,b:a+b
# print("the sum is ",s(10,20))



# s=lambda a,b:a if a>b else b
# print(s(20,10))


# s=lambda a,b,c: a if a>b and a>c else b if b>c else c
# print(s(10,20,30))



# function as a argument ma use hunxa
# filter()
# map()
# reduce()


#filter syntax : filter(function,sequence)
# l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
# def isEven(n):
#     if n%2==0:
#         return True
#     else:
#         return False

# l1=[]
# for n in l:
#     if isEven(n)==True:
#         l1.append(n)

# print(l1)without filter


# def isEven(n):
#     if n%2==0:
#         return True
#     else:
#         return False

# l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
# l1=list(filter(isEven,l))
# print(l1)


# l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
# l1=list(filter(lambda x:x%2==0,l))
# print(l1)



# std=["kripan","kri","krish","krishtina","anup","sagar"]
# startswithK=list(filter(lambda name:name[0]=="k",std))
# print(startswithK)



#MAP():syntax  map(function,seq)

# l=[1,2,3,4,5]

# def double(x):
#     return 2*x

# l1=list(map(double,l))
# print(l1)


# l=[1,2,3,4,5]
# m=[2,3,4,5,6]
# l1=list(map(lambda x,y:x+y,l,m))
# print(l1)


#reduce(function,sequence) reduces everything to just 1

# from functools import reduce
# l=[1,2,3,4,5]
# l1=reduce(lambda x,y:x+y,l)
# print(l1)


#everything in python is object even a function is anobject
# def f():
#     print("hello")

# f()
# print(id(f))


#Function Aliasing(another name)

# def hello(name):
#     print("helllo",name)

# wish = hello #no bracket should be there
# del hello
# hello("kri")
# wish("kri")


# def outer():
#     print("outer function.")
#     def inner():
#         print("inner function")
#     print("Outer function callling inner function")
#     return inner

# f1=outer()
# f1()


#Modules:A group of variable, function ,class saved in .py is called modules..... code reusability....length of code is decreased and readability of code is increased
 
# import modules

# print(modules.a)
# modules.hello(20,30)
# modules.hi(30,80)



#Module Aliasing
#import modules as m


# import modules as m

# print(m.a)
# m.hello(20,30)
# m.hi(40,50)



# from modules import hello,hi,a we can use * for all members 
# print(a)
# hello(10,20)
# hi(40,40)


# from modules import hello as s, hi as h
# s(20,40)
# h(40,40)


#Various possibilities of import
#import module_name
#import module_name1, module_name2, module_name3
#import module_name as m
#from module import member
#from module import member as member1,member2
#from module import member as m
#from module import member as m, member1 as m1, member2 as m2
#from module import 


#Module Conflict

# from modules import hi as h
# from demo import hi as i

# h(20,30)


#Reloading of module
# from modules import hi as h
# from demo import hi as i
# h(20,30)
# i(40,50)

# import time
# import importlib
# import modules 
# modules.hi(10,20)
# print("our program is on sleep")
# time.sleep(30)
# print("our program is awake")
# importlib.reload(modules)
# modules.hi(20,30)


#DIR_function

# import time
# print(dir(time)) gives us the list about it

# import time
# help(time)


#for every python file there is __name__ is added internally
# import modules indirect execution
# import modules
# modules.f1()
# modules.f2()
# modules.f3()


#MATH MODULE:
# import math
#  print(dir(math))
#  help(math)
# print(math.floor(3.16))
# print(math.sinh(30.6))



#RANDOM MODULE:to generate a random number
# import random
# for i in range(10):
#   print(random.random())
# print(random.randint(1000,6000)) this is for the integer number

# import random
# for i in range(10):
#     print(random.uniform(1000,2000))

# random() is not incluive it doesnot give 0,1 
#randint() is incluive it gives the 0,1
#randomuniform also is not inclusive 

# print(random.randrange(10))
# print(random.randrange(10,20))
# print(random.randrange(1,10,2))


# from random import *
# list=["kripan","rish","sagar","sameer"]
# print(choice(list))


#OTP GENERATION (6 numbers)
# from random import *
# print(randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),sep="")

# from random import *
# otp=""
# for i in range(6):
#     otp = otp+str(randint(0,9))
# print(otp)


# from random import *
# print(randint(000000,999999)) not possible because of the reading six zeros as one zero



#generate fake employee data for database purpose
#name must be 3-10 and must have first alphabet capital
#number must start with e- and must have 4 digit
#salary must be from 10000-50000
#mobile number must start with 6789 and have 10 digits
#designation: software eng, sse, team lead,project lead,manager
#city ktm,pkr,hetauda,kavre,dolokha


#python package
#collection of codes are called function
#collection of function,variables,class are called modules
#collection of modules are called packages
# It can resolve naming conflicts
# we can identify our components/members




#Object-Oriented-Programming
# 3 terms are repeatedly used: Clss, object, reference variable


#class and object , object:physical instance of class.........  class: template/blueprnt/models/design
#object must be feasible physically and plan is the class
#the variables that operates or reference a object is an reference variable
# one object can have multiple reference variable, if the object variable has no referencevariable it is not eligiblefor GC

#class has only two things 1 attributes 2 behaviour
#attributes (properties) 
#beaviour 
#class vitra variable is called attributes a=10
#class vitra function is called behaviour/actions/methods






#SYNTAX: class classname(valid identifier):
                          # """ doc string""" optional
                            # variables
                           # fucntion()









# class Kripan:
#     ''' This class is a demo class. This class does nothing'''
#      #attributes/variables
#      #behaviour /methods()

# # print(Kripan.__doc__)
# help(Kripan)


#to make an empty class
# class A:
#     pass


#Types of variables: Instance(object level), static(class level) and local(method level) variable
#Types of method: Instance , class ,static method more than 95% we use instance method


# class Student:
#     """this is class for student info"""
#     def __init__(self):
#         self.name="kripan"
#         self.roll=1
#         self.marks=99

#     def talk(self):
#         print("hello myname is: ",self.name)
#         print("hello my roll is: ",self.roll)
#         print("hello my marks is: ",self.marks)

#object syntax: referencevariable=classname()
# s=Student()
# s1=Student()
# s.talk()
# print(s.name)

#__init__ is an constructor  we use self to call object inside the class
#constructor meain work is initialization, object vanne bitikeii call hunxa

#self()=default variable that points to current object
# by using self we can access instance varibale and instance method


# class Kri:
#     def __init__(self):
#         print(id(self))


# s=Kri()
# print(id(s))

# class Kripan:
#     """This class is for student"""
#     def __init__(self,name,age,marks):
#         self.name=name
#         self.age=age
#         self.marks=marks

#     def talk(self):
#         print("the name is: ",self.name)
#         print("the age is:",self.age)
#         print("the marks is:",self.marks)
#         print()
#         print()

# s=Kripan("kripan",21,98)
# s1=Kripan("kripan",21,98)
# s.talk()
# s1.talk()
# print(id(s))
# print(id(s1))




#Constructor
#the constructor is def__init__(self):
#when the object is created the construtor is called
# its work is variable initialization
# it is specail varaible
#one object one constrcutor


# class Kripan():
#     def __init__(self,name,age,marks):
#         self.name=name
#         self.age=age
#         self.marks=marks


#     def talk(self):
#         # print("address is: ",self.address)
#         print("Hello welcome, ",self.name)
#         print("Age is: ",self.age)
#         print("Marks is: ",self.marks)
        


# s=Kripan("Thimi",20,30)



#method has any name---constructor must have name __init__
#executed iff we call it explicitly----automatically once object is made
#per object any number od methods---per object only one constructor




# class Kripan():
#     def __init__(self,name,age,marks):
#          self.name=name
#          self.age=age
#          self.marks=marks


#     def talk(self):
#          print("Hello welcome, ",self.name)
#          print("Age is: ",self.age)
#          print("Marks is: ",self.marks)


# list_of_student=[]
# while True:
#     name=input("enter the name: ")
#     age=int(input("enter the age: "))
#     marks=int(input("enter the marks: "))
#     s= Kripan(name,age,marks)
#     list_of_student.append(s)
#     print("Students Info added")
#     option = input("Do you want to continue adding students ? [yes/no]")
#     if option.lower()=="no":
#          break

# print()
# print("All info are:")
# for s in list_of_student:
#      s.talk()
#      print()
#      print()




#types of variables inside a class:
#Instance variable, static and load variable in OOP
#instance variable is object level variable
#class level varaibale is  class level variable
#local variable is method level variable




#Instance variable
#object -object different value is instance variable
#has self as first argument


# class Student():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def talk(self):
#         print("the name is: ",self.name)
#         print("the roll no is: ",self.age)

#     def  m1(self,x):
#         self.x=50


# s=Student("Kripan",22)
# s.talk()



#static variable:
#class level variables are static variables

#types of methods:
#instance method, class and static methos


#instance method having instance variable atleast one
#has first argument as self

#class method has  static variable only used and first method cls and has decorator @classmethod


# class Student:
#     college_name="KCT"#static variable
#     def __init__(self,name,roll):
#         self.name=name#instance variable
#         self.roll=roll#instance variable

#     def talk(self):
#         # self.age=25
#         print("the name is: ",self.name)
#         print("the roll no is: ",self.roll)
#         print()
#         print()

#     @classmethod#class decorator
#     def getcollegename(cls):
#         print("college name is: ",cls.college_name)#class method
#     @staticmethod#static decorator
#     def m1(a,b):
#         print("the sum is:",a+b)

# s=Student("kabir",1)
# s1=Student("Pragyan",2) 
# s2=Student("Kabin",3)      
# s.talk()
# s1.talk() 
# s2.talk()
# s.getcollegename()
# s.m1(10,20)


#Instance Varibale
#for every object a separate copy of instance varibale is created
#Instance variables are always declared by using reference variable

# class Employee:
#     def __init__(self):
#         self.eno=100
#         self.name="Ramesh"
#         self.salary=6000

# e=Employee()
# print(e.__dict__)#to check the dictionary


# class Test:
#     def __init__(self):
#         self.a=10#these lines are same
#         self.b=20
#     def m(self):
#         self.c=30
# t=Test()
# t.m()
# t.d=50#these lines are same
# print(t.__dict__)


#accessing instance variable
# class Test:
#     def __init__(self):
#         self.a=20
#         self.b=30
#     def display(self):
#         print(self.a)
#         print(self.b)

# t=Test()
# t.display()
# print(t.a,t.b)



# class Test:
#     def __init__(self):
#         self.a=10
#         self.b=20
#         self.c=30
#         self.d=40

#     def m(self):
#         del self.d

# t=Test()
# t.m()
# print(t.__dict__)



#STATIC VARIABLE
# class Test:
#     a=10#outside method but inside a class
#     def hello():
#         pass   


# class Test:
#     def __init__(self):
#         Test.b=20#inside a constructor


# class Test:
#     a=10
#     def __init__(self):
#         Test.b=20
    # def m1(self):
    #     Test.c=30
    # @classmethod
    # def m2(cls):
    #     Test.d=40
    #     cls.e=50
    # @staticmethod
    # def m3():
    #     Test.f=60


# t=Test()
# t.m1()
# t.m2()
# t.m3()
# print(Test.__dict__)



#accesing the static variable
# class Test:
#     a=10
#     def __init__(self):
#         print(Test.a)
#         print(self.a)
#     def m1(self):
#          print(Test.a)
#          print(self.a)
#     @classmethod
#     def m2(cls):
#         print(Test.a)
#         print(cls.a)
#     @staticmethod
#     def m3():
#         print(Test.a)


# t=Test()
# t.m1()
# t.m2()
# t.m3()




# class Test:
#     x=10
#     def __init__(self):
#         self.y=20

# t1=Test()
# t2=Test()
# print(t1.x,t1.y)
# print(t2.x,t2.y)
# t1.x=111
# t1.y=222
# print(t1.x,t1.y)
# print(t2.x,t2.y)


# class Test:
#     a=10
#     def __init__(self):
#         self.b=20

# t1=Test()
# t2=Test()
# Test.a=111
# t1.b=222
# print(t1.a,t1.b)
# print(t2.a,t2.b)


# class Test:
#     a=10
#     @classmethod
#     def m1(cls):
#         del cls.a
#         # del Test.a

# t=Test()
# t.m1()
# print(Test.__dict__)



#local variable: temporary requirement inside a method(function)
# class Test:
#     @staticmethod
#     def average(list):
#         result = sum(list)/len(list)
#         return result

# list =[10,20,30,40]
# a=Test.average(list)
# print("the result is: ",a)


