def main():
    """Main function"""
    print_square(3)


def print_square(size):
    """Function printing square"""
    for _ in range(size):
        print_row(size)


def print_row(width):
    """Function printing row"""
    print("#" * width)


main()
