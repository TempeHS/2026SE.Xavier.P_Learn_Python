[Home](../README.md) | [Lecture 5](5-UnitTests.md) | [Problem 5.1](PROBLEM5.1.md) | [Problem 5.2](PROBLEM5.2.md) | [Problem 5.3](PROBLEM5.3.md) | Problem 5.4

# Refueling

In a file called fuel.py, reimplement Fuel Gauge from Problem Set 3, restructuring your code per the below, wherein:

convert expects a str in X/Y format as input, wherein each of X and Y is an integer, and returns that fraction as a percentage rounded to the nearest int between 0 and 100, inclusive. If X and/or Y is not an integer, or if X is greater than Y, then convert should raise a ValueError. If Y is 0, then convert should raise a ZeroDivisionError.
gauge expects an int and returns a str that is:
"E" if that int is less than or equal to 1,
"F" if that int is greater than or equal to 99,
and "Z%" otherwise, wherein Z is that same int.
def main():
    ...


def convert(fraction):
    ...


def gauge(percentage):
    ...


if __name__ == "__main__":
    main()
Then, in a file called test_fuel.py, implement two or more functions that collectively test your implementations of convert and gauge thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

pytest test_fuel.py

## Hints
Be sure to include
import fuel
or

from fuel import convert, gauge
atop test_fuel.py so that you can call convert and gauge in your tests.

Take care to return, not print, an int in convert and a str in gauge. Only main should call print.
Note that you can check with pytest whether a function has raised an exception, per docs.pytest.org/en/latest/how-to/assert.html#assertions-about-expected-exceptions.s

## Before You Begin
From the root of your repository execute `cd 5-UnitTests` So your current working directory is ...		

		/5-UnitTests $:
Next execute

		mkdir test_fuel.py
to make a folder called `test_fuel` in your codespace.

Then execute

		cd test_fuel
to change directories into that folder. You should now see your terminal prompt as `/5-UnitTests/test_fuel $`. You can now execute

		code test_fuel.py
to make a file called `test_fuel.py` where you’ll write your program.

# How to Test
To test your tests, run pytest test_fuel.py. Be sure you have a copy of a fuel.py file in the same folder. Try to use correct and incorrect versions of fuel.py to determine how well your tests spot errors:

Ensure you have a correct version of fuel.py. Run your tests by executing pytest test_fuel.py. pytest should show that all of your tests have passed.
Modify the correct version of fuel.py, changing the return values of convert. Your program might, for example, mistakenly return a str instead of an int. Run your tests by executing pytest test_fuel.py. pytest should show that at least one of your tests has failed.
Similarly, modify the correct version of fuel.py, changing the return values of gauge. Your program might, for example, mistakenly omit a % in the resulting str. Run your tests by executing pytest test_fuel.py. pytest should show that at least one of your tests has failed.

# Commit your program to GITHUB
At the `/5-UnitTests/test_fuel $` prompt in your terminal:

		git add -A 
Add all changed files in the repository to be committed

		git commit -m “Upload completed test_fuel.py“
Commit all changes in the REPO with the comment “Upload completed test_fuel.py“
*note: If the file is not complete, adjust the comment to describes what is being commited*

		git push 
Push all changes to the REPO
