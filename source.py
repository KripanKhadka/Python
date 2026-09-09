print("hello world")
a=10;
print(a)
cash =100;
print(cash);
print(id(a));

# #__name this is private
# #___name this is protected/ strictly private
# #__name__ this is magic variable/dunder varianble 



#  #reserved words or keywords
# #mainly 33 words
# #EXCEPT FINALLY RAISE IMPORT FROM AS CLASS DEF ASSERT PASS GLOBAL NON LOCAL LAMBDA
#  #DEL WITH





# #Dynamically type data
# #a=10;

# #int float complex bool str byte bytearray range list tuple
# #set frozenset  dict none

# #int takes whole number in binary decimal octal or hexadecimal default is decimal(0-9)

# #for the binary representation we use 0b or 0B
# #for octal 0o or 0O
# #for hexadecimal we use 0x or 0X

# #to convert into the binary we use  bin()
# #to convert inro the octal we use oct()
# #to convert into the hexadecimal we use hex()
# #we can directly use complex number in python
# #we need j to represent a complex number

# #a=0b1101+2j
# #print(a)
# # we can also use the binary or hex or oct for the real number but not for the imaginary

# #a=2+5j
# #b=4+6j
# #print(a*b)
# # we can do any arithmetic operations in python for complex number.

# # to get only real part we do
# #print(a.real)
# # for the imagiranry we do
# #print(a.imag)

# #Boolean data type; either True or false python interpreter takes internally true as 1 and false as 0
# #a=20
# #b=10
# #c=b>a
# #print(c)
# # in python we can add true and false since it takes true as 1 and false as 0
# #a=True
# #b=True
# #c=False
# #print(a+b)# it gives 2 since both are True
# #print(b+c)# it gives 1 since One is True other is False

# #String data type
# # a="apple keeps doctor away"
# # print(type(a))
# #Slicing of string
# #we also have a negative indexing in python
# # print(a[-3])
# # print(a[8:15])#we can find the range of the string
# # print(len(a))# this is for length
# # print(a[0].upper()+a[1:])

# #type casting
# # to convert any data type into int we use int
# # a=15.9
# # print(int(a))
# # b=True
# # print(int(b))
# # c="10"# if there is integer with base ten inside string we can convert the string to integer otherwise a string cannot be converted into an int
# # print(int(c))
# # # to convert into floast we use float
# # d=16
# # print(float(d))
# # to convert into the complex we use complex

# e=17
# # print(complex(e))
# # f="10"
# # print(complex(f))
# # print(complex(True,False))

# # #Boolean
# # print(bool(10))# 0 bayek sab trye aauxa
# # print(bool("True"))#string vitra j sukei hos True haina vaney false

# #string
# # a="hello"
# # print(str("3+6j"))# number dekhiye pani string ho
# # print(str(True))

# #Fundamental data types vs Immutability(not changeable)
# #All fundamental data types are immutable, Once we create an object, we cannot perform any changes in that object.
# # If we try to change than with those changes  new object is created
# # In python everything is object

# #for eg
# # z=10
# # print(id(z))
# # z=z+2
# # print(id(z))# the prevoius one object is cleared by the Garbage Collectot(GC)
# # # if they have the same value then it is smart enough to reference it to same object
# # a=10
# # b=10
# # print(id(a))
# # print(id(b))
# # print(a is b)
# # #mutable case example the list doesnot create new object but replace the value in it.
# # a=[10,20,30,40]
# # print(a)
# # print(id(a))
# # a[0]=50
# # print(a)
# # print(id(a))
# # group of datas lai represent garna list,tuple,set,frozenset,dict,range,bytes and bytesarray
# # id we want to represent a group of value as single entity where insertion order is preserved and duplicates are allowed
# # we should go for list


# #LIST
# # x=[10,20,30,40,50,10,"Hello",True]
# # print(type(x))
# # #heterogeneous values are allowed
# # #slicing is allowed because the order is preserved
# # print(x[2:4])
# # x.append(90)#append ley thapxa last ma tara
# # x.remove(10)# remove huda chai agadhi bata  hunxa
# # print(x)
# # for x in x:
# #     print(x)# yo chai for loop euta euta object dekhauna


# #TUPLES
# #exactly as list but immutable list we use small bracket
# #tuples    
# # t=(10,20,30,40)
# # print(type(t))
# # #to make a single value tuple we must give a , behind the number otherwise it will give us a int value
# # u=(10,)
# # print(type(u))
# # print(t[1])
# # print(t[1:4])


# #SET
# #if we want to represent a value wihtout duplicates and insertion order is not preserved
# #heterogeneous object is allowed
# #no insertion order
# #mutable

# # s={10,20,30}
# # print(type(s))
# # #to make a single value set is s=set()
# # # to add in set we use s.add and s.remove
# # s.add(40)
# # s.add(50.6)
# # s.add(80)
# # print(s)



# #FROZENSET
# #exactly set but immutable
# # fs=frozenset(s)
# # print(fs)
# # print(type(fs))


# #DICTIONARY dict
# #mutable
# #works in key value pair
# #order is not preserved
# #vakue can be replaceable by key
# # j={100:"kri",200:"khadka"}
# # print(j)
# # print(type(j))


# #RANGE
# #it represents sequence of number
# #immutable
# #different forms form1:
# # r=range(10)
# # #form2:
# # r=range(10,20)
# # #form3:
# # r=range(10,20,2)
# # print(type(r))
# # print(r)
# # for i in r:
# #  print(i)
# # print(r[2:5])


# #BYTES
# #immutable
# #value must range from 0 to 255
# #there cannot be heterogeneous data types
# # k=[10,20,30,40]
# # by=bytes(k)
# # print(type(by))
# # for i in by:
# #     print(i)


# #BYTEARRAY
# #same as byte but mutable
# # l=[10,20,30,40]
# # by=bytearray(l)
# # by[0]=11
# # print(type(by))
# # for i in by:
# #     print(i)



# #NONE
# #for garbage collection we use none



# #scape sequence can only be used inside a string
# # S='python\'s \n classes'
# # print(S)
# # #\n gives new tab, \t gives tab, \r gives carriage return , \b gives backspace,\v vertical tab, \' gives single quote and all
# # #CONSTANT
# # #generally anything in capital value is considered a constant but there is no any case like c where we keep const

# # MAX=10;
# # print(MAX)

# #3.1 operators
# #1) Arithmetic operators, 2)relational or comparison operators 3)logical operators 4) Bitwise operators 5)Assignment Operators 6) equality 7)shift 8)ternary 9)special(identity,membership)

# #Arithmetic operators
# #+,-,*,/,**,//,%

# # print(10+2)
# # print(10-2)
# # print(10*2)
# # print(10/2)
# # print(10%3)
# # print(10**2)
# # print(10//3)#this is floor
# # # in string we can use two arithmetic operators +,*
# # print("kri" + "khadka")#this is concatenation
# # print("kri "*5)# we cant put multiplication operator between two string operator there must be one integer
# # # we use type casting for it
# # a="hello "
# # print(a*False)#it is empty because it internally reads 0
# # print(a*True)# it prints hello since its internally one


# # #COMPARISON OR RELATIONAL OPERATORS
# # a=10
# # b=20
# # print(a>b)
# # print(a<b)
# # print(a>=b)
# # print(a<=b)
# # #two strings can be comapred by using first symbol using ascii value of it
# # # to know ascii value we use print(ord("A"))
# # # to know the digit value we use chr: print(chr(105))
# # d="kripan"
# # b="merina"
# # print(d>b)
# # print(d<b)
# # print(d<=b)
# # print(d>=b)
# # #chaining is allowed in this comparison operator
# # print(10<20<30)
# # print(10>20<30<40)

# #EQUALITY OPERATOR
# # print(10==20)
# # print(10!=20)
# # print(1==True)
# # print(10==10.0)
# # #chaining is also allowed in this if one is false then all is false
# # print(10==10!=20!=10==10)


# #LOGICAL OPERATOR
# # IT IS USED FOR BOTH BOOLEAN AND NON BOOLEAN
# #AND-> BOTH TRUE THAN TRUE , OR-> atleast one is true than true not opposes the sign
# # print(True and True)
# # print(True and False)
# # print(True or False)
# # print( not False)



# #NON BOOLEAN
# #0 mean false non zero is true
# #empty set,list,tuple, dict are all fasle
# #if x is false then return x
# #if x is true then return y
# # print(10 and 20)
# # print("" and "python")
# # username=input("enter your username")
# # password=input("enter your paassword")
# # if username=="python" and password =="pass":
# #     print("correct credentials")
# # else:
# #     print("username mismatch")

# # # if x is true than return x
# # # if x is false then return y
# # print([10] or 20)
# # print("hello" or "")

# # print(not "")
# # print(not False)


# #BITWISE OPERATOR
# # it works on bits & bit wise and
# #bitwise or |
# #bitwise x-or ^
# #bitwise complement ~
# #bitwise << left shift
# #bitwise >> left shift
# # to use it it must be completely int or bool

# #bitwise and: if both bits are 1 than result is 1
# # bitwise | if atleast one than 1 else 0
# # if both are dif than 1 else 0
# # nor if 1 then 0 if  then 1

# # print(4&5)
# # print(4|5)
# # print(4^5)
# # print(~4)
# # #msb indicates sign bit 0 -> +ve and 1->negative bit
# # #positive number will be represented directly whereas -ve numbers will be represneted in 2s complement form
# # print(10<<2)
# # print(10>>3)

# #ASSIGNMENT OPERTOR(=)

# # X=10
# # #COMPOUND ASSIGNMENT OPERATOR (IF THERE IS ANY ARTHMETIC OR BITWISE WITH =)
# # X+=5
# # print(X)


# # #TERNARY OPERATOR/conditional operator
# # #SYNTAX x=first-value if condition else second value
# # a=10
# # b=20
# # c=10 if a>b else 20
# # print(c)

# # a=int(input("enter a number:"))# the reason the deafult input is string

# # b=int(input("enter a number:"))
# # c= a if a>b else b
# # print("the greater number is:", c)

# # #NESTING OF TERNARY ALGORITHM
# # a=int(input("enter the first number"))
# # b=int(input("enter the second number"))
# # c=int(input("enter the third number"))
# # max=a if a>b and a> c else   b if b>c  else c 
# # print("the greatest number is", max)

# #Special operators
# #1) Identity and Membership Operators



# #1) Identity Operators
# #is and is not address comparison ko lagi ho
# # a=10
# # b=10
# # c=11
# # print(a is b)
# # print(a is not c)
# #for lists its not a fundamental data types hence new object is created


# #2) Membershio opeartors
# #in and not in
# # x="python is fun"
# # print('s' in x)
# # print("python " in x)
# # print("but" in x)
# # print("python " not in x)


# #OPERATOR PRECEDENCE: it describes the order or priority



# #MATH MODULE: collection of functions, variables, class etc for reusability done using import
# # import mymath as m  # this  m is aliasing 
# # import math
# # print(m.add(10,20))
# # print(m.multiply(10,20))
# # r=5
# # print("the area of circle is:", math.pi*math.pow(r,2))# math.pow is used to find the power of a number
# # print(dir(math))# it gives all the functions and variables inside the math module
# # from math import pi,pow# we can also import specific function or variable from the module

# # from math import *# it imports all the functions and variables from the module
# # #the difference between from and import is that in import we have to use the module name to access the function or variable but in from we can directly use the function or variable without using the module name


# #PYTHON INPUT AND OUTPUT
# # roll=int(input("enter the student roll number: "))
# # marks=float(input("enter the student marks: "))
# # name=input("enter the name of student:")
# # ispass=eval(input("True if pass , false if fail: "))
# # print("the student info is below: ")
# # print("Roll Number is: ", roll, type(roll))
# # print("Marks is:", marks, type(marks))
# # print("Name is: ",name,type(name))
# # print("the status is: ",ispass,type(ispass))





# # a=input("enter the number you want to put")
# # print(a)
# # b=a.split()
# # c=[int(x) for x in b]
# # print(type(a))
# # print(type(b))
# # print(type(c))


# # a,b=[int (x) for x in input("enter two numbers").split(",")]# split le tukrayo for x in le sab lai janauxa ani int x le janako x lai integer banauxa
# # print(a+b)


# # from sys import argv
# # print("the length is ",len(argv))
# # print("the name of the file is",argv[0])
# # print("the line to line is")
# # for x in argv:
# #     print(x)



# #Output statement
# # a=10
# # m=12
# # n=14
# # print("the values are",a,n,m)#yesle multiple value print garna sakxa
# # print("the values are ",a,m,n,sep=":")#sep le chai comma use garxa instead of space

# #by default we use end="\n" but we can change it to anything we want we overide it using end=""
# # print("kripan", end="")
# # print("khadka ", end="")

# # name="kripan"
# # age=21
# # # print("my name is",name ,"age is" ,age)

# # # we can also use formatting to print the output in a specific format
# # # print("my name is {} and age is {}".format(name,age))

# # #we can also use f-string to print the output in a specific format
# # print(f"my name is {name} and age is{age}")




# #CONTROL FLOW / CONTROL STRUCTURE

# # a=int(input("enter the first number:"))
# # b=int(input("enter the second number:"))
# # c=int(input("enter the third number:"))
# # if a>b and a>c:
# #     print(f"{a} is greater than {b} and {c}")
# # elif b>c and b>a:
# #     print(f"{b} is greater than {a} and {c}")
# # else:
# #     print(f"{c} is greater than {a} and {b}")    

# # name=input("enter name:")
# # age=int(input("enter age:"))
# # if name=="kripan" and age==21:
# #     print("you are eligible")
# # elif name=="khadka" and age==22:
# #     print("you are eligible")    
# # else:
# #    print("you are not eligible")

# # print("this is end of the program")


# #q1
# # a=int(input("enter a number:"))
# # b=int(input("enter second number:"))
# # if a<b:
# #     print(f"the smaller number is {a}")
# # else:
# #     print(f"the smaller number is {b}")


# #q2
# # x=int(input("enter first number:"))
# # y=int(input("enter second number:"))
# # z=int(input("enter third number:"))
# # if x<y and x<z:
# #     print(f"the smallest number is {x}")
# # elif y<z:
# #     print(f"the smallest number is {y}")
# # else:
# #     print(f"the smallest number is {z}")


# #  q3
# # x=int(input("enter a number:"))
# # if x%2==0:
# #     print(f"it is even number: {x}")
# # else:
# #     print(f"It is odd number: {x}")  


# # sub =int(input("Enter a sub:"))
# # match sub:
# #     case 'DSA':
# #          print("DSA")
# #     case 'python':
# #           print("Python")
# #     case _:
# #           print("Oh no you missed exciting subject")      



# # n=int(input("enter a number:"))
# # if n==1:
# #       print("One")
# # elif n==2:
# #       print("two")
# # elif n==3:
# #       print("three")
# # elif n==4:
# #       print("four")
# # elif n==5:
# #       print("five")
# # elif n==6:
# #       print("six")
# # else:
# #       print("other than 1, 2, 3, 4, and 5")



# #using switch case
# # list=["one","two","three","four","five","six"]
# # n=int(input("enter any number:"))
# # print(list[n-1])



# #Iterative statements
# #syntax for x in sequence:
# # body
# # s="learning"
# # for x in s:
# #     print(x)

# # r=input("enter any string:")
# # for x in r:
# #     print(x) for loop in string 


# # s=input("enter any string:")
# # i=0
# # for x in s:
# #  print(f"the first character in {i} is {x}")
# #  i+=1


# # for x in range(10):
# #     print(x)

# # for x in range(20,0,-1):# this brings the number from 20 to 1 in reverse order
# #    if(x%2!=0):
# #       print(x)

# # list=eval(input("enter a list of numbers: "))
# # sum = 0
# # for x in list:
# #     sum = sum + x

# # print("the sum is ", sum)







# #while loop

# # x=1
# # while x<10:
# #     print(x)
# #     x=x+2



# # n=int(input("enter a number:"))
# # sum=0
# # i=1
# # while i<=n:
# #     sum =sum+i
# #     i=i+1
# # print(f"the sum of {n} numbers is:{sum}")




# # name=input("enter a name:")
# # while name!="kripan":
# #     name=input("try  another name:")
# # print("you entered the correct name")

      

# # for i in range(3):
# #     for j in range(2):
# #         print(i,j)

# # n=int(input("enter number of rows:"))
# # for i in range(n):
# #       for j in range(n):
# #         print("*", end="")







# #break statement
# # for i in range(100):
# #   if i==10:
# #     print("i am done!")
# #     break
# #   print(i)
     

# # j=[1,2,300,400,60,500,600,800,80]     
# # for i in j:
# #     if i>=500:
# #         print("cannot shop higher than 500")
# #         break
# #     print(i)
# # print("thanks for shopping with us")


# # del removes the reference variable a
# # a=10
# # print(a)
# # del a
# # print(a)


# #STRING
# # s="kripankhadka"
# # print(type(s))

# # j='''this 
# #   is 
# #    my 
# #    name
# #      '''
# # print(type(j))




# #Accesing the character of a  string
# #1) indexing 2) slicing

# # s="python is fun"
# # # print(s[4])
# # # print(s[-9])
# # i=0
# # for x in s:

# #     print(f"the character is {x} present at positive indes {i} and negative index{i-len(s)}")
# #     i=i+1


# #slicing
# # [begin:end-1:step]




# # name=input("enter a name").strip()
# # if name=="kripan":
# #     print("the name is correct")
# # else:
# #     print("incorrect name")
# # we cana also use rstrip() and lstrip()



# # a="learning pyton is fun"
# # print(a.rfind("i",7,60))#this is using the gap between



# # l=[10,20,3,40,50]
# # i=0
# # while i<len(l):
# #     print(l[i])
# #     i=i+1


# # l=[10,20,30,40,50]
# # for i in l:
# #     print(i)



# #list has append , insert , extend



# #Functionn:: code reusability
# #types of function: built in and user defined id() print() type() eval()
# #user defined function (syntax)
# # we use def which is define
# # def function_name(parameters):
# # ''' doc string '''
# #
# #function body
# #
# #return value( return value is optional)
# # to call a function we use function_name ()



# # def hello(name):
# #     print("hello",name)

# # hello("vaskar")# if there is parameter then there must be given input
# # hello("mer")


# # def square(num):
# #     print(f"the square of {num} is",num*num)

# # square(5)

# # def add(a,b):
# #     sum=a+b
# #     return sum
# # a=add(20,10)
# # print(a)
# # print("the sum is",add(10,20))


# # def odd(num):
# #     if num%2==0:
# #       (print(num,"is even number"))
# #     else:
# #        (print(num,"is odd number"))


# # odd(12)
# # odd(10)



# # def fact(num):
# #     result=1
# #     while num>=1:
# #         result=result*num
# #         num=num-1
# #     return result

# # a=fact(5)
# # print(a)


# # def sum_sub(a,b):
# #     sum=a+b
# #     sub=a-b
# #     return sum,sub

# # a,b=sum_sub(10,20)
# # print("the sum is ",a)
# # print("the sub is",b)




#4 types of agrumenet in python 
#positional arguement, keyword argument, default and variable argument

# def sub(a,b):
#     print(a-b)

# sub(20,10)
# sub(20, b=30)
# sub(a=20,b=10)
# sub(b=10,a=20)