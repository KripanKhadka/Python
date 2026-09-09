# class Test:
#     def __init__(self):
#         print("This is constructor")
#     def __del__(self):
#         print("This is destructor")

# t=Test()
# print("End of application")

# import time
# class Test:
#     def __init__(self):
#         print("This is constructor")
#     def __del__(self):
#         print("This is destructor")

# t=Test()
# print("Constructor is just called")
# time.sleep(5)
# t1=t
# t2=t
# print("test subject has 3 ref now")
# del t
# print("t reference is deleted")
# time.sleep(5)
# del t1
# print("t1 is deleted")
# time.sleep(5)
# del t2
# print("t2 is deleted")
# time.sleep(5)
# print("End of application")


# class Test:
#     def __init__(self):
#         print("this is is constructor")
#     def __del__(self):
#         print("This is destructor")

# l=[Test(),Test(),Test()]
# del l 
# print("end of application")


#no of reference in an object
# import sys
# class Test:
#     pass
# t=Test()
# t1=t
# t2=t1
# t3=t1
# del t1
# print(sys.getrefcount(t))


#Constrcutor --------------------------------------------Destructor
#__init__(self)-------------------------------------------__del__(self)
#Object initailization---------------------resource dellocation/cleanup
#as soon as object is made------------------just before GC destroys the object


#Using Members of One Class Inside another class:
#2 ways has-a realtion(composition) --------------- is-a(inheritance) relation

