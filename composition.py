# class Engine:
#     a=10
#     def __init__(self):
#         self.b=20
#     def m1(self):
#         print("this is engine")

# class Car:
#     def __init__(self):
#         self.engine=Engine()
#     def m2(self):
#         print("Car object using engine Object")
#         print(self.engine.a)
#         print(self.engine.b)

# c=Car()
# c.m2()


# class Car:
#     def __init__(self,name,model,color):

#          self.name =name
#          self.model=model
#          self.color=color

#     def getinfo(self):
#          print(f"Car Name: {self.name}\n   Car.model: {self.model} \n Car Color: {self.color}")


# class Employee:
#      def __init__(self,ename,eno,car):
#           self.ename=ename
#           self.eno=eno
#           self.car=car

#      def empinfo(self):
#           print("employment Name:",self.ename)
#           print("Employment num:",self.eno)
#           print("employee car info:")
#           self.car.getinfo()

# c=Car("Ferrari","V2","Red")
# e=Employee("Ramesh","e550",c)
# e.empinfo()


