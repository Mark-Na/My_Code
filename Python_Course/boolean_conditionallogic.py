# if condition is True:
    #do something
#elif some other condition is True:
    # do something
#else:
    #do something
name = "Jon Snow"
if name == "Arya Stark":
    print("Valar Morghulis")
elif name == "Jon Snow":
    print("You know nothing")
else:
    print("Carry on")

# x=1
# x is 1 #True, truthy
# x is 0 #False, falsy
#natural false, empty strings, None, 0, empty objects

animal = input("Enter your favourite animal: ")
if animal:
    print(animal + " is my favourite too")
else:
    print("YOU DIDN\'T SAY ANYTHING")
# == truthy if a has same value of b
# != truthy if a does not have same value as b
# > truthy if a greater than b
# < truth if a is less than b
# >= truthy if a is greater than or equal to b
# <= truthy if a is less than or equal to b
# and truthy if both a and b are true
# or truthy if either a or b are true
# not truthy if the opposite of a is true

#is vs ==
# not the same
# a = [1,2,3]
# b = [1,2,3]
# a == b # returns true, checks the value
# a is b #checks to see if they are placed in same memory

