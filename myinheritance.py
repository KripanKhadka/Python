#is-a relation (inheritance):
#the process of creating new classes based on some existing classes is called inheritance
#object sadheii child class ko banaune
#syntax class childclass(parentcalss)
#class A:pass ----   class B(A): pass

# class P:
#     def m(self):
#         print("This is m method of calss P")
# class C(P):
#     def m1(self):
#         print("this is m1 method of class C")

# s=C()
# s.m()
# s.m1()


# class p:

#     a=10
#     def __init__(self):
#         self.b=20
#     def m1(self):
#         print("this is instance method")
#     @classmethod
#     def m2(cls):
#         print("this is class method")
#     @staticmethod
#     def m3():
#         print("this is static method")


# class c(p):
#     pass

# c=c()
# print(c.a)
# print(c.b)
# c.m1()
# c.m2()
# c.m3()



# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def eat(self):
#         print("person can eat momo")

# class Employee(Person):
#     def __init__(self,name,age,eno,esal):
#         super().__init__(name,age)
#         # self.name=name
#         # self.age=age
#         self.eno=eno
#         self.esal=esal

#     def work(self):
#         print("Employee can work")
#     def empino(self):
#         print("employee Name: ",self.name)
#         print("employee age: ",self.age)
#         print("employee eno: ",self.eno)
#         print("employee salary: ",self.esal)


# c=Employee("Kripan",24,"e445",44000)
# c.eat()
# c.empino()


# class Car:
#     def __init__(self,name,model,color):
#         self.name=name
#         self.model=model
#         self.color=color
#     def getinfo(self):
#         print(f"car name is {self.name}\n car model:{self.model}\n car color: {self.color}")


# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def eatandrink(self):
#         print("Eat momos and drink cocacola")


# class Employee(Person):
#     def __init__(self,name,age,eno,esak,car):
#         super().__init__(name,age)
#         self.eno=eno
#         self.esal=esak
#         self.car=car
#     def work(self):
#         print("Employee can work")
#     def empinfo(self):
#         print("employee Name: ",self.name)
#         print("employee age: ",self.age)
#         print("employee eno: ",self.eno)
#         print("employee salary: ",self.esal)
#         print("car info of employee: ")
#         print()
#         self.car.getinfo()

# c=Car("Ferrari","V2","REd")
# e=Employee("Kripan",24,"e440",50000,c)
# e.eatandrink()
# e.work()
# e.empinfo()

#types of inheritance: single , multi_level , hierrachal,multiple, hybrid and cyclic

#single child class
# class P:
#     def m1(self):
#         print("Parent Class")

# class C(P):
#     def m2(self):
#         print("Child class")

# c=C()
# c.m1()
# c.m2()


#multi level
# class P:
#     def m1(self):
#         print("Parent class")

# class C(P):
#     def m2(self):
#         print("Class method")

# class D(C):
#     def m3(self):
#         print("Child child class")

# c=D()
# c.m1()
# c.m2()
# c.m3()

#hierarchal inheritance : one parent multiple children
# class P:
#     def m1(self):
#         print("Parent Class")

# class C(P):
#     def m2(self):
#         print("this is first child")
# class D(P):
#     def m3(self):
#         print("this is second child")


# c=C()
# d=D()
# c.m1()
# c.m2()
# d.m1()
# d.m3()


#multiple inheritance:multiple parents and single off spring
# class P1:
#     def m1(self):
#         print("Parent one method")
# class P2:
#     def m1(self):
#         print("Parent two method")
# class C(P1,P2):
#     def m1(self):
#         print("Child method")
# c=C()
# c.m1()


#hybrid inheritance: two or more type of inheritance
# class A:
#     def m1(self):
#         print("A class method")
# class B(A):
#     def m3(self):
#         print("B class method")
# class C(A):
#     def m4(self):
#         print("C class method")
# class D(B,C):
#     def m2(self):
#         print("D class method")

# d=D()
# d.m1()




# class A:
#     def m1(self):
#         print("A class method")
# class B:
#     def m1(self):
#         print("B class method")
# class C:
#     def m1(self):
#         print("C class method")
# class X(A,B):
#     def m3(self):
#         print("X class method")
# class Y(B,C):
#     def m1(self):
#         print("Y class method")
# class P(X,Y,C):
#     def m2(self):
#         print("P class method")

# p=P()
# p.m1()

#method resolution order: It goes depth first search (d-l-s)
# class A:
#     pass
# class B(A):
#     pass
# class C(A):
#     pass
# class D(B,C):
#     pass
# print(B.mro())
# print(C.mro())
# print(D.mro())



# class A:
#     def m1(self):
#         print("A class method")
# class B:
#     def m1(self):
#         print("B class method")
# class C:
#     def m1(self):
#         print("C class method")
# class X(A,B):
#     def m3(self):
#         print("X class method")
# class Y(B,C):
#     def m1(self):
#         print("Y class method")
# class P(X,Y,C):
#     def m2(self):
#         print("P class method")

# print(P.mro())

#head is first element
#others all are  tail
#mro algorithm (c3 algorithm): samuel pedroni
#if head is nott in tail of any other lis then add this to result and remove from the list
#if head is present at tail cosider head element of next list
#mro of a= a,obj----mro of b =b,obj-------mro of c=c,obj----------mro of x=x,a,b,obj-----mro of y=y,b,c,obj-
#mro of p=p+merge(mrox,mroY,mroC....,XYC)
#=p+merge(XABo,YBCo,Co,XYC)
#=p+x+merge(ABO,YBCO,CO,YC)
#p+X+A+Merge(bo,ybco,co,yc)
#p+x+a+y+merge(bo,bco,co,c)
#p+x+a+y+b+merge(o,co,co,c)
#p+x+a+y+b+c+merge(o,o,o,o)
#pxaybco


