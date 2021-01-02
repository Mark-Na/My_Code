nums = [1,2,3]
print([x*10 for x in nums])
print([x/2 for x in nums])
# __for__in___
numbers = [1,2,3,4,5,6]
doubled_numbers = []
#long way
# for num in numbers:
#     doubled_number = num*2
#     doubled_numbers.append(doubled_number)
# print(doubled_numbers)

#shorter
doubled_numbers = [num * 2 for num in numbers]
print(doubled_numbers)

words = ["hello", "hi"]
print([word[0].upper() + word[1:] for word in words])

print([num*10 for num in range(1,6)])
print([bool(val) for val in [0, [], '']])
string_list = [str(num) for num in nums]
print(string_list)

evens = [num for num in numbers if num%2 == 0]
print(evens)
odds = [num for num in numbers if num%2 != 0]
print(odds)

print([num*2 if num%2 ==0 else num/2 for num in numbers])

with_vowels = "This is so much fun!"
print(''.join(char for char in with_vowels if char not in "aeiou"))

#nested lists
nested_list= [[1,2,3],[4,5,6],[7,8,9]]
print(len(nested_list))
print(nested_list[-1])

for l in nested_list:
    for val in l:
        print(val)

board = [[num for num in range(1,4)]for val in range(1,4)]
print(board)
print([["X" if num % 2 != 0 else "O" for num in range(1,4)]for val in range(1,4)])
print([["*"for i in range(1,4)]for x in range(1,4)])

