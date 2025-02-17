original = input("Text: ")
for char in original:
    char_lower = char.lower()
    if char_lower != char:
        print("_", end="")
    print(char_lower, end="")
print()