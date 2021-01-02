# collection or grouping of items
# can store other lists in it as well
tasks = ["Install Python", "Learn Python", "Take a Break"]
demo_list = [ "a", 1, 45, True, 6.777]
print(len(demo_list))
r = range(1,10)
r = list(r)
print(r)
friends = ["Ashley","Matt","Michael"]
#lists always starts counting at 0
print(friends[0])
print(friends[1])
print(friends[2])
print("Ashley" in friends)
print("Bob" in friends)

colors = ["purple", "teal", "magenta", True, 8.9]
for color in colors:
    print(color)

numbers=[4,6,3,5,7]
for num in numbers:
    print(num**3)

i = 0
while i< len(numbers):
    print(numbers[i])
    i += 1
# list methods:
data = [1,2,3]
#data.____ to apply list methods
# append adds to the end of the list
data.append(4)
#can only append one item at a time
data.append([5,6,7,8])
#extend can add multiple items to the end of the list
data.extend([5,6,7,8])
print(data)
# insert adds a value at designated location
data.insert(len(data),9)
data.insert(2,2.5)
print(data)
x = []
x.append(1)
print(x)
# clear removes all items from list at once
# pop removes the specified item and returns it, if not specified removes the last one
last = data.pop()
print(last)
first = data.pop(0)
print(first)
#remove removes the first item from the list whose value is specified
# index returns the index of the specified item in the list
# can specify start and end
# count accepts single input and returns the number of times the specified appears in the list
# sort sorts the items of the list
# join converts lists to string
# joins the strings in the list together 
words = ["hello", "hi"]
print(",".join(words))
#slices:
# some_list[start:end:step] makes a new list using slices of old list
first_list = [1,2,3,4]
print(first_list[1:])
print(first_list[-2:])
print(first_list[:2])
print(first_list[:-1])
print(first_list[1:4:2])
print(first_list[0:4:2])
print(first_list[::2])
print(first_list[1::-1])
print(words[0][::-1])
words[0],words[1]= words[1],words[0]
print([word[0].upper() + word[1:] for word in words])

