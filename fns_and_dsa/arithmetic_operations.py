def perform_operation(num1, num2, operation):

    if operation == "add":
        result = num1 + num2
        return result
    elif operation == "subtract":
        result = num1 - num2
        return result
    elif operation == "multiply":
        result = num1 * num2
        return result
    elif operation == "divide":
        try:
            result = num1 / num2
            return result
        except ZeroDivisionError:
            return print("You can't divide by ZERO!")
    else:
        return print("please choose a valid operator!")




    