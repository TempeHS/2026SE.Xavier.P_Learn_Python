def main():
    
    while True:
        try:
            fraction = input("Enter the fraction of fuel: ")
            top, bottom = fraction.split('/')
            fuel = int(top) / int(bottom)
            fuel = round(fuel * 100)
            if 100 >= fuel >= 99:
                print("F")
            elif fuel <= 1:
                print("E")
            elif fuel < 100:
                print(f"{fuel}%")
        except ValueError:
            print("ERROR: Please enter a fraction (X/Y)")
        except ZeroDivisionError:
            print("ERROR: Cannot divide by zero")
        if fuel > 100:
            continue
        else:
            break

main()