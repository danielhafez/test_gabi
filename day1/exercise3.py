def is_even(number):
    if not isinstance(number, int):
        return "Error: please insert an integer"
        exit(code)
    elif number % 2 == 0:
        return str(number) + " is even"
    else:
        return str(number) + " is not even"

