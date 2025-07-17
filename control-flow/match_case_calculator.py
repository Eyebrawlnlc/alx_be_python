number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")


if operation == "+":
    result = number1 + number2
    print(result)
elif operation == "-":
    result = number1 - number2
    print(result)
elif operation == "*":
    result = number1 * number2
    print(result)
elif operation == "/":
    result = number1 / number2
    print(result)