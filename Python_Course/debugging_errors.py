#common errors:
# SyntaxError: occurs when python encounters incorrect syntax
# ex: due to typos or not knowing python well enough

#NameError when a variable is not defined, hasnt been assigned yet
#TypeError: operation or function is apploed to wrong type
# len(5) or 3+'s' or len(2.4) or 'awesome' + []
#IndexError when you tyr to access an element in a list using an invalid index(outside the range of the list or string)
#ValueError occurs when built-in operation or function receives an argument that has the right type but an inappropriate 
#ex :int('foo')
#KeyError when dictionary does not have specified key ex: d = {} d['foo']
#AttributeError when variable does not have an attribute
# ex: 'awesome'.foo, [1,2,3].hello()

#Raise own exceptions
# raise ValueError('invalid value')

def colorize(text,color):
    colors = ['blue','green','yellow']
    if type(text) is not str:
        raise TypeError ("Text must be instance of str")
    if color not in colors:
        raise ValueError("color is invalid color")
    print(f"Printed {text} in {color}")

#try and except
# try:
#     foobar
# except NameError as err:
#     print(err)

# try:
#     foobar
# except:
#     print('Problem')
#print("after the try")

# try:
#     colt
# except NameError:
#     print("you tried to use a variable that was never declared")

d = {"name":"Ricky"}


def get(d,key):
    try:
        d[key]
    except KeyError:
        return None
print(get(d,'name'))
print(get(d,'city'))

#Else and FInally
# while True:
#     try:
#         num = int(input("please enter a number: "))
#     except ValueError:
#         print('that\'s not a number')
#     else:#runs if except does not
#         print("I'm in the else")
#         break
#     finally:#always runs
#         print("RUNS NO MATTER WHAT")

def divide(a,b):
    try:
        result= a/b
    except ZeroDivisionError:
        print("please don't divide by zero")
    except TypeError as err:
        print("a and b must be ints or floats")
        print(err)
    else:
        print(f"{a} divided by {b} is {result}")

print(divide(1,2))
print(divide(1,0))

def divide2(a,b):
    try:
        result= a/b
    except (ZeroDivisionError, TypeError) as err:
        print("something went wrong")
        print(err)
    else:
        print(f"{a} divided by {b} is {result}")

print(divide2(1,2))
print(divide2(1,0))

#debugging with pdb
# import pdb;pdb.set_trace()
# common commands: l(list) to see where u are
# q to quit
# p print
# c continue
# n next line
# have to p var to print variable
# a shows all arguments values