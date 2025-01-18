def safe_divide(numerator, denominator):
    '''Divide two numbers safely'''
    try:
        # Attempt to convert inputs to floats
        num = float(numerator)
        den = float(denominator)
        # Perform division
        result = num / den
        return f"Result: {result:.2f}"
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except ValueError:
        return "Error: Both inputs must be numeric."

if __name__ == "__main__":
    print(safe_divide(10, 2))  
    print(safe_divide(10, 0))  
    print(safe_divide(10, 'a'))