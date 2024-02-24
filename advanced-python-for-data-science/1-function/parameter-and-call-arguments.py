# Example
# - no input
# - 3 output
#     - multiply 5*2
#     - multiply 10*2
#     - multiply 15*2
# - process set value in main function
# - transfer all valur from main into sub function
# - exec process and display at sub function

def multiply(number):
    print(str(number) + "*2 : " + str(number*2))

multiply(5)
multiply(10)
multiply(15)

def sum_two_numbers(a, b):
    return a+b

c = sum_two_numbers(1,3)
print(c)


def plus(x, y):
    return x+y

def minus(x, y):
    return x-y

def multiply(x, y):
    return x*y

def divide(x, y):
    return x/y

x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))

c = plus(x, y)
print("The sum of the two numbers is: ", c)

c = minus(x, y)
print("The difference of the two numbers is: ", c)

c = multiply(x, y)
print("The product of the two numbers is: ", c)

c = divide(x, y)
print("The division of the two numbers is: ", c)