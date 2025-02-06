[Home](../README.md) | [Lecture 2](2-Loops.md) | [Problem 2.1](PROBLEM2.1.md) | [Problem 2.2](PROBLEM2.2.md) | [Problem 2.3](PROBLEM2.3.md) | Problem 2.4 | [Problem 2.5](PROBLEM2.5.md)

# Vanity Plates

<img src="images/plate.png" width="450" />


In Massachusetts, home to Harvard University, it’s possible to [request a vanity license plate](https://www.mass.gov/how-to/request-a-vanity-license-plate) for your car, with your choice of letters and numbers instead of random ones. Among the requirements, though, are:
- “All vanity plates must start with at least two letters.”
- “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
- “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
- “No periods, spaces, or punctuation marks are allowed.”

In `plates.py`, implement a program that prompts the user for a vanity plate and then output `Valid` if meets all of the requirements or `Invalid` if it does not. Assume that any letters in the user’s input will be uppercase. Structure your program per the below, wherein `is_valid` returns `True` if `s` meets all requirements and `False` if it does not. Assume that s will be a `str`. You’re welcome to implement additional functions for `is_valid` to call (e.g., one function per requirement).

		def main():
			plate = input("Plate: ")
			if is_valid(plate):
				print("Valid")
			else:
				print("Invalid")


		def is_valid(s):
			...


		main()

## Hints
- Recall that a `str` comes with quite a few methods, per [docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods).
- Much like a `list`, a `str` is a “sequence” (of characters), which means it can be [“sliced”](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations) into shorter strings with syntax like `s[i:j]`. For instance, if `s` is `"CS50"`, then `s[0:2]` would be "CS".

## Before You Begin
From the root of your repository execute `cd 2-Loops` So your current working directory is ...		

		/2-Loops $:
Next execute

		mkdir plates
to make a folder called `plates` in your codespace.

Then execute

		cd plates
to change directories into that folder. You should now see your terminal prompt as `/2-Loops/plates $`. You can now execute

		code plates.py
to make a file called `plates.py` where you’ll write your program.

# How to Test
Here’s how to test your code manually:

1. Run your program with `python plates.py`. Type `CS50` and press Enter. Your program should output:

		Valid
2. Run your program with `python plates.py`. Type `CS05` and press Enter. Your program should output:

		Invalid
3. Run your program with `python plates.py`. Type `CS50P` and press Enter. Your program should output

		Invalid
4. Run your program with `python plates.py`. Type `PI3.14` and press Enter. Your program should output

		Invalid
5. Run your program with `python plates.py`. Type `H` and press Enter. Your program should output

		Invalid
6. Run your program with `python plates.py`. Type `OUTATIME` and press Enter. Your program should output

		Invalid

# Commit your program to GITHUB
At the `/2-Loops/plates $` prompt in your terminal:

		git add -A 
Add all changed files in the repository to be committed

		git commit -m “Upload completed plates.py“
Commit all changes in the REPO with the comment “Upload completed plates.py“
*note: If the file is not complete, adjust the comment to describes what is being commited*

		git push 
Push all changes to the REPO
