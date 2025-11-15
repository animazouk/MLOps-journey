num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))
op = input("enter the operator")

def calculator(x,y,o):

    if o == '+':
        return x + y
    elif o == '-':
        return x - y
    elif o == '*':
        return x * y
    elif o == '/':
        return x / y
    elif o == '%':
        return x % y
    else:
        print("wrong oprand input")

print(calculator(num1,num2,op))