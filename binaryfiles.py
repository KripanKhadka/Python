# with  open("img.jpeg","rb") as f1:
#     f2=open("newimg.jpeg","wb")
#     a=f1.read()
#     f2.write(a)
# print("I hope image is copied")
 

#handling csv files (comma separeted files):


# import csv
# with open("emp.csv","w",newline="") as f:
#     w=csv.writer(f)# it writes in csv files
#     # print(type(w))
#     w.writerow(["e-num","e-name","e-saary","e-address"])
#     n=int(input("enter thenumber of emplyess"))
#     for i in range(n):
#         en=int(input("enter employee num: "))
#         ename=input("enter employee ename: ")
#         esalary=int(input("enter employee esalary: "))
#         eaddress=input("enter employee eaddress: ")
#         w.writerow([en,ename,esalary,eaddress])
# print("our file is created")

# import csv
# with open("emp.csv","r")as f1:
#     w=csv.reader(f1)
#     data=list(w)
#     for line in data:
#         for word in line:
#             print(word,"\t",end="")
#         print()
    