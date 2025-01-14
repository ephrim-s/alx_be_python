def safe_divide(numerator, denominator):
    try:
        if denominator == 0:
            raise ValueError("Error: Cannot divide by zero.")
        return float(numerator)/float(denominator)
    except NameError:
        print("Error: Please enter numeric values only.")
