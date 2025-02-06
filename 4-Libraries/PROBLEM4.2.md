[Home](../README.md) | [Lecture 4](4-Libraries.md) | [Problem 4.1](PROBLEM4.1.md) | Problem 4.2 | [Problem 4.3](PROBLEM4.3.md) | [Problem 4.4](PROBLEM4.4.md) | [Problem 4.5](PROBLEM4.5.md) | [Problem 4.6](PROBLEM4.6.md)

# Frank, Ian and Glen’s Letters
[FIGlet](https://en.wikipedia.org/wiki/FIGlet), named after [Frank, Ian, and Glen’s letters](http://www.figlet.org/faq.html), is a program from the early 1990s for making large letters out of ordinary text, a form of ASCII art:

		_ _ _          _   _     _
		| (_) | _____  | |_| |__ (_)___
		| | | |/ / _ \ | __| '_ \| / __|
		| | |   <  __/ | |_| | | | \__ \
		|_|_|_|\_\___|  \__|_| |_|_|___/
Among the fonts supported by FIGlet are those at [figlet.org/examples.html](http://www.figlet.org/examples.html).

FIGlet has since been ported to Python as a module called [pyfiglet](https://pypi.org/project/pyfiglet/0.7/).

In a file called `figlet.py`, implement a program that:

Expects zero or two command-line arguments:
Zero if the user would like to output text in a random font.
Two if the user would like to output text in a specific font, in which case the first of the two should be `-f` or `--font`, and the second of the two should be the name of the font.
Prompts the user for a `str` of text.
Outputs that text in the desired font.
If the user provides two command-line arguments and the first is not `-f` or `--font` or the second is not the name of a font, the program should exit via `sys.exit` with an error message.

## Hints
- You can install `pyfiglet` with:

		pip install pyfiglet
- The documentation for pyfiglet isn’t very clear, but you can use the module as follows:

		from pyfiglet import Figlet
		figlet = Figlet()
You can then get a `list` of available fonts with code like this:

		figlet.getFonts()
You can set the font with code like this, wherein `f` is the font’s name as a `str`:

		figlet.setFont(font=f)
And you can output text in that font with code like this, wherein `s` is that text as a `str`:

		print(figlet.renderText(s))
- Note that the `random` module comes with quite a few functions, per [docs.python.org/3/library/random.html](https://docs.python.org/3/library/random.html).

## Before You Begin
From the root of your repository execute `cd 4-Libraries` So your current working directory is ...		

		/4-Libraries $:
Next execute

		mkdir figlet
to make a folder called `figlet` in your codespace.

Then execute

		cd figlet
to change directories into that folder. You should now see your terminal prompt as `/4-Libraries/figlet $`. You can now execute

		code figlet.py
to make a file called `figlet.py` where you’ll write your program.

# How to Test
Here’s how to test your code manually:
1. Run your program with `python figlet.py` test. Your program should exit via `sys.exit` and print an error message:

		Invalid usage
2. Run your program with `python figlet.py -a slant`. Your program should exit via `sys.exit` and print an error message:

		Invalid usage
3. Run your program with `python figlet.py -f invalid_font`. Your program should exit via `sys.exit` and print an error message:

		Invalid usage
4. Run your program with `python figlet.py -f slant`. Type `CS50`. Your program should print the following:

		___________ __________ 
		/ ____/ ___// ____/ __ \
		/ /    \__ \/___ \/ / / /
		/ /___ ___/ /___/ / /_/ / 
		\____//____/_____/\____/  
5. Run your program with `python figlet.py -f rectangles`. Type `Hello, world`. Your program should print the following:

		_____     _ _                        _   _ 
		|  |  |___| | |___      _ _ _ ___ ___| |_| |
		|     | -_| | | . |_   | | | | . |  _| | . |
		|__|__|___|_|_|___| |  |_____|___|_| |_|___|
						|_|                       
6. Run your program with `python figlet.py -f alphabet`. Type `Moo`. Your program should print the following:

		M   M         
		MM MM         
		M M M ooo ooo 
		M   M o o o o 
		M   M ooo ooo          

# Commit your program to GITHUB
At the `/4-Libraries/figlet $` prompt in your terminal:

		git add -A 
Add all changed files in the repository to be committed

		git commit -m “Upload completed figlet.py“
Commit all changes in the REPO with the comment “Upload completed figlet.py“
*note: If the file is not complete, adjust the comment to describes what is being commited*

		git push 
Push all changes to the REPO