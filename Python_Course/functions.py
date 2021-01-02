#function is a process for executing a task
# def sing_happy_birthday(name):
#     print("Happy Birthday To You")
#     print("Happy Birthday To You")
#     print(f"Happy Birthday Dear {name}")
#     print("Happy Birthday To You")

# sing_happy_birthday('bob')
# sing_happy_birthday('bob')
# sing_happy_birthday('bob')
# sing_happy_birthday('bob')

nums = [1,2,3,4]
length = len(nums)
last_item = nums.pop()

def square_of_7():
    return 7**2
result = square_of_7()
print(result)

#return exits the function

def generate_evens():
    return[x for x in range(1,50) if x % 2 == 0]

def square(num):
    return num**2
print(square(5))

def add(a,b):
    return a+b
#parameter is a variable in a method definition
# when method is called, the argument is the data that is passed into the method's parameters
# parameter is var in the declaration of function
# argument is actual var of this var that is passed to a function

def divide(num1,num2):
    return num1/num2

def sum_odd_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
    return total
print(sum_odd_numbers([1,2,3,4,5,6,7,8,9]))

def is_odd_number(num):
    if num%2 != 0:
        return True
    return False
print(is_odd_number(2))

def exponent(num,power=2): #if power not specified, will automatically default to 2
    return num ** power

print(exponent(2))
print(exponent(5,3))

def subtract(a,b):
    return a-b

def math(a,b,fn = add):
    return fn(a,b)

print(math(2,2,subtract))

def full_name(first,last):
    return f"Your name is {first} {last}"

print(full_name(first = 'colt', last = 'steele'))
print(full_name(last = 'steele', first = 'colt'))
print(exponent(power =5,num =3))

def say_hello():
    instructor = 'colt'
    return f'Hi {instructor}'
print(say_hello())
# print(instructor) error as instructor is only available inside that function
# cannot change global variables inside a function, assumes local var alrdy initialized

# this is how to use the global variables in the function
# total = 0
# def increment():
#     global total 
#     total += 1 
#     return total

#nonlocal: allows to modify parent's variables in a child ( nested ) function

# def outer():
#     count = 0
#     def inner():
#         nonlocal countcount += 1
#         return count
#     return inner()]

# documenting functions use """ """
# def say_hello():
#     """A simple function that returns the string hello"""
#     return "Hello!"
# print(say_hello.__doc__)
# print(print.__doc__)

#def return_day(num):
    # try:
    #     return["Sunday","monday",...]
    # except IndexError as e:
    #     return None

# def last_element(l):
#     if l:
#         return l[-1]
#     return None

def single_letter_count(string,letter):
    return string.lower().count(letter.lower())

def multiple_letter_count(string):
    return {letter: string.count(letter) for letter in string}

list1 = [1,2,3,4]
list2 = list1
print(list2)

string = "hi my name is bob"
l = list(string)
print((l))
print(len(l))
while l.__contains__(' '):
    l.remove(' ')
print(l)
check = ""
for i in range(len(l)):
    check+=l[i]
print(check)


def is_palindrome(string):
    return string == string[::-1]

def is_palindrome2(string):
    stripped = string.replace(" ","")
    return stripped == stripped[::-1]

def compact(l):
    return [val for val in l if val]

def intersection(l1,l2):
    return [val for val in l1 if val in l2]

    
def intersection2(l1,l2):
    return [val for val in set(l1) and set(l2)]

def partition(l,fn):
    return[[val for val in l if fn(val)],[val for val in l if not fn(val)]]

# use the * and ** operators as parameters to a function and outside a function
# leverage dictionary and tuple unpacking 

# * args, special operater that gathers remaining arguments as a tuple, just a parameter
def sum_all_nums(num1,num2,num3):
    return num1 + num2 + num3

def sum_all_nums2(*nums):
    total = 0
    for num in nums:
        total += num
    return total
print(sum_all_nums2(4,6)) 

def ensure_correct_info(*args):
    if "Colt" in args and "Steele" in args:
        return "Welcome back Colt"
    return "Not sure who you are"
print(ensure_correct_info())
print(ensure_correct_info("hello",False,78,'Colt',5.4444,'Steele'))

#**kwargs - keyword args
#store the remaining keyword arguments as a dictionary
def fave_colours(**kwargs):
    for person,color in kwargs.items():
        print(f"{person}'s favourite color is {color}")
print(fave_colours(colt = 'purple', ruby = 'red',ethel = 'teal'))

def special_greeting(**kwargs):
    if "David" in kwargs and kwargs["David"] == "special":
        return "You get a special greeting David"
    elif "David" in kwargs:
        return f"{kwargs['David']} David!"
    return "Not sure who this is..."

# parameter ordering:
# parameters , *args , default parameters , **kwargs
def display_info(a,b,*args,instructor = 'Colt', **kwargs):
    return [a,b,args,instructor,kwargs]
print(display_info(1,2,3,last_name = 'Steele', job = 'Instructor'))

# tuple unpacking 
# can use * as an argument to a function to unpack values

def sum_all_nums3(*args):
    total = 0
    for num in args:
        total += num
    print(total)

nums1 = (1,2,3,4,5,6)
nums2 = [1,2,3,4,5,6]
sum_all_nums3(*nums1) # only works with the *

# dictionary unpack using **
def display_names(first,second):
    print(f"{first} says hello to {second}")
names = {"first":"Colt","second":"Rusty"}
display_names(**names)

def add_and_multiply(a,b,c,**kwargs):
    print(a + b * c)
data = dict(a=1,b=2,c=3,d=6,name = 'Tony',cat='Blue')
add_and_multiply(**data)
