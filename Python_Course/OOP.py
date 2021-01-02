#classes and object
# class is a blueprint for objects, can contain methods and attributes
# instance : onjects that are constructed from the blueprint that contain the class methods and properties

#abstraction and encapsulation
# goal is to encapsulate code into logical hierarchical groupings using classes

# Deck {class}

# _cards {private list attribute}
# _max_cards {private int attribute}
# shuffle {public method}
# deal_card {public method}
# deal_hand {public method}
# count {public method}

# encapsulation: grouping of public and private attributes and methods into programmatic class
# abstraction: exposing only relevant data in a class interface, hiding provate attribute and methods from the users

class User :
    active_users = 0
    def __init__(self,first,last,age):
       self.first = first
       self.last = last
       self.age = age
       User.active_users += 1
    
    def logout(self):
        User.active_users -= 1
        return f"{self.first} has logged out"
    
    def full_name(self):
        return f"{self.first}  {self.last}"
    
    def initias(self):
        return f"{self.first[0]}.{self.last[0]}."
    def likes(self,thing):
        return f"{self.first} likes {thing}"
    def is_senior(self):
        return self.age>=65
    def birthday(self):
        self.age +=1
        return  f"Happy {self.age}th, {self.full_name()}"

user1 = User("Joe","Smith",68)
user2 = User("Blanca","Lopez",41)
print(user1.first,user1.last,user1.age)
print(user1.birthday())
#self refers to current class instance
# self must always be first parameter to __init__ and any methods and properties on class instances

class Person:
    def __init__(self):
        self.name = "Tony"
        self._secret = "hi!" # only accessed by programmer
        self.__msg = "I LIKE TURTLES"
        self.__lol = "HAHAHAH"
    #def doorman(self,guess):
       # if guess == self._secret:
            #let them in

        
p = Person()
print(p.name)
print(p._secret)
#print(p.__msg) # cannot access this
print(p._Person__msg)
print(p._Person__lol)
#__ before a variable and not after does something

#instance attributes and methods

#class attribute is directly on a class that are shared by all instances of a class and the class itself
#class methods are methods that are not concerned with instances but the class itself
# use @classmethod

#__repr__ method
#inheritance and Objectives:
#inherits from another class (base or parent class)
#

class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species
    
    def __repr__(self):
        return f"{self.name} is a {self.species}"

    def make_sound(self,sound):
        print(f"this animal says {sound}")

class Cat(Animal):#inherits animals
    def __init__(self,name,species,breed,toy):
        super().__init__(name,species)
        self.breed = breed
        self.toy = toy

    def play(self):
        print(f"{self.name} plays with {self.toy}")

# blue = Cat()
# blue.make_sound('meow')
# print(blue.cool)
# print(Cat.cool)
# print(Animal.cool)
# print(isinstance(blue,Animal))

blue = Cat("Blue","Cat","Scottish Fold", "String")
print(blue)
blue.play()
#properties:
class Human:
    def __init__(self,first,last, age):
        self.first = first
        self.last = last
        if age >= 0:
            self._age = age
        else:
            self._age = 0
    # def getAge(self):
    #     return self._age
    # def setAge(self,new_age):
    #     if new_age >= 0:
    #         self._age = new_age
    #     else:
    #         self._age = 0 
    @property#decorator
    def age(self):
        return self._age
    @age.setter
    def age(self,value):
        if value>=0:
            self._age=value
        else:
            raise ValueError("Age cannot be negative")
    @property
    def full_name(self):
        return f"{self.first} {self.last}"
    
    @full_name.setter
    def full_name(self,name):
        self.first,self.last = name.split(" ")

# jane = Human("Jane","Goodall",-10)
# # print(jane.getAge())
# print(jane.age)
# jane.age = 20
# print(jane.age)
# print(jane.full_name)
# jane.full_name = "Tim Bob"
# print(jane.full_name)
# print(jane.__dict__)

#Polymorphism
# object that can take on many forms
# the same class method works in a similar way for different classes 
# ex: animal.speak(), dog.speak()
# the same operation works for different kinds of objects: len(list) len(tuple) len(string)

#1. the same class method works in a similar way for diff classes. Ex a method in a base class overidden by subclass
#2. 8+2 = 10, '8'+'2'= '82' called a special method and works bc it uses __add__() method

#magic methods:
# 

