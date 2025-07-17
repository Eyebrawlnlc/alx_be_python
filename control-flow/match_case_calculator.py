number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
operations = input("Choose the operation (+, -, *, /): ")


if operations == "+":
    result = number1 + number2
    print(result)
elif operations == "-":
    result = number1 - number2
    print(result)
elif operations == "*":
    result = number1 * number2
    print(result)
elif operations == "/":
    result = number1 / number2
    print(result)
