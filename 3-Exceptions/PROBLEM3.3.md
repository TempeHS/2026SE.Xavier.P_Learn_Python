[Home](../README.md) | [Lecture 3](3-Exceptions.md) | [Problem 3.1](PROBLEM3.1.md) | [Problem 3.2](PROBLEM3.2.md) | Problem 3.3 | [Problem 3.4](PROBLEM3.4.md)

# Grocery List
Suppose that you’re in the habit of making a list of items you need from the grocery store.

In a file called `grocery.py`, implement a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item. No need to pluralize the items. Treat the user’s input case-insensitively.

Hints


## Hints
- Note that you can detect when the user has inputted control-d by catching an `[EOFError](https://docs.python.org/3/library/exceptions.html#EOFError)` with code like:

		try:
			item = input()
		except EOFError:
			...
- Odds are you’ll want to store your grocery list as a `dict`.
- Note that a `dict` comes with quite a few methods, per [docs.python.org/3/library/stdtypes.html#mapping-types-dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict), among them `get`, and supports operations like:

		d[key]
and

		if key in d:
			...
wherein `d` is a `dict` and `key` is a `str`.

Be sure to avoid or catch any `[KeyError](https://docs.python.org/3/library/exceptions.html#KeyError)`.

## Before You Begin
From the root of your repository execute `cd 3-Exceptions` So your current working directory is ...		

		/3-Exceptions $:
Next execute

		mkdir grocery
to make a folder called `grocery` in your codespace.

Then execute

		cd grocery
to change directories into that folder. You should now see your terminal prompt as `/3-Exceptions/grocery $`. You can now execute

		code grocery.py
to make a file called `grocery.py` where you’ll write your program.

# How to Test
Here’s how to test your code manually:

1. Run your program with `python grocery.py`. Type `mango` and press Enter, then type `strawberry` and press Enter, followed by control-d. Your program should output:

		1 MANGO
		1 STRAWBERRY
2. Run your program with `python grocery.py`. Type `milk` and press Enter, then type `milk` again and press Enter, followed by control-d. Your program should output:

		2 MILK
3. Run your program with `python grocery.py`. Type `tortilla` and press Enter, then type `sweet potato` and press Enter, followed by control-d. Your program should output:

		1 SWEET POTATO
		1 TORTILLA

# Commit your program to GITHUB
At the `/3-Exceptions/grocery $` prompt in your terminal:

		git add -A 
Add all changed files in the repository to be committed

		git commit -m “Upload completed grocery.py“
Commit all changes in the REPO with the comment “Upload completed grocery.py“
*note: If the file is not complete, adjust the comment to describes what is being commited*

		git push 
Push all changes to the REPO
