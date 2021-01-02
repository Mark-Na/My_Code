# tuple is an ordered collection or grouping of items like a list 
numbers = (1,2,3,4)
#it is immutable, cannot be changed unlike lists
x = (1,2,3)
3 in x 
# x[0] = 313 get errors
# faster than lists
# makes code safer from bugs and problems
# they are valid keys in dictionaries
# ex of tuples, months of the year cuz they will never change and same order
# create using () or the tuple function
# can access data from tuples using []
locations = {
    (35.6895,39.6917): "Tokyo Office",
    (40.7128,74.0060): "New York Office",
    (37.7749,122.4194):"San Francisco Office"
}
print(locations)
#some dictionary methods like .items return tuples
cat = {'name':'biscuit','age':0.5,'favourite_toy':'my chapstick'}
print(cat.items())
# can use for loop to iterate over tuple
for num in numbers:
    print(num)

i = len(numbers)-1
while i>= 0:
    print(numbers[i])
    i-=1
# tuple methods: count returns number of times a value appears in a tuple, tuple.count(x)
# index returns the index at which a value is found in a tuple, tuple.index(x)
# can hae nested tuples
num2 = (1,2,3,(4,5),6,7)
num2[3]
# can slice tuples
# tuple of one element : value = (1,) or tuple([1])

# Sets:
# are like formal mathematical sets
# dnt have duplicate values
# not ordered 
#cannot access items in a set by index
# useful for keeping track of collection of elements but dont care about keys or vals or duplicates

s = set({1,2,3,4,5,5,5})
print(s)
s = set({1,4,5})
4 in s
8 in s
s = set({1,2,4,'a',3.3333})
print(s)
for number in s:
    print(number)

# Set methods:
# add: adds an element to a set, if the element is alrdy in the set, the set just doesn't change set.add(x)
# remove: removes value from set if in it, else it returns an error set.remove(x)
# discard: just does not through key errors like remove, set.remove(x)
# copy, creates copy of set: another_s = set.copy()
# clear, removes all contents of the set
# Set Math:
# intersection: returns the value thats in both sets:  set1 & set2
#symmetric difference:
#union: combines two sets : set1 | set1

#set comprehension:
{x**2 for x in range(10)}

def are_all_vowels_in_string(string):
    return len({char for char in string if char in 'aeiou'}) == 5

print({char.upper() for char in 'hello'})
hi = 'hello'
print({char for char in hi if char in 'aeiou'})
print(are_all_vowels_in_string(hi))