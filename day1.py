# meaning = 42 
# print("")
# # if meaning > 10:
# #     print("right on")
# # else:
# #     print("not today")

# #this is a ternary operator
# print("right on") if meaning > 10 else print("not today")


# #string data type

# #literal assignment
first = "name"
last = "last name"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))


#constructor fucntion
# pizza = str ("pepporani")
# print(type(pizza))
# print(type(pizza)== str)
# print(isinstance(pizza, str))

# #Concatenation
# fullname = first + " " + last
# print(fullname)
# fullname += "!"
# print(fullname)


# #casting a number into a string
# decade = str(1999)
# print(type(decade))
# print(decade)

# statement = "i like the raps from " + decade + "!"
# print(statement)

#multiple lines

# multiline="""
# Hey, How are you chibi chan?
# All good Chibi chan 
#    Hehe   I hope you are doing well Chibi chan

# """
# print(multiline)

#escpaing special characters
# sentence =  'I\'m a string with an apostrophe'
# print(sentence)

#String Methods

# first = "Chibi Chan"
# print(first)
# print(first.lower())
# print(first.upper())
# print(first)

# multiline = """Hey, How are you chibi chan?
# All good Chibi chan
#  k gardei xau hmm?"""

# # print(multiline.title())
# # print(multiline.replace("chibi chan", "chibi chan is the best"))
# # print(multiline)

# print(len(multiline))

# multiline +="                                            "
# multiline = "                "+ multiline
# print(len(multiline))
# print(len(multiline.strip()))
# print(len(multiline.lstrip()))
# print(len(multiline.rstrip()))


#build a menu
title = "menu".upper()
print(title.center(20,"="))
print("Coffee".ljust(16,".") + "$2.50".rjust(4))
print("CheeseCake".ljust(16,".") + "$5.50".rjust(4))
print("Muffin".ljust(16,".") + "$6.50".rjust(4))

