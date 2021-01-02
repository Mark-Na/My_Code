#data structure that consists of key value pairs
#use the keys to describe data and 
instructor = {
    "name":"Colt",
    "owns_dog":True,
    "favourite_language":"Python",
    #"is_hilarious":False,
    44 : "my favourite number!"
}


cat = {"name": "Blue", "age":3.5, "isCute":True}
print(cat)
cat2 = dict(name = "kitty",age = 0.5)
print(cat2)
print(cat["name"])
print(cat2["age"])
#iterating over dictionaries:
for value in instructor.values():
    print(value)

for v in instructor.keys():
    print(v)

print(instructor.items())

for k,v in instructor.items():
    print(f"key is '{k}' and value is '{v}'")

#shortcut total_donations = sum(donation.values()) or sum(donation for donation in donations.values())
print("name" in instructor)
print("address" in instructor)
print("name" in instructor.values())

#clear empties out the dictionary
# name_of_dict.clear()
# copy makes copy of the dictionary name_of_other_dict = name_of_dict.copy()
# fromkeys creates key-value pairs from comma seperated values
new_user = {}.fromkeys([])
new_user = {}.fromkeys(['name','score','email', 'profile bio'],'unknown')
print(new_user)
print(new_user.fromkeys(['phone'],'unknown'))
print(new_user.fromkeys('phone','unknown'))
# get retrieves a key in an object and return None instead of keyError if key doesnt exist
print(instructor.get('name'))
print(instructor.get('email'))

# "{} left".format(bakery_stock[food])
# dict.fromkeys(name_of_dict, value_to_all_be_set_too)
# pop takes single argument corresponding to a key and removes that key-value pair from the dictionary and returns value coresponding to key that was removed
# key error if removed non existent key
print(instructor.pop("owns_dog"))
# popitem() removes random key from dictionary
print(instructor.popitem())
# update, updates keys and values in dictionary with another set of key value pairs
print(instructor)
person = {"city":"Antigua"}
person.update(instructor)
print(person)
person['name'] = 'Evelia'
print(person)
person.update(instructor)
print(person)
# add to dictionary by doing name_of_dict[key] = value

#{__:__for__in__} iterates over keys by default
numbers = dict(first = 1, second = 2, third = 3)
squared_numbers = {key:value**2 for key, value in numbers.items()}
print(squared_numbers)
print({num : num **2 for num in [1,2,3,4,5]})
string1 = "abc"
string2 = "123"
combo = {string1[i]:string2[i] for i in range(0,len(string1))}
# fast way is dict(zip(list1,list2))
print(combo)
yelling = {k.upper():v.upper() for k,v in instructor.items()}
print(yelling)
print({num:("even" if num % 2 == 0 else "odd") for num in range(1,5)})
yelling = {(k.upper() if k is 'name' else k): v.upper() for k,v in instructor.items()}
print(yelling)
#if given var : [[~,~],[~,~],...] turn into dict by doing dict(var) or new_dict = {k:v for k,v in var}
#answer = {char:0 for char in 'aeiou} 
#answer = dict.fromkeys('aeiou',0)
print(''.join(instructor.values()))
