def safe_divide(numerator, denominator):
    try:
        if denominator == 0:
            raise ZeroDivisionError("Error: Cannot divide by zero.")

        else:
            print("The result of the division is", float(numerator) / float(denominator))
    except:
        raise ValueError("Error: Please enter numeric values only.")

