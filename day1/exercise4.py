def is_parsable(user_input):
    if not isinstance(user_input, str) and not isinstance(user_input, int):
        return "please insert a string or an integer"
        exit(code)
    elif isinstance(user_input, int):
        return "the input is parsable to an integer"
    elif isinstance(user_input, str):
        try:
            int(user_input)
            return "the input is parsable to an integer"
        except ValueError:
            return "the inserted string can't be parsed to integer"


example = input("Please insert a string or an integer ")
print(is_parsable(example))