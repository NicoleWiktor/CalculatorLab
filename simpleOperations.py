def simple_calculate(operation, num1, num2):
    """
    Performs the given simple operation on the given numbers, which may be either integers or floats.
    args:
        - operation: the operation to perform (+, -, *, or /)
        - num1: the first number
        - num2: the second number
    returns:
        - the result of the operation on the given numbers
    """

    if operation == '+':
        return num1 + num2

    elif operation == '-':
        # TODO: finish this statement
        # - should return the result of subtracting num2 from num1
        pass  # Replace this line with your code
        return num1 - num2
    elif operation == '*':
        # TODO: finish this statement
        # - should return the result of multiplying num1 by num2
        pass  # Replace this line with your code
        return num1*num2
    elif operation == '/':
        # TODO: finish this statement
        # - should return the result of dividing num1 by num2
        # - remember to raise a ValueError if num2 is 0
        pass  # Replace this line with your code
        return num1/num2
    else:
        raise ValueError(
            'Invalid Operation: Simple Operations are (+, -, *, and /)')
