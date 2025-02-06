[Home](../README.md) | [Lecture 2](2-Loops.md) | [Problem 2.1](PROBLEM2.1.md) | Problem 2.2 | [Problem 2.3](PROBLEM2.3.md) | [Problem 2.4](PROBLEM2.4.md) | [Problem 2.5](PROBLEM2.5.md)

# Coke Machine
<img src="images/coke.png" width="300" />

Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.

## Before You Begin
From the root of your repository execute `cd 2-Loops` So your current working directory is ...		

		/2-Loops $:
Next execute

		mkdir coke
to make a folder called `coke` in your codespace.

Then execute

		cd coke
to change directories into that folder. You should now see your terminal prompt as `/2-Loops/coke $`. You can now execute

		code coke.py
to make a file called `coke.py` where you’ll write your program.

# How to Test
Here’s how to test your code manually:

1. Run your program with `python coke.py`. At your `Insert Coin`: prompt, type `25` and press Enter. Your program should output:

		Amount Due: 25   
and continue prompting the user for coins.

2. Run your program with python coke.py. At your `Insert Coin`: prompt, type `10` and press Enter. Your program should output:

		Amount Due: 40
and continue prompting the user for coins.

3. Run your program with python coke.py. At your `Insert Coin`: prompt, type `5` and press Enter. Your program should output:

		Amount Due: 45
and continue prompting the user for coins.

4. Run your program with python coke.py. At your `Insert Coin`: prompt, type `30` and press Enter. Your program should output:

		Amount Due: 50
because the machine doesn’t accept 30-cent coins! Your program should then continue prompting the user for coins.

5. Run your program with `python coke.py`. At your `Insert Coin`: prompt, type `25` and press Enter, then type `25` again and press Enter. Your program should halt and display:

		Change Owed: 0
6. Run your program with `python coke.py`. At your Insert Coin: prompt, type `25` and press Enter, then type 10 and press Enter. Type `25` again and press Enter, after which your program should halt and display:

		Change Owed: 10

# Commit your program to GITHUB
At the `/2-Loops/coke $` prompt in your terminal:

		git add -A 
Add all changed files in the repository to be committed

		git commit -m “Upload completed coke.py“
Commit all changes in the REPO with the comment “Upload completed coke.py“
*note: If the file is not complete, adjust the comment to describes what is being commited*

		git push 
Push all changes to the REPO