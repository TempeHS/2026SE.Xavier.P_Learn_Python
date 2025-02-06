[Home](../README.md) | [Lecture 5](5-UnitTests.md) | [Problem 5.1](PROBLEM5.1.md) | Problem 5.2 | [Problem 5.3](PROBLEM5.3.md) | [Problem 5.4](PROBLEM5.4.md)

# Back to the Bank
In a file called bank.py, reimplement Home Federal Savings Bank from Problem Set 1, restructuring your code per the below, wherein value expects a str as input and returns an int, namely 0 if that str starts with “hello”, 20 if that str starts with an “h” (but not “hello”), or 100 otherwise, treating the str case-insensitively. You can assume that the string passed to the value function will not contain any leading spaces. Only main should call print.

def main():
    ...


def value(greeting):
    ...


if __name__ == "__main__":
    main()
Then, in a file called test_bank.py, implement three or more functions that collectively test your implementation of value thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

pytest test_bank.py

## Hints
Be sure to include
import bank
or

from bank import value
atop test_bank.py so that you can call value in your tests.

Take care to return, not print, an int in value. Only main should call print.

## Before You Begin
From the root of your repository execute `cd 5-UnitTests` So your current working directory is ...		

		/5-UnitTests $:
Next execute

		mkdir test_bank
to make a folder called `test_bank` in your codespace.

Then execute

		cd test_bank
to change directories into that folder. You should now see your terminal prompt as `/5-UnitTests/test_bank $`. You can now execute

		code test_bank.py
to make a file called test_bank.py where you’ll write your program.

# How to Test
To test your tests, run pytest test_bank.py. Be sure you have a copy of a bank.py file in the same folder. Try to use correct and incorrect versions of bank.py to determine how well your tests spot errors:

Ensure you have a correct version of bank.py. Run your tests by executing pytest test_bank.py. pytest should show that all of your tests have passed.
Modify the correct version of bank.py, changing the values provided for each greeting. Your program might, for example, mistakenly provide $100 to a customer greeted by “Hello” and $0 to a customer greeted with “What’s up”! Now, run your tests by executing pytest test_bank.py. pytest should show that at least one of your tests has failed.

# Commit your program to GITHUB
At the `/5-UnitTests/test_bank $` prompt in your terminal:

		git add -A 
Add all changed files in the repository to be committed

		git commit -m “Upload completed test_bank.py“
Commit all changes in the REPO with the comment “Upload completed test_bank.py“
*note: If the file is not complete, adjust the comment to describes what is being commited*

		git push 
Push all changes to the REPO