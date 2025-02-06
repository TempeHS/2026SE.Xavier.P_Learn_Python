[Home](../README.md) | [Lecture 1](1-Conditionals.md) | [Problem 1.1](PROBLEM1.1.md) | [Problem 1.2](PROBLEM1.2.md) | [Problem 1.3](PROBLEM1.3.md) | Problem 1.4 | [Problem 1.5](PROBLEM1.5.md)

# Math Interpreter

Python already supports math, whereby you can write code to add, subtract, multiply, or divide values and even variables. But let’s write a program that enables users to do math, even without knowing Python.

In a file called `interpreter.py`, implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place. Assume that the user’s input will be formatted as `x` `y` `z`, with one space between `x` and `y` and one space between `y` and `z`, wherein:

`x` is an integer
`y` is `+`, `-`, `*`, or `/`
`z` is an integer
For instance, if the user inputs `1 + 1`, your program should output `2.0`. Assume that, if `y` is `/`, then `z` will not be `0`.

Note that, just as `python` itself is an interpreter for Python, so will your `interpreter.py` be an interpreter for math!

## Hints
- Recall that a `str` comes with quite a few methods, per <https://docs.python.org/3/library/stdtypes.html#string-methods>, including `split`, which separates a `str` into a sequence of values, all of which can be assigned to variables at once. For instance, if `expression` is a `str` like `1 + 1`, then

		x, y, z = expression.split(" ")
will assign `1` to `x`, `+` to `y`, and `1` to `z`.

## Before You Begin
From the root of your repository execute `cd 1-Conditionals` So your current working directory is ...		

		/1-Conditionals $:
Next execute

		mkdir interpreter
to make a folder called `interpreter` in your codespace.

Then execute

		cd interpreter
to change directories into that folder. You should now see your terminal prompt as `/1-Conditionals/interpreter $`. You can now execute

		code interpreter.py
to make a file called `interpreter.py` where you’ll write your program.

# How to Test
Here’s how to test your code manually. At the `interpreter/ $` prompt in your terminal: :

1. Run your program with `python interpreter.py`. Type `1 + 1` and press Enter. Your program should output:

		2.0
2. Run your program with `python interpreter.py`. Type `2 - 3` and press Enter. Your program should output:

		-1.0
3. Run your program with `python interpreter.py`. Type `2 * 2` and press Enter. Your program should output:

		4.0
4. Run your program with `python interpreter.py`. Type `50 / 5` and press Enter. Your program should output:

		10.0

# Commit your program to GITHUB
At the `/1-Conditionals/interpreter $` prompt in your terminal:

		git add -A 
Add all changed files in the repository to be committed

		git commit -m “Upload completed interpreter.py“
Commit all changes in the REPO with the comment “Upload completed interpreter.py“
*note: If the file is not complete, adjust the comment to describes what is being commited*

		git push 
Push all changes to the REPO
