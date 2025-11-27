#============================
# Example-1. a Person class
#============================

class Person:
    def __init__(self,name , age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"HELLO, {self.name} you must be {self.age} years old")


person1 = Person("adarsh",21)
person1.greet()