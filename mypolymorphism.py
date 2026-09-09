#overloading , overriding , ducktyping
#operator overloading , method and construtcor

# print(20+30)
# print("heelo"+"world")
# print(3*"A")


# class Book:
#     def __init__(self,pages):
#         self.pages=pages
#     def __add__(self,other):
#         return self.pages+other.pages
# b1=Book(200)
# b2=Book(100)
# print(b1+b2)
#+---> __add__(self,other)
#-    ==> __sub__(self,other)
#__mul__
#__div__
#__floordiv__
#__mod__
#__pow__

# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def __gt__(self,other):
#         return self.marks>other.marks

# s=Student("Kri",42)
# s1=Student("SIT",44)
# print(s<s1)


# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def __mul__(self,other):
#         return self.salary*other.days

# class Attendancesheet(Employee):
#     def __init__(self,name,days,salary):
#         super().__init__(name,salary)
#         self.days=days


# t=Attendancesheet("kri",15,50000)
# print("total salary:",t.days*t.salary)

# class Student:
#     def __init__(self,name,roll,marks):
#         self.name=name
#         self.roll=roll
#         self.marks=marks
#     def __str__(self):
#         return f"this is {self.name} object"

# s1=Student("kri",7,99)
# s2=Student("sit",12,99)
# print(s1)
# print(s2)


# class Book:
#     def __init__(self,pages):
#         self.pages=pages
#     def __add__(self,other):
#         # return self.pages+other.pages
#         return Book(self.pages+other.pages)
#     def __str__(self):
#         return f"total no of pages is {self.pages}"
# b1=Book(400)
# b2=Book(300)
# b3=Book(400)
# print(b1+b2+b3)

# class Book:
#     def __init__(self,pages):
#         self.pages=pages
#     def __add__(self,other):
#         # return self.pages+other.pages
#         return Book(self.pages+other.pages)
#     def __mul__(self,other):
#         return Book(self.pages*other.pages)

#     def __str__(self):
#         return f"total no of pages is {self.pages}"
# b1=Book(400)
# b2=Book(300)
# b3=Book(400)
# b4=Book(500)
# print(b1+b2*b3+b4)


#method overloading:No method overloading in python;but explixitly its possible
# class Test:
#     def m1(self):
#         print("No arg-method")
#     def m1(self,a):
#         print("One arg")
#     def m1(self,a,b):
#         print("Two arg")

# Test().m1("kri","bri")


# class Test:
#     def sum(self,*a):
#         total = 0
#         for x in a:
#             total =total+x
#             print("the sum is :",total)

# t=Test()
# t.sum(10)
# t.sum(11,22,33,44)


#overriding:#it is the type of thinge we have done like child overrding the parent in inheritance

#Ducktyping: if any animal swims like a duck, walk like a duck adn quaks like a duck then animal is a duck


# class Duck:
#     def swim(self):
#         print("Quack Quck")
# class Dog:
#     def talk(self):
#         print("Vow Vow")
# class Cat:
#     def talk(self):
#         print("meow Meow")
# class Goat:
#     def talk(self):
#         print("Myaa myaa")


# def f1(obj):
#     if hasattr(obj,"talk"): 
#         obj.talk()
#     else:
#        print("NO attribute talk")
# l=[Duck(),Dog(),Cat(),Goat()]
# for obj in l:
#     f1(obj)