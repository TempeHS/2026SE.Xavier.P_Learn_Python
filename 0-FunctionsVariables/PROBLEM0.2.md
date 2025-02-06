[Home](../README.md) | [Lecture 0](0-FunctionsVariables.md) | [Problem 0.1](PROBLEM0.1.md) | Problem 0.2 | [Problem 0.3](PROBLEM0.3.md) | [Problem 0.4](PROBLEM0.4.md) | [Problem 0.5](PROBLEM0.5.md)

# Playback Speed

Some people have a habit of lecturing speaking rather quickly, and it’d be nice to slow them down, a la YouTube’s 0.75 playback speed, or even by having them pause between words.

In a file called playback.py, implement a program in Python that prompts the user for input and then outputs that same input, replacing each space with ... (i.e., three periods).

## Hints
- Recall that input returns a str, per <https://docs.python.org/3/library/functions.html#input>.
- Recall that a str comes with quite a few methods, per <https://docs.python.org/3/library/stdtypes.html#string-methods>.

## Before You Begin
From the root of your repository execute `cd 0-FunctionsVariables` So your current working directory is ...		

		/0-FunctionsVariables $:
Next execute

		`mkdir playback`
to make a folder called `playback` in your codespace.

Then execute

		`cd playback`
to change directories into that folder. You should now see your terminal prompt as `/0-FunctionsVariables/playback $`. You can now execute

		`code playback.py`
to make a file called `playback.py` where you’ll write your program.

# How to Test
Here’s how to test your code manually. At the `playback/ $` prompt in your terminal: :

1. Run your program with `python playback.py`. Type `This is CS50` and press `Enter`. Your program should output:

		This...is...CS50
2. Run your program with `python playback.py`. Type `This is our week on functions` and press `Enter`. Your program should output:

		This...is...our...week...on...functions
3. Run your program with `python playback.py`. Type `Let's implement a function called hello` and press Enter. Your program should output:

		Let's...implement...a...function...called...hello

# Commit your program to GITHUB
At the `/0-FunctionsVariables/playback $` prompt in your terminal:

		git add -A 
Add all changed files in the repository to be committed

		`git commit -m “Upload completed playback.py“`
Commit all changes in the REPO with the comment “Upload completed playback.py“
*note: If the file is not complete, adjust the comment to describes what is being commited*

		`git push` 
Push all changes to the REPO