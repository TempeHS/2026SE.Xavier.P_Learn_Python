[Home](../README.md) | [Lecture 4](4-Libraries.md) | [Problem 4.1](PROBLEM4.1.md) | [Problem 4.2](PROBLEM4.2.md) | [Problem 4.3](PROBLEM4.3.md) | Problem 4.4 | [Problem 4.5](PROBLEM4.5.md) | [Problem 4.6](PROBLEM4.6.md)

# Guessing Game
I’m thinking of a number between 1 and 100…

[What is it?](images\Answer.png)

In a file called `game.py`, implement a program that:

- Prompts the user for a level, _n_. If the user does not input a positive integer, the program should prompt again.
- Randomly generates an integer between 1 and _n_, inclusive, using the `random` module.
- Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
- If the guess is smaller than that integer, the program should output `Too small!` and prompt the user again.
- If the guess is larger than that integer, the program should output `Too large!` and prompt the user again.
- If the guess is the same as that integer, the program should output `Just right!` and exit.

## Hints
- Note that the `random` module comes with quite a few functions, per [docs.python.org/3/library/random.html](https://docs.python.org/3/library/random.html).

## Before You Begin
From the root of your repository execute `cd 4-Libraries` So your current working directory is ...		

		/4-Libraries $:
Next execute

		mkdir game
to make a folder called `game` in your codespace.

Then execute

		cd game
to change directories into that folder. You should now see your terminal prompt as `/4-Libraries/game $`. You can now execute

		code game.py
to make a file called `game.py` where you’ll write your program.

# How to Test
Here’s how to test your code manually:

1. Run your program with `python game.py`. Type `cat` at a prompt that says `Level:` and press Enter. Your program should reprompt you:

		Level:   
2. Run your program with `python game.py`. Type `-1` at a prompt that says `Level:` and press Enter. Your program should reprompt you:

		Level:   
3. Run your program with `python game.py`. Type `10` at a prompt that says `Level:` and press Enter. Your program should now be ready to accept guesses:

		Guess:   
4. Run your program with `python game.py`. Type `10` at a prompt that says `Level:` and press Enter. Then type `cat`. Your program should reprompt you:

		Guess:   
5. Run your program with `python game.py`. Type `10` at a prompt that says `Level:` and press Enter. Then type `-1`. Your program should reprompt you:

		Guess:   
6. Run your program with `python game.py`. Type `1` at a prompt that says `Level:` and press Enter. Then type `1`. Your program should output:

		Just right!  
There’s only one possible number the answer could be!
7. Run your program with `python game.py`. Type `10` at a prompt that says `Level:` and press Enter. Then type `100`. Your program should output:

		Too large!  
Looks like you’re guessing outside the range you specified.
8. Run your program with `python game.py`. Type `10000 `at a prompt that says `Level:` and press Enter. Then type `1`. Your program should output:

		Too small!  
Most likely, anyways: you might get lucky and see Just right!. But it would certainly be odd for you to see Just right! every time. And certainly you shouldn’t see Too large!.

# Commit your program to GITHUB
At the `/4-Libraries/game $` prompt in your terminal:

		git add -A 
Add all changed files in the repository to be committed

		git commit -m “Upload completed game.py“
Commit all changes in the REPO with the comment “Upload completed game.py“
*note: If the file is not complete, adjust the comment to describes what is being commited*

		git push 
Push all changes to the REPO