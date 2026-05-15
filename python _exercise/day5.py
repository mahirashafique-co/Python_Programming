# Functions in Python are reusable code blocks designed to perform specific tasks.
# A function executes only when it is invoked.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

def welcome():
    print("Welcome to python")
welcome()
welcome()
welcome()

#arguments
def newfun(name):
   print("hello" ,name)
newfun("mahira")
newfun("shafique")


def info(firstname,lastname):
    print("your fullname is",firstname,lastname)

info("mahira","shafique")


# *arbitrary arguments
def fruits(*fruits):
    print(fruits[0],fruits[1],fruits[2],fruits[3])
fruits("apple","banana","guava","pineapple")

# keywords arguments
def keywordsarg(val1,val2,val3):
    print("the final value is",val3)
keywordsarg(val1="mahira",val2="shafique",val3="pineapple")



# ** arbitrary keyword arguments
def arbkey(**details):
    print("your first name is",details["firstname"])
    print("your last name is",details["lastname"])
    print("your age is",details["age"])
arbkey(firstname="mahira",lastname="QA",age="3")

#default value

def country(country="Norway"):
    print("your country is",country)
country("mahira")
country()

#return
def value(a,b):
 result=(a+b)
 print("value is",result)

value(8,1)