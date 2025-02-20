def main():
    plate = input("Plate: ")
    if is_valid(plate):		
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    not_first_num = False
    number_start = False
    char_count = 0
    for char in s:
        if char.isdigit() == False and char.isalpha() == False:
            return False
        char_count += 1
        if char_count == 1 or char_count == 2:
            if char.isdigit():
                return False
        if char.isdigit():
            number_start = True
        if number_start:
            if char.isalpha():
                return False
            elif not_first_num == False:
                if char == "0":
                    return False
                not_first_num = True
    if char_count > 6 or char_count < 2:
        return False
    return True




main()
