a=777

def hello(a,b):
    print("the sum is:",a+b)



def hi(a,b):
    print("the product is",a*b)
    print("changed")

# print(dir())

# print(__name__) direct execution


# def f():
#     if __name__=="__main__":
#         print("direct execution")
#     else:
#         print("indirect execution")

# f()

def f1():
    print("First execution")

def f2():
    print("Second execution")

def f3():
    print("Third execution")

if __name__=="__main__":
    f1()
    f2()
    f3()


