[Home](../README.md) | [Lecture 4](4-Libraries.md) | [Problem 4.1](PROBLEM4.1.md) | [Problem 4.2](PROBLEM4.2.md) | [Problem 4.3](PROBLEM4.3.md) | [Problem 4.4](PROBLEM4.4.md) | Problem 4.5 | [Problem 4.6](PROBLEM4.6.md)

# Little Professor
Watch: https://youtu.be/ZuJwzH9BIgs

One of David’s first toys as a child, funny enough, was [Little Professor](https://en.wikipedia.org/wiki/Little_Professor), a “calculator” that would generate ten different math problems for David to solve. For instance, if the toy were to display `4 + 0 =` , David would (hopefully) answer with `4`. If the toy were to display `4 + 1 =` , David would (hopefully) answer with `5`. If David were to answer incorrectly, the toy would display `EEE`. And after three incorrect answers for the same problem, the toy would simply display the correct answer (e.g., `4 + 0 = 4` or `4 + 1 = 5`).

In a file called `professor.py`, implement a program that:

Prompts the user for a level, 
- If the user does not input `1`, `2`, or `3`, the program should prompt again.
- Randomly generates ten (10) math problems formatted as `X + Y =` , wherein each of `X` and `Y` is a non-negative integer with _n_ digits. No need to support operations other than addition (`+`).
- Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program should output `EEE` and prompt the user again, allowing the user up to three tries in total for that problem. If the user has still not answered correctly after three tries, the program should output the correct answer.
- The program should ultimately output the user’s score: the number of correct answers out of 10.
Structure your program as follows, wherein `get_level` prompts (and, if need be, re-prompts) the user for a level and returns `1`, `2`, or `3`, and `generate_integer` returns a randomly generated non-negative integer with `level` digits or raises a `ValueError` if `level` is not `1`, `2`, or `3`:

		import random


		def main():
			...


		def get_level():
			...


		def generate_integer(level):
			...


		if __name__ == "__main__":
			main()


## Hints
- Note that you can raise an exception like `ValueError` with code like:

		raise ValueError
- Note that the `random` module comes with quite a few functions, per [docs.python.org/3/library/random.html](https://docs.python.org/3/library/random.html).

## Before You Begin
From the root of your repository execute `cd 4-Libraries` So your current working directory is ...		

		/4-Libraries $:
Next execute

		mkdir professor
to make a folder called `professor` in your codespace.

Then execute

		cd professor
to change directories into that folder. You should now see your terminal prompt as `/4-Libraries/professor $`. You can now execute

		code professor.py
to make a file called `professor.py` where you’ll write your program.

# How to Test
Here’s how to test your code manually:

1. Run your program with `python professor.py`. Type `-1` and press Enter. Your program should reprompt you:

		Level:   
2. Run your program with `python professor.py`. Type `4` and press Enter. Your program should reprompt you:

		Level:   
3. Run your program with `python professor.py`. Type `1` and press Enter. Your program should begin posing addition problems with positive, single-digit integers. For example:

		6 + 6 =    
Your program should output 10 distinct problems before printing the number of questions you answered correctly and exiting.
4. Run your program with `python professor.py`. Type `1` and press Enter. Answer the first question incorrectly. Your program should output:

		EEE
before reprompting you with the same question.
5. Run your program with `python professor.py`. Type `1` and press Enter. Answer the first question incorrectly, three times. Your program should output the correct answer. For example:

		6 + 6 = 12
and then move on to another question. Answer the remaining questions correctly. Your program should output a score of `9`.
6. Run your program with `python professor.py`. Type `1` and press Enter. Answer all 10 questions correctly. Your program should output a score of `10`.

# Commit your program to GITHUB
At the `/4-Libraries/professor $` prompt in your terminal:

		git add -A 
Add all changed files in the repository to be committed

		git commit -m “Upload completed professor.py“
Commit all changes in the REPO with the comment “Upload completed professor.py“
*note: If the file is not complete, adjust the comment to describes what is being commited*

		git push 
Push all changes to the REPO