[Home](../README.md) | [Lecture 3](3-Exceptions.md) | [Problem 3.1](PROBLEM3.1.md) | Problem 3.2 | [Problem 3.3](PROBLEM3.3.md) | [Problem 3.4](PROBLEM3.4.md)

# Felipe’s Taqueria
<img src="images/felipes-logo.png" width="300" />

One of the most popular places to eat in [Harvard Square](https://en.wikipedia.org/wiki/Harvard_Square) is [Felipe’s Taqueria](https://www.felipesboston.com/), which offers a [menu[(https://www.felipesboston.com/menu)] of entrees, per the `dict` below, wherein the value of each key is a price in dollars:

		{
			"Baja Taco": 4.25,
			"Burrito": 7.50,
			"Bowl": 8.50,
			"Nachos": 11.00,
			"Quesadilla": 8.50,
			"Super Burrito": 8.50,
			"Super Quesadilla": 9.50,
			"Taco": 3.00,
			"Tortilla Salad": 8.00
		}
In a file called `taqueria.py`, implement a program that enables a user to place an order, prompting them for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign ($) and formatted to two decimal places. Treat the user’s input case insensitively. Ignore any input that isn’t an item. Assume that every item on the menu will be [titlecased](https://docs.python.org/3/library/stdtypes.html#str.title).

## Hints
- Note that you can detect when the user has inputted control-d by catching an `[EOFError](https://docs.python.org/3/library/exceptions.html#EOFError)` with code like:

		try:
			item = input()
		except EOFError:
			...
You might want to print a new line so that the user’s cursor (and subsequent prompt) doesn’t remain on the same line as your program’s own prompt.

- Inputting control-d does not require inputting Enter as well, and so the user’s cursor (and subsequent prompt) might thus remain on the same line as your program’s own prompt. You can move the user’s cursor to a new line by printing `\n` yourself!
- Note that a `dict` comes with quite a few methods, [per docs.python.org/3/library/stdtypes.html#mapping-types-dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict), among them `get`, and supports operations like:

		d[key]
		and

		if key in d:
			...
wherein `d` is a `dict` and `key` is a `str`.

Be sure to avoid or catch any [KeyError](https://docs.python.org/3/library/exceptions.html#KeyError).

## Before You Begin
From the root of your repository execute `cd 3-Exceptions` So your current working directory is ...		

		/3-Exceptions $:
Next execute

		mkdir taqueria
to make a folder called `taqueria` in your codespace.

Then execute

		cd taqueria
to change directories into that folder. You should now see your terminal prompt as `/3-Exceptions/taqueria $`. You can now execute

		code taqueria.py
to make a file called `taqueria.py` where you’ll write your program.

# How to Test
Here’s how to test your code manually:

1. Run your program with `python taqueria.py`. Type `Taco` and press Enter, then type `Taco` again and press Enter. Your program should output:

		Total: $6.00  
and continue prompting the user until they input control-d.

2. Run your program with `python taqueria.py`. Type `Baja Taco` and press Enter, then type `Tortilla Salad` and press enter. Your program should output:

		Total: $12.25
and continue prompting the user until they input control-d.

3. Run your program with `python taqueria.py`. Type `Burger` and press Enter. Your program should reprompt the user.

4. Be sure to try other foods and vary the casing of your input. Your program should behave as expected, case-insensitively.

# Commit your program to GITHUB
At the `/3-Exceptions/taqueria $` prompt in your terminal:

		git add -A 
Add all changed files in the repository to be committed

		git commit -m “Upload completed taqueria.py“
Commit all changes in the REPO with the comment “Upload completed taqueriataqueria.py“
*note: If the file is not complete, adjust the comment to describes what is being commited*

		git push 
Push all changes to the REPO