class DivisionByZeroError(Exception):
    """Custom exception for division by zero."""
    pass


def safe_divide(numerator, denominator):
    '''Divide two numbers safely'''
    try:
        result = float(numerator) / float(denominator)
    except ZeroDivisionError:
        raise DivisionByZeroError('Error: Cannot divide by zero')
    except ValueError:
        print('Error: Please enter numeric values only')
    else:
        print(f'The result of the division is {result}')