class User :
    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users"

    @classmethod
    def from_string(cls,data_str):
        first,last,age = data_str.split(",")
        return cls(first,last,int(age))


    def __init__(self,first,last,age):
       self.first = first
       self.last = last
       self.age = age
       User.active_users += 1
    
    def __repr__(self):
        return f"{self.first} is {self.age}"
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

# user1 = User("Joe","Smith",68)
# user2 = User("Blanca","Lopez",41)
# print(User.display_active_users())
# user3 = User("Joe","Smith",68)
# user4 = User("Blanca","Lopez",41)
# print(User.display_active_users())



class Moderator(User):
    total_mods = 0

    def __init__(self,first,last,age,community):
        super().__init__(first,last,age)
        self.community=community
        Moderator.total_mods +=1
    
    @classmethod
    def display_active_mods(cls):
        return f"There are currently {cls.total_mods} active mods"

    def remove_post(self):
        return f"{self.full_name()} removed a post from {self.community} community"

jasmine = Moderator("Jasmine","O'Connor",61,"piano")
print(jasmine.full_name())
print(jasmine.community)
tom = User.from_string("Tom,Jones,90")
print(tom)

j = User("judy","steele",18)
print(j)
print(User.display_active_users())
print(Moderator.display_active_mods())

#multiple inheritance, if u have the same method in them, it ewill take the one you used first in the multiple inheritance statement, to have it all run,
# name of inheritance.__init__(self,name=name)

#Method resolution order, when you create  a class you have an order in which python wulll look for methods on instances of that class
# __mro__, mro() method on the class, help(class name)
#
