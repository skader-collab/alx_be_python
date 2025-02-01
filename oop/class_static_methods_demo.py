class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Returns the sum of two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Prints the calculation type and returns the product of two numbers."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

# Example usage:
if __name__ == "__main__":
    print(f"Addition: {Calculator.add(5, 3)}")
    print(f"Multiplication: {Calculator.multiply(4, 2)}")