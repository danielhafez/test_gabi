def build_pyramid_with_direction(height, direction):
    # Check if input is valid
    if isinstance(height, int) is False:
        if isinstance(height, str):
            try:
                int(height)
            except ValueError:
                print("Please insert an integer for the height")
                exit()
        else:
            print("Please insert an integer for the height")
            exit()

    height = int(height)
    if height < 0:
        print("Please insert a POSITIVE integer for the height")
        exit()

    if direction == 'down':
        opposite = 0
        for i in range(height + 1, 1, -1):
            print(' ' * opposite + (i - 1) * '* ')
            opposite = opposite + 1
            height = height - 1
    else:
        for i in range(1, height + 1, 1):
            print(' ' * height + i * '* ')
            height = height - 1


print('Hello, this program will print a pyramid \r')
user_height = input("Please insert the height of the pyramid: ")
user_direction = str(input('Please choose the direction of the pyramid (up/down): '))
build_pyramid_with_direction(user_height, user_direction)
