def safe_divide(numerator, denominator):
    try:
        if denominator == 0:
            raise ValueError("Error: Cannot divide by zero.")
        result = float(numerator)/float(denominator)
        return f"The result of the division is {result}"
    except NameError:
        print("Error: Please enter numeric values only.")
