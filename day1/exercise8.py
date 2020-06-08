def solve_math(expression):
    if not isinstance(expression, str):
        return "the algebra expression is invalid"
        exit()

    else:
        modified = expression.split('x')
        print(expression.split('x'))



def filter_spaces(array):
    for elements in array:
        if elements == " ":
            return False
        else:
            return True


solve_math('x-x+x/x')
