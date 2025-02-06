# Response Validation

When creating a Google Form that prompts users for a short answer (or paragraph), it’s possible to enable response validation and require that the user’s input match a regular expression. For instance, you could require that a user input an email address with a regex like this one:

^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$
Or you could more easily use Google’s built-in support for validating an email address, per the screenshot below, much like you could use a library in your own code:

Google Form

In a file called response.py, using either validator-collection or validators from PyPI, implement a program that prompts the user for an email address via input and then prints Valid or Invalid, respectively, if the input is a syntatically valid email address. You may not use re. And do not validate whether the email address’s domain name actually exists.


## Hints
Note that you can install validator-collection with:
pip install validator-collection
Click Homepage to find your way to the library’s documentation.

Note that you can install validators with:
pip install validators
Click Homepage to find your way to the library’s documentation.

## Before You Begin
From the root of your repository execute `cd 7-RegularExpressions` So your current working directory is ...		

		/7-RegularExpressions $:
Next execute

		mkdir response
to make a folder called `response` in your codespace.

Then execute

		cd response
to change directories into that folder. You should now see your terminal prompt as `/7-RegularExpressions/response $`. You can now execute

		code response.py
to make a file called `response.py` where you’ll write your program.

# How to Test
Here’s how to test your code manually:

Run your program with python response.py. Ensure your program prompts you for an email, then type malan@harvard.edu, followed by Enter. Your program should output Valid.
Run your program with python response.py. Type your own email, followed by Enter. Your program should output Valid.
Run your program with python response.py. Type malan@@@harvard.edu, followed by Enter. Your program should output Invalid.
Run your program with python response.py. Mistype your own email, including an extra . before .com, for example. Press enter and your program should output Invalid.


# Commit your program to GITHUB
At the `/7-RegularExpressions/response $` prompt in your terminal:

		git add -A 
Add all changed files in the repository to be committed

		git commit -m “Upload completed response.py“
Commit all changes in the REPO with the comment “Upload completed response.py“
*note: If the file is not complete, adjust the comment to describes what is being commited*

		git push 
Push all changes to the REPO