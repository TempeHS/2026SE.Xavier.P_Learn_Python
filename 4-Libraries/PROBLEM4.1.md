[Home](../README.md) | [Lecture 4](4-Libraries.md) | Problem 4.1 | [Problem 4.2](PROBLEM4.2.md) | [Problem 4.3](PROBLEM4.3.md) | [Problem 4.4](PROBLEM4.4.md) | [Problem 4.5](PROBLEM4.5.md) | [Problem 4.6](PROBLEM4.6.md)

# Emojize
Because emoji aren’t quite as easy to type as text, at least on laptops and desktops, some programs support “codes,” whereby you can type, for instance, `:thumbs_up:`, which will be automatically converted to 👍. Some programs additionally support aliases, whereby you can more succinctly type, for instance, `:thumbsup:`, which will also be automatically converted to 👍.

See [carpedm20.github.io/emoji/all.html?enableList=enable_list_alias](https://carpedm20.github.io/emoji/all.html?enableList=enable_list_alias) for a list of codes with aliases.

In a file called `emojize.py`, implement a program that prompts the user for a `str` in English and then outputs the “emojized” version of that `str`, converting any codes (or aliases) therein to their corresponding emoji.

## Hints
- Note that the `emoji` module comes with two functions, per [pypi.org/project/emoji](https://pypi.org/project/emoji/), one of which is `emojize`, which takes an optional, named parameter called language. You can install it with:

		pip install emoji

## Before You Begin
From the root of your repository execute `cd 4-Libraries` So your current working directory is ...		

		/4-Libraries $:
Next execute

		mkdir emojize
to make a folder called `emojize` in your codespace.

Then execute

		cd emojize
to change directories into that folder. You should now see your terminal prompt as `/4-Libraries/emojize $`. You can now execute

		code emojize.py
to make a file called `emojize.py` where you’ll write your program.

# How to Test
Here’s how to test your code manually:

1. Run your program with `python emojize.py`. Type `:1st_place_medal:` and press Enter. Your program should output:

		Output: 🥇
2. Run your program with `python emojize.py`. Type `:money_bag:` and press Enter. Your program should output:

		Output: 💰
3. Run your program with `python emojize.py`. Type `:smile_cat:` and press Enter. Your program should output:

		Output: 😸

# Commit your program to GITHUB
At the `/4-Libraries/emojize $` prompt in your terminal:

		git add -A 
Add all changed files in the repository to be committed

		git commit -m “Upload completed emojize.py“
Commit all changes in the REPO with the comment “Upload completed emojize.py“
*note: If the file is not complete, adjust the comment to describes what is being commited*

		git push 
Push all changes to the REPO
