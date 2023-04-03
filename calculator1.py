# program for simple calculator
firstnumber = float(input("Enter first number:"))
secondnumber = float(input("Enter second number"))
myoperator = str(input("Enter operator(+, -, *, /)"))

if myoperator=="+":
    print(firstnumber+secondnumber)
elif myoperator=="-":
    print(firstnumber-secondnumber)
elif myoperator=="/":
    print(firstnumber/secondnumber)
elif myoperator=="*":
    print(firstnumber*secondnumber)
else:
    print("Invalid")