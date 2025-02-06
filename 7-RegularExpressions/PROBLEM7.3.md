# Working 9 to 5

https://youtu.be/UbxUSsFXYo4

Whereas most countries use a 24-hour clock, the United States tends to use a 12-hour clock. Accordingly, instead of “09:00 to 17:00”, many Americans would say they work “9:00 AM to 5:00 PM” (or “9 AM to 5 PM”), wherein “AM” is an abbreviation for “ante meridiem” and “PM” is an abbreviation for “post meridiem”, wherein “meridiem” means midday (i.e., noon).

Conversion Table
In a file called working.py, implement a function called convert that expects a str in either of the 12-hour formats below and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00). Expect that AM and PM will be capitalized (with no periods therein) and that there will be a space before each. Assume that these times are representative of actual times, not necessarily 9:00 AM and 5:00 PM specifically.

9:00 AM to 5:00 PM
9 AM to 5 PM
Raise a ValueError instead if the input to convert is not in either of those formats or if either time is invalid (e.g., 12:60 AM, 13:00 PM, etc.). But do not assume that someone’s hours will start ante meridiem and end post meridiem; someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).

Structure working.py as follows, wherein you’re welcome to modify main and/or implement other functions as you see fit, but you may not import any other libraries. You’re welcome, but not required, to use re and/or sys.

import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    ...


...


if __name__ == "__main__":
    main()
Either before or after you implement convert in working.py, additionally implement, in a file called test_working.py, three or more functions that collectively test your implementation of convert thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

pytest test_working.py

## Hints
Recall that the re module comes with quite a few functions, per docs.python.org/3/library/re.html, including search.
Recall that regular expressions support quite a few special characters, per docs.python.org/3/library/re.html#regular-expression-syntax.
Because backslashes in regular expressions could be mistaken for escape sequences (like \n), best to use Python’s raw string notation for regular expression patterns, else pytest will warn with DeprecationWarning: invalid escape sequence. Just as format strings are prefixed with f, so are raw strings prefixed with r. For instance, instead of "harvard\.edu", use r"harvard\.edu".
Note that re.search, if passed a pattern with “capturing groups” (i.e., parentheses), returns a “match object,” per docs.python.org/3/library/re.html#match-objects, wherein matches are 1-indexed, which you can access individually with group, per docs.python.org/3/library/re.html#re.Match.group, or collectively with groups, per docs.python.org/3/library/re.html#re.Match.groups.
Note that you can format an int with leading zeroes with code like
print(f"{n:02}")
wherein, if n is a single digit, it will be prefixed with one 0, per docs.python.org/3/library/string.html#format-string-syntax.

## Before You Begin
From the root of your repository execute `cd 7-RegularExpressions` So your current working directory is ...		

		/7-RegularExpressions $:
Next execute

		mkdir working
to make a folder called `working` in your codespace.

Then execute

		cd working
to change directories into that folder. You should now see your terminal prompt as `/7-RegularExpressions/working $`. You can now execute

		code working.py
to make a file called `working.py` where you’ll write your program.

# How to Test
How to Test working.py
Here’s how to test working.py manually:

Run your program with python working.py. Ensure your program prompts you for a time. Type 9 AM to 5 PM, followed by Enter. Your program should output 09:00 to 17:00.
Run your program with python working.py. Type 9:00 AM to 5:00 PM, followed by Enter. Your program should again output 09:00 to 17:00.
Run your program with python working.py. Ensure your program prompts you for a time. Type 10 PM to 8 AM, followed by Enter. Your program should output 22:00 to 08:00.
Run your program with python working.py. Ensure your program prompts you for a time. Type 10:30 PM to 8:50 AM, followed by Enter. Your program should again output 22:30 to 08:50.
Run your program with python working.py. Ensure your program prompts you for a time. Try intentionally inducing a ValueError by typing 9:60 AM to 5:60 PM, followed by Enter. Your program should indeed raise a ValueError.
Run your program with python working.py. Ensure your program prompts you for a time. Try intentionally inducing a ValueError by typing 9 AM - 5 PM, followed by Enter. Your program should indeed raise a ValueError.
Run your program with python working.py. Ensure your program prompts you for a time. Try intentionally inducing a ValueError by typing 09:00 AM - 17:00 PM, followed by Enter. Your program should indeed raise a ValueError.
How to Test test_working.py
To test your tests, run pytest test_working.py. Try to use correct and incorrect versions of working.py to determine how well your tests spot errors:

Ensure you have a correct version of working.py. Run your tests by executing pytest test_working.py. pytest should show that all of your tests have passed.
Modify the correct version of working.py, particularly its function convert. Your program might, for example, fail to raise a ValueError when it should. Run your tests by executing pytest test_working.py. pytest should show that at least one of your tests has failed.
Similarly, modify the correct version of working.py, changing the return values of convert. Your program might, for example, mistakenly omit minutes. Run your tests by executing pytest test_working.py. pytest should show that at least one of your tests has failed.

# Commit your program to GITHUB
At the `/7-RegularExpressions/working $` prompt in your terminal:

		git add -A 
Add all changed files in the repository to be committed

		git commit -m “Upload completed working.py“
Commit all changes in the REPO with the comment “Upload completed working.py“
*note: If the file is not complete, adjust the comment to describes what is being commited*

		git push 
Push all changes to the REPO
