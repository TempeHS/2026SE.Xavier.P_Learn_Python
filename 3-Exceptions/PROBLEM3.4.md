[Home](../README.md) | [Lecture 3](3-Exceptions.md) | [Problem 3.1](PROBLEM3.1.md) | [Problem 3.2](PROBLEM3.2.md) | [Problem 3.3](PROBLEM3.3.md) | Problem 3.4

# Outdated

In the United States, dates are typically formatted in [month-day-year order](https://en.wikipedia.org/wiki/Date_and_time_notation_in_the_United_States) (MM/DD/YYYY), otherwise known as [middle-endian](https://en.wikipedia.org/wiki/Endianness#Middle-endian) order, which is arguably bad design. Dates in that format can’t be easily sorted because the date’s year comes last instead of first. Try sorting, for instance, `2/2/1800`, `3/3/1900`, and `1/1/2000` chronologically in any program (e.g., a spreadsheet). Dates in that format are also ambiguous. [Harvard](https://www.harvard.edu/about/history/) was founded on September 8, 1636, but 9/8/1636 could also be interpreted as August 9, 1636!

Fortunately, computers tend to use [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601), an international standard that prescribes that dates should be formatted in year-month-day (YYYY-MM-DD) order, no matter the country, formatting years with four digits, months with two digits, and days with two digits, “padding” each with leading zeroes as needed.

In a file called `outdated.py`, implement a program that prompts the user for a date, [anno Domini](https://en.wikipedia.org/wiki/Anno_Domini), in month-day-year order, formatted like `9/8/1636` or `September 8, 1636`, wherein the month in the latter might be any of the values in the `list` below:

		[
			"January",
			"February",
			"March",
			"April",
			"May",
			"June",
			"July",
			"August",
			"September",
			"October",
			"November",
			"December"
		]
Then output that same date in `YYYY-MM-DD` format. If the user’s input is not a valid date in either format, prompt the user again. Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.

## Hints
- Recall that a `str` comes with quite a few methods, per [docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods), including `split`.
- Recall that a `list` comes with quite a few methods, per [docs.python.org/3/tutorial/datastructures.html#more-on-lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists), among which is `index`.
- Note that you can format an `int` with leading zeroes with code like

		print(f"{n:02}")
wherein, if `n` is a single digit, it will be prefixed with one `0`, per [docs.python.org/3/library/string.html#format-string-syntax](https://docs.python.org/3/library/string.html#format-string-syntax).

## Before You Begin
From the root of your repository execute `cd 3-Exceptions` So your current working directory is ...		

		/3-Exceptions $:
Next execute

		mkdir outdated
to make a folder called `outdated` in your codespace.

Then execute

		cd outdated
to change directories into that folder. You should now see your terminal prompt as `/3-Exceptions/outdated $`. You can now execute

		code outdated.py
to make a file called `outdated.py` where you’ll write your program.

# How to Test
Here’s how to test your code manually:

1. Run your program with `python outdated.py`. Type `9/8/1636` and press Enter. Your program should output:

		1636-09-08
2. Run your program with `python outdated.py`. Type `September 8, 1636` and press Enter. Your program should output:

		1636-09-08
3. Run your program with `python outdated.py`. Type `23/6/1912` and press Enter. Your program should reprompt the user.

4. Run your program with `python outdated.py`. Type `December 80, 1980` and press Enter. Your program should reprompt the user.

# Commit your program to GITHUB
At the `/3-Exceptions/outdated $` prompt in your terminal:

		git add -A 
Add all changed files in the repository to be committed

		git commit -m “Upload completed outdated.py“
Commit all changes in the REPO with the comment “Upload completed outdated.py“
*note: If the file is not complete, adjust the comment to describes what is being commited*

		git push 
Push all changes to the REPO
