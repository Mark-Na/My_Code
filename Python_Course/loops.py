# for item in interable_object:
    # do something with item
# iterable_object is some kind of collection of items: list, string, range, etc
# item is new variable that can be anything you want 
# item references the current position of the iterator within the iterable
# it will iterate every item of the collection then go away when it has visited all items

for x in range(1,10):
    print(x)
    print(x*x)

for letter in 'coffee':
    print(letter * 10)

#range(7) goes from 0-6
#range(1,8) goes from 1 to 7
#range(1,10,2) gives odds from 1- 10
#range(7,0,-1) goes down from 7-1
r = range(10)
print(list(r))
nums = range(1,10,2)
print(list(nums))

for num in range(10):
    print(num)

for num2 in range(10,20,2):
    print(num2)

num3 = range(1,5)
print(num3)  

#while loops:
# they continue ot execute while a ceratin condition is truthy and will end when they become falsy
# require more carefule setups as you need to spicify termination conditions manually

# msg = input("whats the secret password ")
# while msg != "bananas":
#     print("WRONG")
#     msg = input("whats the secret password ")
# print("correct")

# break allows us to leave any loop whenever we want
# 