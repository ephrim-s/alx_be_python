def safe_divide(numerator, denominator):
    try:
        return int(numerator)/int(denominator)
    except Exception as e:
        return e