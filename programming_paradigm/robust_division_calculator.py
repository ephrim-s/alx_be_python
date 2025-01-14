def safe_divide(numerator, denominator):
    try:
        if denominator == 0:
            raise ValueError:
                print("Error: Cannot divide by zero.")
        return int(numerator)/int(denominator)
    except Exception as e:
        return e
