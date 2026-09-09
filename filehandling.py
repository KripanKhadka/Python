# l=[]
# a=input("enter your name: ")
# b=input("enter your address: ")
# l.append(a)
# l.append(b)
# print(l)

#types of files 1) text file(abc.txt) and binary files(apple.jpg)
#opening of file:syntax;f= open(filename,mode).filename is the file i am opening and mode is the operation i am doing
#operation of file:for eg f=open("abc.txt","r") r is the operation
#closing of file:f.close()  ->  resource deallocation

#operations:points at the begininng of the filed r-> read mode , if abc.txt is not there then file not found error its the default mode
#operations:w-> write mode f=open("abc.txt","w") if o abc.txt is not found then new file is created, ani already vaako file ma overwrite gardinxa
#operations:a-> append exactly same as open but the thing is it will not ovveride but add to the present text
#operations:r+ -> it means first read and then write 
#operations:w+ -> write then read 
#operations: a+ -> append then read
#operations: X -> exclusive, abc if already exist then it n causes error it needs new file everytime



#Properties of file object:
# f=open("abc.txt",'r')
# print("the file is open", f.name)#it gives the name
# print("the filemode is ", f.mode)#it gives the mode
# print("the filemode is ", f.closed)#it gives the mode
# print("is it readable ", f.readable())#it gives readability
# print("is it writeable ", f.writable())#it gives writability
# f.close()
# print("the filemode is ", f.closed)


#writing data to txt file
#f.write (str)
#f.writeline(list of lines)

# f=open("abc.txt","a")
# f.write("Kripan")
# f.write("Khadka\n")
# f.write("Prince\n")
# f.write("Smriti")
# print("written in file successfully")
# f.close()

# f=open("abc.txt","w")
# # list=["kri","prince","khadka"] it can also be tuple
# d={"A":"kri","B":"Khadka"}
# f.writelines(d.values())
# print("i think dara is written on file")
# f.close()


# fname=input("enter the filename you want")
# f=open(fname,"w")
# while True:
#     data=input("enter data you want to add: ")
#     f.write(data + "\n")
#     option =input("Do you eant to add more data")
#     if option.lower()=="no":
#         break
# f.close()
# print("Data written Succesfully")




# reading from file
# f.read()---> read total data
#f.read(n)-----> read n number od line from file
#f.readline()--->1 line at a time not whole w run can read one line
#f.readlines()---> reads all from the list


# f=open("abc.txt","r")
# data = f.readline()
# print(data)
# data1=f.readline()
# print(data1)
# f.close()

# f=open("abc.txt","r")
# line=f.readline()
# while line!="":
#     print(line,end="")
#     line=f.readline()

# f.close()


# f=open("abc.txt","r")
# lines=f.readlines()
# print(lines)
# for line in lines:
#     print(line,end="")
# f.close()


# fname=input("enter your file name from which you want to read: ")
# lname=input("enter your file name in which you want to write: ")
# f1=open(fname,"r")
# f2=open(lname,"w")
# data=f1.read()
# f2.write(data)
# f1.close()
# f2.close()

# with open("abc.txt","w") as f1:# with le chaii close na use garda ni vayo
#     f1.write("i have written something")
#     print("is file close",f1.closed)
# print("is file closed",f1.closed)


#tell le mero cursor ko position kata xa vanera dinxa

# with open("abc.txt","r")as f1:
#     print(f1.tell())
#     print(f1.read(5))
#     print(f1.tell())


#seek: f.seek(from where)

# import os,sys
# fname=input("enter the filename: ")
# if os.path.isfile(fname):
#     print(fname,"is in our sysem:")
#     f=open(fname,"r")
#     data=f.read()
#     print(data)
#     f.close()
# else:
#     print("file soes not exit")
#     sys.exit(0)






# import os,sys
# fname=input("enter the filename: ")
# if os.path.isfile(fname):
#     print(fname,"is in our sysem:")
#     lcount=wcount=ccount=0
#     f=open(fname,"r")
#     for line in f:
#         lcount =lcount+1
#         no_of_words= len(line.split())
#         wcount=wcount+no_of_words
#         no_of_character=len(line)
#         ccount=ccount+no_of_character
       

    
# else:
#     print("file soes not exit")
#     sys.exit(0)

# print("NUmber of lines:",lcount)
# print("Number of words:", wcount)
# print("Number of character:", ccount)