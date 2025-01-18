class DivisionByZeroError(Exception):
    """Custom exception for division by zero."""
    pass

def safe_divide(numerator, denominator):
    '''Divide two numbers safely'''
    try:
        # Attempt to convert inputs to floats
        num = float(numerator)
        den = float(denominator)
        if den == 0:
            raise DivisionByZeroError("Error: Division by zero is not allowed.")
        # Perform division
        result = num / den
        return f"Result: {result:.2f}"
    except DivisionByZeroError as e:
        return str(e)
    except ValueError:
        return "Error: Both inputs must be numeric."

if __name__ == "__main__":
    print(safe_divide(10, 2))  
    print(safe_divide(10, 0))  
    print(safe_divide(10, 'a'))