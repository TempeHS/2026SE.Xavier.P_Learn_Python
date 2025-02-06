[Home](../README.md) | [Lecture 5](5-UnitTests.md) | [Problem 5.1](PROBLEM5.1.md) | [Problem 5.2](PROBLEM5.2.md) | Problem 5.3 | [Problem 5.4](PROBLEM5.4.md)

# Re-requesting a Vanity Plate

https://youtu.be/mQZmCJUSC6g

In a file called plates.py, reimplement Vanity Plates from Problem Set 2, restructuring your code per the below, wherein is_valid still expects a str as input and returns True if that str meets all requirements and False if it does not, but main is only called if the value of __name__ is "__main__":

def main():
    ...


def is_valid(s):
    ...


if __name__ == "__main__":
    main()
Then, in a file called test_plates.py, implement four or more functions that collectively test your implementation of is_valid thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

pytest test_plates.py

## Hints
Be sure to include
import plates
or

from plates import is_valid
atop test_plates.py so that you can call is_valid in your tests.

Take care to return, not print, a bool in is_valid. Only main should call print.

## Before You Begin
From the root of your repository execute `cd 5-UnitTests` So your current working directory is ...		

		/5-UnitTests $:
Next execute

		mkdir test_plates
to make a folder called `test_plates` in your codespace.

Then execute

		cd test_plates
to change directories into that folder. You should now see your terminal prompt as `/5-UnitTests/test_plates $`. You can now execute

		code test_plates.py
to make a file called `test_plates.py` where you’ll write your program.

# How to Test
To test your tests, run pytest test_plates.py. Be sure you have a copy of a plates.py file in the same folder. Try to use correct and incorrect versions of plates.py to determine how well your tests spot errors:

Ensure you have a correct version of plates.py. Run your tests by executing pytest test_plates.py. pytest should show that all of your tests have passed.
Modify the correct version of plates.py, perhaps eliminating some of its constraints. Your program might, for example, mistakenly print “Valid” for a license plate of any length! Run your tests by executing pytest test_plates.py. pytest should show that at least one of your tests has failed.
You can execute the below to check your tests using check50, a program CS50 will use to test your code when you submit. (Now there are tests to test your tests!). Be sure to test your tests yourself and determine which tests are needed to ensure plates.py is checked thoroughly.

# Commit your program to GITHUB
At the `/5-UnitTests/test_plates $` prompt in your terminal:

		git add -A 
Add all changed files in the repository to be committed

		git commit -m “Upload completed test_plates.py“
Commit all changes in the REPO with the comment “Upload completed test_plates.py“
*note: If the file is not complete, adjust the comment to describes what is being commited*

		git push 
Push all changes to the REPO
