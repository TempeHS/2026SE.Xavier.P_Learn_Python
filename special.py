num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Enter the operator: ")
ui_output = ""
if operator == "-":
    ui_output = num1 - num2
elif operator == "+":
    ui_output = num1 + num2
elif operator == "*":
    ui_output = num1 * num2
elif operator == "/":
    ui_output = num1 / num2
else:
    ui_output = "Not a known operator"
print(ui_output)

