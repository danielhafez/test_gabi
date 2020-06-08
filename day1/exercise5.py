def build_pyramid(height):
    for i in range(1, height + 1, 1):
        print(' ' * height + i * '* ')
        height = height - 1


print('Hello, this program will print a pyramid with height of 5: \r')
build_pyramid(5)
