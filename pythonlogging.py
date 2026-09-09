#python logging has given us module logging
#logging levels gives us what importance the messgae is
#CRITICAL=>50(App could be down so it but be handeled asap)
#ERROR=>40(a little less than critical yet still a problem)
#WARNING =>30()
#INFO=> 20()
#DEBUG=>10()
#NOTSET=>0

#logging need-> log fileor console and logging level
#to 
# import logging
# logging.basicConfig(format="%(asctime)s :%(levelname)s : %(name)s :%(message)s",filename="log.txt",level=10,filemode="w",datefmt="%A %B %d/%m/%Y %I:%M:%S %p"  )
# print("this is demo of warning")
# logging.debug("this code is corrected")
# logging.info("this is info information")
# logging.warning("this is warning information")
# logging.error("this is error information")
# logging.critical("this is critical information")

#to know the date and time and day the python has given us the keyword name "format"

#format="%(levelname)s : %(name)s :%(message)s"


# import logging
# logging.basicConfig(format="%(asctime)s :%(levelname)s : %(name)s :%(message)s",filename="log.txt",level=10,filemode="w",datefmt="%A %B %d/%m/%Y %I:%M:%S %p" )
# logging.info("Process Started")
# try: 
#     x=int(input("enter first number: "))
#     y=int(input("enter second number: "))
#     print("the result is :", x/y)
# except ZeroDivisionError as z:
#     print("there is value error. you need to check your log file")
#     logging.exception(z)
# except ValueError as v:
#     print("value error check thelog file")
#     logging.exception(v)
# logging.info("Process Completed")


# import logging
# import logstudent

# logging.basicConfig(format="%(asctime)s :%(levelname)s : %(name)s :%(message)s",filename="log.txt",level=10,filemode="w",datefmt="%A %B %d/%m/%Y %I:%M:%S %p" )
# logging.info("INFO MESSGAE FROM LOgs module")

#Own Logger: logger() handler() formatter()-> its insidea handler and handler is inside -> logger()

import logging 
logger = logging.getLogger("my Logger")
logger.setLevel(logging.DEBUG)
filehandler=logging.FileHandler("Kri.log",mode="w")
formatter=logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
filehandler.setFormatter(formatter)
logger.addHandler(filehandler)
logger.critical("This is criticla")
logger.info("This is info")
logger.warning("This is warninh")
logger.debug("This is debug")
logger.error("This is error")