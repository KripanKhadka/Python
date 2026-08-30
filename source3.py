# #BANK SYSTEM
# import sys
# class Customer:
#     """This is Bank System"""
#     bank_name="ACEM"
#     def __init__(self,name,balance=0.0):
#         self.name=name
#         self.balance=balance


#     def deposit(self,amount):
#         self.balance=self.balance+amount
#         print("New balance after deposit is:",self.balance)

#     def withdraw(self,amount):
#         if amount> self.balance:
#             print("Insufficient find. Please Deposit Firse")
#             sys.exit()
#         else:
#             self.balance=self.balance-amount
#             print("Balance after winthdraw:", self.balance)

# print()
# print("#"*50)
# print("Welcome to ACEM bank")
# print("#"*50)
# name=input("Please enter your name: ")
# c=Customer(name)
# while True:
#     print("d-deposit \n w-withdraw \n e-exit")
#     option =input("Enter your option: ")
#     if option=="d" or option =="D":
#         amount = float(input("Enter your amount to deposit : "))
#         c.deposit(amount)
#     elif option =="w" or option=="w":
#         amount = float(input("Enter your amount to withdraw : "))
#         c.withdraw(amount)
#     elif option == "e" or option=="E":
#         print("Thank you for using our services")
#         sys.exit()
#     else:
#         print("Invalid Option. Please choose valid option")
    