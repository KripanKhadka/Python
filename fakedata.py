from random import *
alphabets="abcdefghijklmnopqrstuvwxyz"
digits="0123456789"
cities=["Kathmandu","Pokhara","Heatauda","Kavre","Nuwakot","Dolakha","Biratnagar"]
designation=["SOftware Engineer","Sr. Software Engineer","TEam Lead","Project Lead","Manager"]

def get_fake_name():
    name = choice(alphabets).upper()
    n = randint(2,9)
    for i in range(n):
        name=name+choice(alphabets)
    return name

# print(get_fake_name())

def get_fake_num():
    enum="e-"
    for i  in range(4):
        enum=enum+choice(digits)
    return enum
# print(get_fake_num())

def get_fake_salary():
    esal=uniform(10000,50000)
    return esal
# print(get_fake_salary())

def get_fake_city():
    city=choice(cities)
    return city
# print(get_fake_city())


def get_fake_mno():
    mno=choice("9")
    for i in range(9):
        mno=mno+choice(digits)
    return mno
# print(get_fake_mno())

def get_fake_designation():
    desig=choice(designation)
    return desig
# print(get_fake_designation())

print("Employee Records")
for  i in range(10):
    print("Name of employee:",get_fake_name())
    print("Number of employee:",get_fake_num())
    print("Salary of employee:{:.2f}".format(get_fake_salary()))
    print("Mob No of employee:",get_fake_mno())
    print("City of employee:",get_fake_city())
    print("Designation of employee:",get_fake_designation())
    print()
    print()

