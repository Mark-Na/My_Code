def sum(n,func):
    total = 0
    for num in range(1,n+1):
        total += func(num)
    return total

def square(x):
    return x*x
print(sum(10,square))

from random import choice

# def greet(person):
#     def get_mood():
#         msg = choice(('Hello there ','Go away ','I love you '))
#         return msg
#     result = get_mood() + person
#     return result
# print(greet("Toby"))

# def make_laugh_func(fn):
#     def get_laugh():
#         laugh = choice(('HAHAHAHAHAH','lol','teehee'))
#         fn()
#         return f"{laugh}"
#     return get_laugh

# @make_laugh_func
# def greets():
#     print('my name Bob')

# print(greets())


# def shout(fn):
#     def wrapper(name):
#         return fn(name).upper()
#     return wrapper

def shout(fn):
    def wrapper(*args,**kwargs):
        return fn(*args,**kwargs).upper()
    return wrapper
@shout
def greet(name):
    return f"Hi I'm {name}"

@shout
def order(main,side):
    return f"Hi, I'd like the {main} with a side of {side} please"

print(greet('Todd'))
print(order('burger','fries'))

#from functools import wraps
#preserves the metadata like the docstring of the function so that it does not get lost in the wrapper function

#speed-test decorator
from functools import wraps

def ensure_first_arg_is(val):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args,**kwargs):
            if args and args[0]!= val:
                return f"First arg needs to be {val}"
            else:
                return fn(*args,**kwargs)
        return wrapper
    return inner

@ensure_first_arg_is("burrito")
def fav_foods(*foods):
    print(foods)
print(fav_foods("burrito","ice cream"))
print(fav_foods("ice cream","burrito"))

@ensure_first_arg_is(10)
def add_to_ten(num1,num2):
    return num1 + num2

print(add_to_ten(10,12))
print(add_to_ten(1,10))

def enforce(*types):
    def decorator(f):
        def new_func(*args,**kwargs):
            new_args = []
            for (a,t) in zip(args,types):
                new_args.append(t(a))
            return f(*new_args,**kwargs)
        return new_func
    return decorator

@enforce(str,int)
def repeat_msg(msg,times):
    for time in range(times):
        print(msg)

repeat_msg("hello",3)

@enforce(float,float)
def divide(a,b):
    print(a/b)

divide(1,2)
divide('1','4')