# #BANK SYSTEM
# import sys
# class Customer:
#     """This is Bank System"""
#     bank_name="ACEM"
#     def __init__(self,name,balance=0.0):
#         self.name=name
#         self.balance=balance


#     def deposit(self,amount):
#         self.balance=self.balance+amount
#         print("New balance after deposit is:",self.balance)

#     def withdraw(self,amount):
#         if amount> self.balance:
#             print("Insufficient find. Please Deposit Firse")
#             sys.exit()
#         else:
#             self.balance=self.balance-amount
#             print("Balance after winthdraw:", self.balance)

# print()
# print("#"*50)
# print("Welcome to ACEM bank")
# print("#"*50)
# name=input("Please enter your name: ")
# c=Customer(name)
# while True:
#     print("d-deposit \n w-withdraw \n e-exit")
#     option =input("Enter your option: ")
#     if option=="d" or option =="D":
#         amount = float(input("Enter your amount to deposit : "))
#         c.deposit(amount)
#     elif option =="w" or option=="w":
#         amount = float(input("Enter your amount to withdraw : "))
#         c.withdraw(amount)
#     elif option == "e" or option=="E":
#         print("Thank you for using our services")
#         sys.exit()
#     else:
#         print("Invalid Option. Please choose valid option")
    

# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def display(self):
#         print("the name is: ",self.name)
#         print("the marks is: ",self.marks)
#     def grade(self):
#         if self.marks>=60:
#             print("First grade student")
#         elif self.marks>=50:
#             print("Second grade student")
#         else:
#             print("You fail")

# n=int(input("Plaese enter how mant studnets: "))
# for i in range(n):
#     name=input("Enter your name: ")
#     marks= int(input("Enter your marks: "))
#     s=Student(name,marks)
#     s.display()
#     s.grade()
#     print()


#2 special instance method: 1) setter(mutator) 2) getter(accessor)
#syntax for Seter:   def setVAr(self,variable): self.variable=variable
#syntaf for getter: def getVar(self,varibale): self.name=name


# class Student:
#     def setName(self,name):
#         self.name=name
#     def getName(self):
#         return self.name
#     def setMarks(self,marks):
#             self.marks=marks
#     def getMarks(self):
#             return self.marks


# n=int(input("enter the number of student: "))
# for i in range(n):
#       s=Student()
#       name=input("enter your name: ")
#       s.setName(name)
#       marks=int(input("enter your marks: "))
#       s.setMarks(marks)
#       print("HI", s.getName())
#       print("Your marks is: ", s.getMarks())
#       print()



#class method
# class ACEM:
#     department=4
#     @classmethod
#     def work(cls,name):
#         print(f"Acem has  {cls.department} department")

# # a=ACEM()
# # a.work("computer")

# ACEM.work("Computer")#only access this through class name not object


# class Test:
#     count=0
#     def __init__(self):
#         Test.count=Test.count+1
#     @classmethod
#     def noofobj(cls):
#         print("The number of object created is: ",cls.count)

# s=Test()
# s1=Test()
# s2=Test()
# s3=Test()
# Test.noofobj()



#instance method ----------------------- class method
#atleast one instance variable----------Only static variable
#Instance variable, satatic variable,local varibale--------------only static varibale
#has self as first parameter--------------has cls as first parameter
#no decorator required---------------- decorators required
#object reference to call-----------------uses class name  but can be used by object reference too


#Static Method:
# class ACEMMath:
#     @staticmethod
#     def add(x,y):
#         print("the sum is: ",x+y)
#     @staticmethod
#     def sub(x,y):
#         print("the sub is: ",x-y)
#     @staticmethod
#     def product(x,y):
#         print("the product is: ",x*y)

# ACEMMath.add(10,20)
# ACEMMath.sub(10,20)
# ACEMMath.product(10,20)


#shortut to remember
#only instance variable---------> instance method
#only static variable------------> class method
#instance and static ----------> instance method
#instance and local ----------> instance
#static and local ----------------> class method
#only local method ------------> static method



#Inner classes:
# class TU:
#     def __init__(self):
#         print("Outer class")
#     class IT:
#         def __init__(self):
#             print("IT class")
#         def m(self):
#             print("Inner class method")

# s=TU()
# s.IT().m()


# class out:
#     def __init__(self):
#         print("Outer object is created. ")
#     class In:
#         def __init__(self):
#             print("Inner object is created. ")
#         class InnerInner:
#             def  __init__(self):
#                print("Inner inner object is created")
#             @staticmethod
#             def m():
#                 print("Inner Inner class") 

# out().In().InnerInner().m()


# class Human:
#     def __init__(self):
#         self.name="Kripan"
#         self.head=self.Head()
#         self.brain=self.Brain()
#     def display(self):
#         print("Hello ,",self.name)

#     class Head:
#         def talk(self):
#             print("Head can rotate. ")
#     class Brain:
#         def think(self):
#             print("Brain can think. ")

# h=Human()
# h.display()
# h.head.talk()
# h.brain.think()

# class Human:
#     def __init__(self,name):
#         self.name=name
#         self.head=self.Head()
#     def info(self):
#         print("Hello mY name is: ",self.name)
#     class Head:
#         def __init__(self):
#          self.brain=self.Brain()
#         def talk(self):
#             print("talk")
#         class Brain:
#             def think(self):
#                 print("Think")

# s=Human("Kri")
# s.info()
# s.head.talk()
# s.head.brain.think()

# class Test:
#     def m(self):
#         def calc(a,b):
#             print("the sum is:",a+b)
#             print("the diff is: ",a-b)

#         calc(10,20)
#         calc(20,50)
# t=Test()
# t.m()




#Garbage Collector:
#GC--> useless object are automatically deleted by python
#useless object--> object which are not referenced by any variable
# import calendar
# print(dir(calendar))

