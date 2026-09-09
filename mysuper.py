# class P:
#     def m1(self):
#         print("this is parent method.")

# class C(P):
#     def m1(self):
#         super().m1()
#         print("this is child method.")

# c=C()
# c.m1()

# class P:
#     a=10
#     def __init__(self):
#         self.b=20
#         print("Parent construtor is called.")
#     def m1(self):
#         print("Parent Class instance method is called")
#     @classmethod
#     def m2(cls):
#         print("parent class method is called")
#     @staticmethod
#     def m3():
#         print("Parent class static method")


# class C(P):
#     a=555
#     def __init__(self):
#             super().__init__()
#             super().m1()
#             super().m2()
#             super().m3()
#             self.b=666
#             print("Parent construtor is called.")
            

# c=C()
# print(c.b)


# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print("Name: ",self.name)
#         print("age: ",self.age )

# class Student(Person):
#     def __init__(self,name,age,roll,mark):
#         super().__init__(name,age)
#         self.roll=roll
#         self.mark=mark
#     def display(self):
#         super().display()
#         print("Roll no: ",self.roll)
#         print("Marks: ",self.mark)
        

# s=Student("Kripan",22,19,98)
# s.display()


# class A:
#     def m1(self):
#         print("A calss method")
# class B(A):
#     def m1(self):
#         print("B calss method")
# class C(B):
#     def m1(self):
#         print("C calss method")
# class D(C):
#     def m1(self):
#         print("D calss method")
# class E(D):
#     def m1(self):
#         # super().m1()
#         # A.m1(self)
#         super(B,self).m1()
#         print("E calss method")

# e=E()
# e.m1()


#from child class we are not allowed to access parent calss instance varible by super( ) compulsory we should use self
# class P:
#     a=10
#     def __init__(self):
#         self.b=20

# class C(P):
#     def m1(self):
#         print(self.b)
# c=C()
# c.m1()

#from child class constructor and instance method we can access parent calss instance ,static and class method by using super()
# class P:
#     def __init__(self):
#         print("parent class constructor")
#     def m1(self):
#         print("Parent class instance method")
#     @classmethod
#     def m2(cls):
#             print("parent class class method")
#     @staticmethod
#     def m3():
#             print("Parent class static method")

# class C(P):
#       def __init__(self):
#             super().__init__()
#             super().m1()
#             super().m2()
#             super().m3()
#       def m1(self):
#             super().__init__()
#             super().m1()
#             super().m2()
#             super().m3()
            
      

# c=C()


#in child class static method we are not allowed to use super() generally but we can use in a special way

# class P:
#     def __init__(self):
#         print("parent class constructor")
#     def m1(self):
#         print("Parent class instance method")
#     @classmethod
#     def m2(cls):
#             print("parent class class method")
#     @staticmethod
#     def m3():
#             print("Parent class static method")

# class C(P):
#       @staticmethod
#       def m1():
#             super(C,C).m2()
#             super(C,C).m3()

# c=C()
# c.m1()



#Polymorphism: Many Form
#3) Duck typing philosophy ------overloading(operator,method,constrtuctor)----------overriding(method,constructor)
#if any animal can swim like duck walk like a duck and quack like a duck is a duck