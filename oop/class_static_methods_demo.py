class Calculator:
    """A simple calculator demonstrating class and static methods."""

    # Class attribute shared by all instances
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method to add two numbers.
        This method does not access class or instance data.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method to multiply two numbers.
        This method accesses the class attribute 'calculation_type'.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
