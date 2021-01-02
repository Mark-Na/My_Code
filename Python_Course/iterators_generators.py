#iterators vs iterables
#iterator: an object to be iterated upon. An object which returns data, one element at a time when next() is called on it
# iterable- An object which will return an iterator when iter() is called on it
#"Hello" is an iterable not iterator. iter("Hello") returns an iterator

#custom for loop
# for num in [1,2,3]
# for num in "hi there"
def my_for(iterable,func):
    iterator = iter(iterable)
    while True:
        try:
           thing = (next(iterator))
        except StopIteration:
            break
        else:
            func(thing)
def square(x):
    print(x*x)
my_for("lol",print)
my_for([1,2,3,4,5],square)

#custom iterators
class Counter:
    def __init__(self,low,high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.high:
            num = self.current
            self.current+=1
            return num
        raise StopIteration


c = Counter(0,10)
iter(c)
for n in Counter(0,10):
    print(n)

#generators are iterators
# can be created using generator expressions
# uses yield instead of return, and can yield multiple times
# generators return a generator

def count_up_to(max):
    count = 1
    while count <=max:
        yield count
        count += 1
counter = count_up_to(5)
print(counter)
print(next(counter))
for num in counter:
    print(num)

# def current_beat():
#     max = 100
#     nums = (1,2,3,4)
#     i = 0
#     result = []
#     while len(result) < max:
#         if i>= len(nums): i = 0
#         result.append(nums[i])
#         i+=1
#     return result
# print(current_beat())

def current_beat():
    nums = (1,2,3,4)
    i = 0
    while True:
        if i >= len(nums): i=0
        yield nums[i]
        i += 1

counter = current_beat()
print(next(counter))

# def nums():
#     for num in range (1,10):
#         yield num
# g = nums()
# g = (num fo rnum in range(1,10))

