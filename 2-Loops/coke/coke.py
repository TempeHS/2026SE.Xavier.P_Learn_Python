amount_due = 50
while amount_due > 0:
    coin = int(input("Insert coin: "))
    if coin == 25 or coin == 10 or coin == 5:
        amount_due = amount_due - coin
    if amount_due > 0:
        print("Amount Due: " + str(amount_due))
print("Change Owed: " + str((amount_due * -1)))