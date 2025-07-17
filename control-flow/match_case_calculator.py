number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
operator = input("Choose the operation (+, -, *, /): ")


if operator == "+":
    result = number1 + number2
    print(result)
elif operator == "-":
    result = number1 - number2
    print(result)
elif operator == "*":
    result = number1 * number2
    print(result)
elif operator == "/":
    result = number1 / number2
    print(result)