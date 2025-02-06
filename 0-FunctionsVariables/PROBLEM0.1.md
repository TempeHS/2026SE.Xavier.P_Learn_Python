[Home](../README.md) | [Lecture 0](0-FunctionsVariables.md) | Problem 0.1 | [Problem 0.2](PROBLEM0.2.md) | [Problem 0.3](PROBLEM0.3.md) | [Problem 0.4](PROBLEM0.4.md) | [Problem 0.5](PROBLEM0.5.md)

# Indoor Voice

WRITING IN ALL CAPS IS LIKE YELLING.

Best to use your “indoor voice” sometimes, writing entirely in lowercase.

In a file called `indoor.py`, implement a program in Python that prompts the user for input and then outputs that same input in lowercase. Punctuation and whitespace should be outputted unchanged. You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input.

## Hints
- Recall that input returns a str, per <https://docs.python.org/3/library/functions.html#input>.
- Recall that a str comes with quite a few methods, per <https://docs.python.org/3/library/stdtypes.html#string-methods>.

## Before You Begin
From the root of your repository execute `cd 0-FunctionsVariables` So your current working directory is ...		

		/0-FunctionsVariables $:
Next execute

		`mkdir indoor`
to make a folder called `indoor` in your codespace.

Then execute

		`cd indoor`
to change directories into that folder. You should now see your terminal prompt as `/0-FunctionsVariables/indoor $`. You can now execute

		`code indoor.py`
to make a file called `indoor.py` where you’ll write your program.

# How to Test
Here’s how to test your code manually. At the `indoor/ $` prompt in your terminal: :

1. Run your program with `python indoor.py`. Type `HELLO` and press Enter. Your program should output:

		hello
2. Run your program with `python indoor.py`. Type `THIS IS CS50` and press Enter. Your program should output:

		this is cs50
3. Run your program with `python indoor.py`. Type `50` and press Enter. Your program should output:

		50

# Commit your program to GITHUB
At the `/0-FunctionsVariables/indoor $` prompt in your terminal:

		git add -A 
Add all changed files in the repository to be committed

		git commit -m “Upload completed indoor.py“
Commit all files that have been `add`ed in the REPO with the comment “Upload completed indoor.py“
_note: If the file is not complete, adjust the comment to describes what is being commited_

		git push
Push all changes to the REPO