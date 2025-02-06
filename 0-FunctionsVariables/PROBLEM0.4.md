[Home](../README.md) | [Lecture 0](0-FunctionsVariables.md) | [Problem 0.1](PROBLEM0.1.md) | [Problem 0.2](PROBLEM0.2.md) | [Problem 0.3](PROBLEM0.3.md) | Problem 0.4 | [Problem 0.5](PROBLEM0.5.md)

# Einstein

Even if you haven’t studied physics (recently or ever!), you might have heard that E = mc<sup>2</sup>, wherein E represents energy (measured in Joules), E represents mass (measured in kilograms), and represents the speed of light (measured approximately as 300000000 meters per second), per Albert Einstein et al. Essentially, the formula means that mass and energy are equivalent.

In a file called `einstein.py`, implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.

## Hints
- Recall that input returns a `str`, per <https://docs.python.org/3/library/functions.html#input>.
- Recall that int can convert a `str` to an `int`, per <https://docs.python.org/3/library/functions.html#int>.
- Recall that Python comes with several built-in functions, per <https://docs.python.org/3/library/functions.html>.

## Before You Begin
From the root of your repository execute `cd 0-FunctionsVariables` So your current working directory is ...		

		/0-FunctionsVariables $:
Next execute

		mkdir einstein
to make a folder called `einstein` in your codespace.

Then execute

		cd einstein
to change directories into that folder. You should now see your terminal prompt as `/0-FunctionsVariables/einstein $`. You can now execute

		code einstein.py
to make a file called `einstein.py` where you’ll write your program.

# How to Test
Here’s how to test your code manually. At the `einstein/ $` prompt in your terminal: :

1. Run your program with `python einstein.py`. Type `1` and press Enter. Your program should output:

		90000000000000000
2. Run your program with `python einstein.py`. Type `14` and press Enter. Your program should output:

		1260000000000000000
3. Run your program with `python einstein.py`. Type `50` and press Enter. Your program should output:

		4500000000000000000

# Commit your program to GITHUB
At the `/0-FunctionsVariables/einstein $` prompt in your terminal:

		git add -A 
Add all changed files in the repository to be committed

		git commit -m “Upload completed einstein.py“
Commit all changes in the REPO with the comment “Upload completed einstein.py“
*note: If the file is not complete, adjust the comment to describes what is being commited*

		git push 
Push all changes to the REPO