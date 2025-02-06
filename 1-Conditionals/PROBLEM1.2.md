[Home](../README.md) | [Lecture 1](1-Conditionals.md) | [Problem 1.1](PROBLEM1.1.md) | Problem 1.2 | [Problem 1.3](PROBLEM1.3.md) | [Problem 1.4](PROBLEM1.4.md) | [Problem 1.5](PROBLEM1.5.md)

# Home Federal Savings Bank
Watch: https://youtu.be/IN6cJ_wGmsk

In season 7, episode 24 of Seinfeld, Kramer visits a bank that promises to give $100 to anyone who isn’t greeted with a “hello.” Kramer is instead greeted with a “hey,” which he insists isn’t a “hello,” and so he asks for $100. The bank’s manager proposes a compromise: “You got a greeting that starts with an ‘h,’ how does $20 sound?” Kramer accepts.

In a file called `bank.py`, implement a program that prompts the user for a greeting. If the greeting starts with `“hello”`, output `$0`. If the greeting starts with an `“h”` (but not “hello”), output `$20`. Otherwise, output `$100`. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.

## Hints
- Recall that a `str` comes with quite a few methods, per <https://docs.python.org/3/library/stdtypes.html#string-methods>.
- Be sure to give `$0` not only for `“hello”` but also `“hello there”`, `“hello, Newman”`, and the like.

## Before You Begin
From the root of your repository execute `cd 1-Conditionals` So your current working directory is ...		

		/1-Conditionals $:
Next execute

		mkdir bank
to make a folder called `bank` in your codespace.

Then execute

		cd bank
to change directories into that folder. You should now see your terminal prompt as `/1-Conditionals/bank $`. You can now execute

		code bank.py
to make a file called `bank.py` where you’ll write your program.

# How to Test
Here’s how to test your code manually. At the `bank/ $` prompt in your terminal: :

1. Run your program with `python bank.py`. Type `Hello` and press Enter. Your program should output:

		$0
2. Run your program with python bank.py. Type `Hello`, Newman and press Enter. Your program should output:

		$0
3. Run your program with `python bank.py`. Type `How you doing?` and press Enter. Your program should output:

		$20
4. Run your program with `python bank.py`. Type `What's happening?` and press Enter. Your program should output:

		$100

# Commit your program to GITHUB
At the `/1-Conditionals/bank $` prompt in your terminal:

		git add -A 
Add all changed files in the repository to be committed

		git commit -m “Upload completed bank.py“
Commit all changes in the REPO with the comment “Upload completed bank.py“
*note: If the file is not complete, adjust the comment to describes what is being commited*

		git push 
Push all changes to the REPO