#lambdas:
def square(num): return num*num
square2 = lambda num: num * num
# lambda can only be one line anopnymous functions
#usually won't put lambda in a variable
add = lambda a,b: a+b
print(square.__name__)
print(square2.__name__)
print(add.__name__)

#map requires function usually lambda and an iterable and returns a collection with the new version
nums =[2,4,6,8,10]
doubles = list(map(lambda x: x*2,nums))
print(doubles)

people = ["Bob","Bleb","Carm"]
peeps = list(map(lambda name: name.upper(),people))
print(peeps)

#filter, lambda for each value in iterable
# returns filter object that can be converted into other iterables
# object contains only the values that return true to the lambda

l = [1,2,3,4]
evens = list(filter(lambda x: x%2 ==0,l))
print(evens)
a_names = list(filter(lambda n: n[0]=='B',people))
print(a_names)

print(list(map(lambda name : f"Your instructor is {name}",filter(lambda value: len(value)<5,people))))
# [f"Your instructor is {name}" for name in names if len(name)<5]

#Any and All
# all: returns true if all elements of the iterable are truthy or if empty
# any returs true if any element of the iterable is truthy. if empty return false
#generator expressions sys.getsizeof
# if only iterating once, use generator, use list comprehension else
# generator expression is list comprehension with () instead of []
#all([if num % 2 == 0 for num in numbers])
# sorted: returns new sorted list from items in iterable but does not change the actual iterable
# sorted can accept tuples
# can reverse it too sorted(numbers,reverse = True)
# for dictionaries : sorted(users,key = len)
# sorted(users,key = lambda user: user['username'])
# sorted(users,key = lambda user: len(user['tweets']),reverse = True)
# sorted(songs,key = lambda s: s['playcount'],reverse = True)

#max: returns the largest item in an iterable of two or more arguments
max(3,67,99) #99
max('c','d','a') #d
#max(list)
#min(list)
#max(string) gives largest char value
#max(tuple)
# if wanted to find shortest length name in a list min(len(name) for name in names)
# to return the actual name need lambda: max(names,key = lambda n: len(n))
# min(songs,key = lambda s: s['playcount'])['title']

#reversed: returns reversed iterator
# if put in a list , must list(reversed(list)) or use list.reverse() instead
# can iterate over reversed(list)
# and can reverse strings as well or use slices
# ''.join(list(reversed("hello")))
# use reversed to iterate over something, like for x in reversed(range(0,10)):

#len() and OOP a little bit
#__len__() like hello.__len__()
# will probably never call this manually but len() does that 

#abs() returns absolute value of a number, argument is int or float
#math.fabs is float absolute value
#sum() takes iterable and optional start and returns the sum of start and goes from left to right sum([1,2,3],-6) will lso add the argument after the comma
# math.fsum() is a better sum
# round(), rounds to nearest integer if specific digits not specified, None also means round to nearest integer
#zip(), makes an iterator that aggregates elements from iterables, returns iterator of tuples where ith tuple contains ith element from each argument sequences or iterables
# iterator stops when shortest input iterable is exhausted

first_zip = zip([1,2,3],[4,5,6])
print(list(first_zip))
print(dict(first_zip))
#if uneven lists trying to zip, it will just limit when you hit the last pair
# can use the * operator to unpack it
five_by_two = [(0,1),(1,2),(2,3),(3,4),(4,5)]
print(list(zip(*five_by_two)))

midterms = [80,91,78]
finals = [98,89,53]
students = ['dan','ang','kate']

final_grades = {t[0] : max(t[1],t[2]) for t in zip(students,midterms,finals)}
print(final_grades)

scores = zip(students,map(
    lambda pair: max(pair),
    zip(midterms,finals)
))
print(dict(scores))

avg_scores = zip(students,map(
    lambda pair: (pair[0]+pair[1])/2,
    zip(midterms,finals)
))

print(dict(avg_scores))

def interleave(str1,str2):
    return ''.join(''.join(x)for x in zip(str1,str2))