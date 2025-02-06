[Home](../README.md) | [Lecture 2](2-Loops.md) | Problem 2.1 | [Problem 2.2](PROBLEM2.2.md) | [Problem 2.3](PROBLEM2.3.md) | [Problem 2.4](PROBLEM2.4.md) | [Problem 2.5](PROBLEM2.5.md)

# camelCase
<img src="images/1024px-CamelCase_new.svg.png" width="300" />

Source: [en.wikipedia.org/wiki/Camel_case](https://en.wikipedia.org/wiki/Camel_case)

In some languages, it’s common to use [camel case](https://en.wikipedia.org/wiki/Camel_case) (otherwise known as “mixed case”) for variables’ names when those names comprise multiple words, whereby the first letter of the first word is lowercase but the first letter of each subsequent word is uppercase. For instance, whereas a variable for a user’s name might be called `name`, a variable for a user’s first name might be called `firstName`, and a variable for a user’s preferred first name (e.g., nickname) might be called `preferredFirstName`.

Python, by contrast, [recommends](https://peps.python.org/pep-0008/#function-and-variable-names) [snake case](https://en.wikipedia.org/wiki/Snake_case), whereby words are instead separated by underscores (_), with all letters in lowercase. For instance, those same variables would be called `name`, `first_name`, and `preferred_first_name`, respectively, in Python.

In a file called `camel.py`, implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. Assume that the user’s input will indeed be in camel case.

## Hints
- Recall that a `str` comes with quite a few methods, per [docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods).
Much like a `list`, a `str` is “iterable,” which means you can iterate over each of its characters in a loop. For instance, if `s` is a `str`, you could print each of its characters, one at a time, with code like:
		for c in s:
    		print(c, end="")

## Before You Begin
From the root of your repository execute `cd 2-Loops` So your current working directory is ...		

		/2-Loops $:
Next execute

		mkdir camel
to make a folder called `camel` in your codespace.

Then execute

		cd camel
to change directories into that folder. You should now see your terminal prompt as `/2-Loops/camel $`. You can now execute

		code camel.py
to make a file called `camel.py` where you’ll write your program.

# How to Test
Here’s how to test your code manually:

1. Run your program with `python camel.py`. Type `name` and press Enter. Your program should output:

		name   
2. Run your program with `python camel.py`. Type `firstName` and press Enter. Your program should output:

		first_name
3. Run your program with `python camel.py`. Type `preferredFirstName` and press Enter. Your program should output

		preferred_first_name

# Commit your program to GITHUB
At the `/2-Loops/camel $` prompt in your terminal:

		git add -A 
Add all changed files in the repository to be committed

		git commit -m “Upload completed camel.py“
Commit all changes in the REPO with the comment “Upload completed camel.py“
*note: If the file is not complete, adjust the comment to describes what is being commited*

		git push 
Push all changes to the REPO
