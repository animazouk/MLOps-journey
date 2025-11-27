#===============================
#OOPs in Python
#===============================
# 1. Instanciating a class

# Dog class : blue print for creating objects
# An object is an insatance of a class
class Dog:
    def __init__(self,name,breed,owner): # runs only once each time when the methode object is instansiated
        self.name = name # Data fields
        self.breed = breed
        self.owner = owner

    def bark(self): 
        print("woof woofg ")


class Owner:
    def __init__(self, name , address, phone_number):
        self.name = name
        self.address = address
        self.phone_number = phone_number


owner1 = Owner("adarsh","wfwfwgeq","9284924820")
dog1 = Dog("paglu","greyhound",owner1)
print(dog1.owner.name)  


# 2. Accessing and modifying Object Data

class User:
    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.password = password
    def say_hi_to_user(self,user):
        print(f"2. Sending message to {user.name} : hi {user.name}, it's {self.name}")
    
user1 = User("adarsh","ada@gmail.com" , "2djwd")
user2 = User("adhya","adha@gmail.com" , "2dnwi")
user3 = User("deepak","dee@gmail.com" , "9chsn")

user1.say_hi_to_user(user2)# accessing data
user1.email = 'adarsh4553@gmail.com'# changing data
print(user1.email)

# 3. access Modification in python
class User:
    def __init__(self,name,email,password):
        self.name = name
        self._email = email # Conventionally treeted as a protected attribute and be accesed within the class deffinition directly.
        self.password = password
    def clean_mail(self):
        print(self._email.lower().strip())
    
user1 = User("adarsh","ada@gmail.com" , "2djwd")
user2 = User("adhya","adha@gmail.com" , "2dnwi")
user3 = User("deepak","dee@gmail.com" , "9chsn")

print(user1._email) # Python dont stop us from doing this but its a convention not to as its marked protected by putting a '_' before itsname.

user1.clean_mail()# right way (acessing a method defined within the class that acesses the protected marked attribute)
# Concenting Adult Philosophy

''' we can force to make an attribute private by putting a '__' before it which makes it 
impossible to be accessed by any means from outside the class definition.'''


# 4. Getter and Setter methods

from datetime import datetime
class User:
    def __init__(self,name,email,password):
        self.name = name
        self._email = email 
        self.password = password


    def get_email(self):
        print(f"Email was accessed at: {datetime.now()}")
        return self._email
    def set_email(self , new_email):
        if "@" in new_email:
            self._email = new_email

user2 = User("adhya","adha@gmail.com" , "2dnwi")

print(user2.get_email())
user2.set_email("adhya32135@gmail.com")
print(user2.get_email())


# 5. Python Properties
# --> it is a recommended approach for controlling access to data in python

class User:
    def __init__(self,name,email,password):
        self.name = name
        self._email = email 
        self.password = password
    

    @property      # Set getter like this
    def email(self):
        print("Email accessed")
        return self._email
    
    @email.setter   #Set setter of the same like this: @nameoftheattribute.setter
    def email(self,new_email):
        if "@" in new_email:
            self.email = new_email

user2 = User("adhya","adha@gmail.com" , "2dnwi")
print(user2.email)  

#6. Static Attributes

# differance between instance and static attribute-->
#========================================================
#   Instance Attrib.     |      Static Atrib.
#========================================================
#   created each time    | static attribute exists
# a new instance of the  |  within the class (value 
# class is created.      | remains the common no matter 
#                        | with instance of that class 
#                        | class it)

class User:
    name_change_count = 0

    def __init__(self,name,email,password):
        self._name = name
        self.email = email
        self.password = password
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,new_name):
        self._name = new_name
        User.name_change_count += 1

user2 = User("adhya","adha@gmail.com" , "2dnwi")
print(f"Original: {user2.name}")        # → Adhya
print(f"Total changes: {User.name_change_count}")  # → 0

user2.name = "Deeksha"                  # ← Use assignment, not function call
print(f"New name: {user2.name}")        # → Deeksha
print(f"Total changes: {User.name_change_count}")


# 7. Static vs. Instance methods

class BankAccount:
    MIN_BALANCE = 100

    def __init__(self,owner , balance =0):
        self.owner = owner
        self._balance = balance

    def deposite(self , amount):
        if amount > 0:
            self._balance += amount
            print(f"{self.owner}'s new balance: [{self._balance}]")
        else:
            print(f"Deposite amount must be positive")
    
    @staticmethod
    def is_valid_interest_rate(rate):
        return 0 <= rate <= 5
    
account4553 = BankAccount("Adarsh" , 100)
account4553.deposite(200)

print(BankAccount.is_valid_interest_rate(3))
print(BankAccount.is_valid_interest_rate(10))