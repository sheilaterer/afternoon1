# function for substraction
def subtract(r ,s):
    return r - s

# function for addition
def add(t ,d):
    return t + d

# function for division
def divide(g ,f):
    return g / f

# function for multiplication
def multiply(x ,y):
    return x * y

print("1.subtract")
print("2.add")
print("3.divide")
print("4.multiply")

while True:
    choice = input("Enter choice(1/2/3/4):")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number:"))
        num2 = float(input("Enter second number:"))

        if choice == '1':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '2':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '3':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '4':
            print(num1, "*", num2, "=", multiply(num1, num2))
        break

    else:
        print("Invalid")








