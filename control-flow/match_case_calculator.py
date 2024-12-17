num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Choose the operation (+, -, *, /): ")
result = 0;

if num2 == 0 and operator == '/':
    print("Cannot divid by zero.")
else:
    match operator:
        case '+':
            result = num1 + num2
        case '-':
            result = num1 - num2
        case '*':
            result = num1 * num2
        case '/':
            result = num1 / num2
        case _:
            print("invalide entry")
    print(f"The result is {result}")

