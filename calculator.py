class Calculator:
    """
    Simple calculator performing basic arithmetic operations on two numbers.
    """
    def __init__(self, op1: float, op2: float):
        """
        Initializes the calculator with two parameters
        Args:
            op1 (float): The first number
            op2 (float): The second number
        """
        self.__op1 = op1
        self.__op2 = op2

    def sum(self) -> float:
        """
        Return the sum of the two operands

        Returns:
            float: The result of addition
        """
        return self.__op1 + self.__op2

    def subtract(self) -> float:
        """
        Return the difference of the two operands

        Returns:
            float: The result of subtraction op1 - op2
        """

        return self.__op1 - self.__op2

    def multiply(self) -> float:
        """
        Return the product of the two operands

        Returns:
            float: The result of multiplication
        """

        return self.__op1 * self.__op2

    def divide(self) -> float:
        """
        Return the division of op1 by op2
        if op2 is zero, return an error message.

        Returns:
            float: The result of addition
        """

        # first version of code to avoid Error
        if self.__op2 == 0:
            return "Error - division by zero!!!"
        else:
            return self.__op1 / self.__op2

        # second version of code to avoid Error
        # try:
        #     return self.__op1 / self.__op2
        # except ZeroDivisionError:
        #     return "Error - division by zero!!!"


if __name__ == "__main__": # pragma: no cover
    # Example usage of calculator

    calc_1 = Calculator(1.0, 2.0)
    print("Addition: ", calc_1.sum())
    print("Subtraction: ", calc_1.subtract())
    print("Multiplication: ", calc_1.multiply())
    print("Division: ", calc_1.divide())

    print("\n---Division by 0 (op2 == 0) ---")

    calc_2 = Calculator(1.0, 0.0)
    print("Division by zero: ", calc_2.divide())


