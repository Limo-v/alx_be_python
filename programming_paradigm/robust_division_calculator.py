def safe_divide(numerator, denominator):
    try:
        if denominator == 0:
            raise ZeroDivisionError("Error: Cannot divide by zero.")

        else:
            float(numerator) / float(denominator)
    except:
        raise ValueError("Error: Please enter numeric values only.")

