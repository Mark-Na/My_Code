x=100
y=101
print(float(x+y))
z = x+y
all,at,once = 1,2,3
print(all)
z = z-1
# naming restrictions:
# 1. variables must start with letter or underscore
# 2. rest of name must consist of letters numbers or underscores
# 3. names are case-sensitive CATS != Cats
# naming conventions:
# snake_case, underscores between words
# or camelCase but snake_case better
# most variables should be with some exceptions CAPITAL_SNAKE_CASE usually refers to constants
# UpperCamelCase usually refers to classes
# double underscore are private or left alone __no_touchy__

# data types
# bool True or False values
# int integers
# str strings, sequence of unicode characters
# list ordered sequence of values of other data types [1,2,3] or ["a", "b","c"]
# dict collection of key values eg {"first_name":"Colt","last_name":"Steele"}
True
989
some_string = "Hello I am a string"
# dynamic typing where variables can be reassigned to different types very easily
a = True
print(a)
a = 4
print(a)
a = "Hi"
print(a)
a = None
print(a)
# None value
# represents null/nothingness
type(None)
# Strings can be in single or double quotes but be consistent
msg = "he said 'hello there ' "
print(msg)
msg2 = 'I am "funny"'
#String Escape Characters
new_line = "hello \nworld!"
#\n = new line
str1 = "this is a backslash: \\"
print(str1)
str1 = "hel\blo"
print(str1)
str1 = "he said \"ha ha\" "
print(str1)
# same with single quotes
mountains = "/\\/\\/\\"
# String concatenation
username = "bluethecat"
print("Hello there and welcome to the game," + username)
"a" + "b" + "z"
name = "colt"
name += "steele"
print(name)
people = 99
people +=1
print(people)
str_one = "your"
str_two = "face"
str_three = str_one + " " + str_two
# formatting strings
x = 10
formatted = f"I've told you {x} times already!"
print(formatted)
formatted = f"I've told you {x*5} times already!"
print(formatted)
#use .format method in udemy exercises
fruit = "apple"
ripeness = "ripe"
print("The {} is {}".format(fruit,ripeness))
#strings and indices
name = "Chuck"
print(name[0])
print(name[-3])
decimal = 12.3424213123123132
integer = int(decimal)
my_list = [1,2,3]
my_list_string = str(my_list)
print(my_list_string)
num = 12
print(type(num))
num = float(num)
print(type(num))
