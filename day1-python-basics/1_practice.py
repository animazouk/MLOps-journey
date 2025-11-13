# Print function
print("\n")
print("   /|")
print("  / |")
print(" /  |")
print("/___|")

# Working with string
print("\n")
phrase = "Adarsh Vishwakarma"
print(phrase.lower()) #returns value of the variable as lower case
print(len(phrase)) # number of letters in a string 'conts spaces as well'
print(phrase.index("A")) # returns the value at the particular index
print(phrase.replace("Adarsh","Adhya")) # returns the value of the variable after rplaceing the first argument by the second passed argument.

# Working with numbers
print("\n")
print(-2.453) #supports negative numbers
print(2.487)
print(3 * 5 - 3 + (4 - 2)) # follows BODMAS
my_num = 5
print(str(my_num) + " is my favourite number") #concatination of int and str in not possible thats why we hade to explicitly convert my_num into a str.
print(-5)
print(abs(-5.5)) #gives absolute values by ingnoring the sign
print(pow(3,2)) # first arg is the oprand second is the power value we want to find for it
print(max([1,2,3,4,5,6,7,8,7,6,98])) #returns the maximum value among the given data
print(3.7) #roundsoff numbers

from math import * #imports various math functions defined in the math module in python

print(floor(3.7)) #roundsit of to the immidiat whole number vlaue lesser then it.
print(ceil(3.2)) #rounds it of to the imidiate whole number value greater then it.
print(round(sqrt(4))) #returns square root of the given number


#GETTING INPUT FROM A USER
name = input("Enter your Name")
print("Hi! " + name)