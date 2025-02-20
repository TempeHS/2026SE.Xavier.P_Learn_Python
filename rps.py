# import the random module
import random

# ask and store name
valid_name = False
while valid_name == False:
    player_name = input("What is your name? ").title()
    if player_name == "Computer" or player_name == "" or player_name == "/n":
        print("Invalid name!")
    else:
        valid_name = True
print(f"Hello, {player_name}!")

# ask for rounds
def rounds(): 
    return int(input("How many rounds would you like to play? "))

# dictionary of choice-num conversion
rps_data = {"Rock":0, "Paper":1, "Scissors":2}
reverse_rps_data = {0:"Rock", 1:"Paper", 2:"Scissors"}

# ask for choice
def player_choice():
    print("What is your choice? ")
    valid_choice = False
    while valid_choice == False:
        choice = input("Rock, paper or scissors: ").capitalize()
        if choice.capitalize() in rps_data:
            print(f"{player_name}, You chose {choice}")
            valid_choice = True
        else:
            print("Invalid choice! Please choose an option: ")
    return rps_data[choice]


# generate random choice for computer
def cpu_choice():
    com_choice = random.randint(0, 2)
    print(f"The opponent chose {reverse_rps_data[com_choice]}")
    return com_choice

# compare choices and determine winner
def compare_choice(p, c):
    if p == c:
        print("Its a tie!")
        return 1
    elif p - 1 == c or p + 2 == c:
        print(f"{player_name} wins!")
        return 2
    else:
        print("Computer wins!")
        return 0

# score keeping
def score(i):
    match i:
        case 0:
            return 1, 0
        case 1:
            return 0, 0
        case 2:
            return 0, 1

# main core
def main():
    long_score_cpu = 0
    long_score_player = 0
    round_int = rounds()
    for _ in range(0, round_int):
        p_choice = player_choice()
        c_choice = cpu_choice()
        score_cpu, score_player = score(compare_choice(p_choice, c_choice))
        long_score_cpu = long_score_cpu + score_cpu
        long_score_player = long_score_player + score_player
        print(f"{player_name}: {long_score_player}, Computer: {long_score_cpu}")
    print("That's the game!")
    if long_score_player > long_score_cpu:
        print(f"{player_name} wins the game!")
        print(f"Congratulations on your victory, {player_name}!")
    elif long_score_player < long_score_cpu:
        print("Computer wins the game!")
        print(f"Better luck next time, {player_name}.")
    else:
        print("It's a tie!")

main()
