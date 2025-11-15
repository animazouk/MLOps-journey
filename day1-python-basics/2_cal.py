
# INPUT TWO NUMBERS FROM THE USER AND PRINT THERE ADDITION

num1 = input("enter the first number: ")
num2 = input("enter the second number: ")
result1 = num1 + num2 
''' returns a concatinated string of those to numbers 
rather then there addition because python takes input 
from the user in string format thus we need to convert 
them to numbers befopre hand '''

# result2 = int(num1) + int(num2)
#  now this will convert them into whole values thus ignoring the decimal values 
result3 = float(num1) + float(num2) # now we are good


print(result1)
print(result3)