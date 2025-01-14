def safe_divide(numerator, denominator):
    try:
        if denominator == 0:
            raise ZeroDivisionError("Error: Cannot divide by zero.")
        result = float(numerator)/float(denominator)
        return f"The result of the division is {result}"
    except ValueError:
        print("Error: Please enter numeric values only.")
