#two types of error in python:
#syntax error and runtime error
#syntax is like grammar eror in english and byakran in english
# for  eg
# print "hello"

#runtime error:when the program is running but there is malfnction due to input or logic is called exception
# for eg:
# print("hello hello")
# print("hello hello")
# print("hello hello")
# print("hello hello")
# print(10/0)
# print("hello")
# print("hello")
# print("hello")

# f=open("abc.txt")
# print(f.read())

#open db connection
#read fata
#use data
#close db conn


#exception handling is to find the alternative so that there is no abnormal termination
#how to handle exception handling:
#pythob: try and except
# try has risky code and except: kei error milaune kaam except vitra lekhxau

# DEFAULT EXCEPTION HANDLING: every exception in python is an object
# every excpetion in python is an object

#PYTHON EXCEPTION HIRARCHY
#BASE EXCERPTION IS THE ROOT CLASS
#CHILD CLASS IS EXCEPTION , SYSTEM EXIT , GENERATOR EXIT , KEYBOARD INTERRUPT
#CHILD CLASS OF EXCEPTION: ATTRIBUTE, ARITHMETIC ERROR, EOF ERROR ,NAME ERROR ,LOOKUP ERROR, OS ERROR , TYPE ERROR, VALUE ERROR
#there are further error too for these child ckass of atihtmetic and all

#Excetipn handling using try-except:
#try has risky code , alternative code is inside except

# print("this is my first line of program")
# print(10/0)
# print("this is last line of program")

# print("this is my first line of code")
# try:
#     print(10/0)
# except ZeroDivisionError:
#     print(10/2)
# print("this is my last line of code")


# try:
#     x= int(input("enter first number"))
#     y= int(input("enter sedond number"))
#     print("the result of division is: ",x/y)
# except BaseException as b:
#     print("type of exception is: ", type(b))
#     print("type of exception is: ", b.__class__)
#     print("type of exception is: ", b.__class__.__name__)




#try with multiple except block:
# try:
#     x= int(input("enter first number"))
#     y= int(input("enter sedond number"))
#     print("the result of division is: ",x/y)
# except ZeroDivisionError:
#     print("you cant divide my zero")
# except ValueError:
#     print("value error problem enter integer")
# print("this is end of program")



# try:
#     x= int(input("enter first number"))
#     y= int(input("enter sedond number"))
#     print("the result of division is: ",x/y)
# except (ArithmeticError,ArithmeticError,ValueError) as e:

#     print("the error type is ",e.__class__.__name__)


#default except block:
#try has risky code and except bloac as default except

# try:
#     x= int(input("enter first number"))
#     y= int(input("enter sedond number"))
#     print("the result of division is: ",x/y)
# except ZeroDivisionError:
#     print("you cant divide my zero")
# except:
#     print("even value error is handled")# default except must be the last part of the code

#finally block:
# file=open("abc.txt")


# try:
#     x= int(input("enter first number"))
#     y= int(input("enter sedond number"))
#     print("the result of division is: ",x/y)
# except ZeroDivisionError:
#     print("you cant divide my zero")
# finally:
#     print("thisis clean up activities")


#NESTED TRY -EXCEPT -FINALLY:

# try:
#     print("outer try")
#     print(10/0)
#     try:
#         print("inner try")
#         print(10/0)
#     except ZeroDivisionError:
#         print("inner except block")
#     finally:
#         print("inner finally")
# except:
#     print("outer except block")
# finally:
#     print("Outer finally block")



#CONTROL FLOW IN NESTED TRY -EXPECT-FINALLY 
#else block with try-expcept finally:
#try: risky code
#except: handling code
#else :will be executed if no exceptiom
#finally: clean up code
#

# try: 
#     print("try")
#     # print(10/0)
# except:
#     print("except")
# else:
#     print("else")
# finally:
#     print("finally")



#CASE1
# try:
#     print("try")
#invalid


#CASE 2 
# except:
#         print("except") invalid
#all three must come one or the other


#case 3:
# try:
#     print("try")
# except:
#         print("except") valid


#case 4:
# try:
#     print("try")
# finally:
#         print("finally")# valid


#case 5:
# try:
#     print("try")
# except:
#       print("except")
# finally:
#         print("finally")

#types of exception: predefoned or built in  next is user defined exception
# class TooYoungException(Exception):
#     def __init__(self,args):
#         self.msg=args

# class TooOldException(Exception):
#     def __init__(self,args):
#         self.msg=args
# age=int(input("enter your age"))
# if age>60:
#     raise TooOldException("Oh! Wait some more years and you will get a better one")
# elif age<18:
#     raise TooYoungException("Oh boy! focus on your studies")
# else:
#     print("You will get your match")
