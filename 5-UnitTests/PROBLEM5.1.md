[Home](../README.md) | [Lecture 5](5-UnitTests.md) | Problem 5.1 | [Problem 5.2](PROBLEM5.2.md) | [Problem 5.3](PROBLEM5.3.md) | [Problem 5.4](PROBLEM5.4.md)

# Testing my twttr

In a file called `twttr.py`, reimplement Setting up my twttr from Problem Set 2, restructuring your code per the below, wherein shorten expects a str as input and returns that same str but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

		def main():
			...


		def shorten(word):
			...


		if __name__ == "__main__":
			main()
Then, in a file called test_twttr.py, implement one or more functions that collectively test your implementation of shorten thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

		pytest test_twttr.py

## Hints
- Be sure to include

		import twttr
*or*

		from twttr import shorten
atop `test_twttr.py` so that you can call shorten in your tests.

- Take care to return, not print, a `st`r in shorten. Only `main` should call print.

## Before You Begin
From the root of your repository execute `cd 5-UnitTests` So your current working directory is ...		

		/5-UnitTests $:
Next execute

		mkdir test_twttr
to make a folder called `test_twttr` in your codespace.

Then execute

		cd `test_twttr`
to change directories into that folder. You should now see your terminal prompt as `/5-UnitTests/test_twttr $`. You can now execute

		code test_twttr.py
to make a file called `test_twttr.py` where you’ll write your program.

# How to Test
To test your tests, run pytest test_twttr.py. Be sure you have a copy of a twttr.py file in the same folder. Try to use correct and incorrect versions of twttr.py to determine how well your tests spot errors:

Ensure you have a correct version of twttr.py. Run your tests by executing pytest test_twttr.py. pytest should show that all of your tests have passed.
Modify the correct version of twttr.py in such a way as to create a bug. Your program might, for example, mistakenly only omit lowercase vowels! Run your tests by executing pytest test_twttr.py. pytest should show that at least one of your tests has failed.

# Commit your program to GITHUB
At the `/5-UnitTests/test_twttr $` prompt in your terminal:

		git add -A 
Add all changed files in the repository to be committed

		git commit -m “Upload completed test_twttr.py“
Commit all changes in the REPO with the comment “Upload completed test_twttr.py“
*note: If the file is not complete, adjust the comment to describes what is being commited*

		git push 
Push all changes to the REPO
