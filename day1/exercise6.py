def build_pyramid(height):
    # Check if input is valid
    if isinstance(height, int) is False:
        if isinstance(height, str):
            try:
                int(height)
            except ValueError:
                print("Please insert an integer")
                exit()
        else:
            print("Please insert an integer")
            exit()

    height = int(height)
    if height < 0:
        print("Please insert a POSITIVE integer")
        exit()

    for i in range(1, height + 1, 1):
        print(' ' * height + i * '* ')
        height = height - 1


print('Hello, this program will print a pyramid \r')
user_height = input("Please insert the height of the pyramid: ")
build_pyramid(user_height)
