[Home](../README.md) | [Lecture 8](8-OOP.md) | [Problem 8.1](PROBLEM8.1.md) | Problem 8.2 | [Problem 8.3](PROBLEM8.3.md)

# Cookie Jar
<img src="images/giphy1.gif"/> 

_Source: Sesame Street_

Suppose that you’d like to implement a [cookie jar](https://en.wikipedia.org/wiki/Cookie_jar) in which to store cookies. In a file called `jar.py`, implement a `class` called `Jar` with these methods:

- `__init__` should initialize a cookie jar with the given capacity, which represents the maximum number of cookies that can fit in the cookie jar. If `capacity` is not a non-negative `int`, though, `__init__` should instead raise a `ValueError`.
- `__str__` should return a `str` with _n_ 🍪, where _n_ is the number of cookies in the cookie jar. For instance, if there are 3 cookies in the cookie jar, then `str` should return "🍪🍪🍪"
- `deposit` should add _n_ cookies to the cookie jar. If adding that many would exceed the cookie jar’s capacity, though, `deposit` should instead raise a `ValueError`.
- `withdraw` should remove _n_ cookies from the cookie jar. Nom nom nom. If there aren’t that many cookies in the cookie jar, though, `withdraw` should instead raise a `ValueError`.
- `capacity` should return the cookie jar’s capacity.
- `size` should return the number of cookies actually in the cookie jar, initially `0`.
Structure your `class` per the below. You may not alter these methods’ parameters, but you may add your own methods.

		class Jar:
			def __init__(self, capacity=12):
				...

			def __str__(self):
				...

			def deposit(self, n):
				...

			def withdraw(self, n):
				...

			@property
			def capacity(self):
				...

			@property
			def size(self):
				...

> [!NOTE]  
> _Complete these steps after optional lecture 5 Unit Tests_ 

After you implement `jar.py`, additionally implement, in a file called `test_jar.py`, four or more functions that collectively test your implementation of `Jar` thoroughly, each of whose names should begin with `test_` so that you can execute your tests with:

		pytest test_jar.py
Note that it’s not as easy to test instance methods as it is to test functions alone, since instance methods sometimes manipulate the same “state” (i.e., instance variables). To test one method (e.g., `withdraw`), then, you might need to call another method first (e.g., `deposit`). But the method you call first might itself not be correct!

And so programmers sometimes [mock](https://en.wikipedia.org/wiki/Mock_object) (i.e., simulate) state when testing methods, as with Python’s own [mock object library](https://docs.python.org/3/library/unittest.mock.html), so that you can call just the one method but modify the underlying state first, without calling the other method to do so.

For simplicity, though, no need to mock any state. Implement your tests as you normally would!

## Hints  
		from jar import Jar


		def test_init():
			...


		def test_str():
			jar = Jar()
			assert str(jar) == ""
			jar.deposit(1)
			assert str(jar) == "🍪"
			jar.deposit(11)
			assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


		def test_deposit():
			...


		def test_withdraw():
			...

## Before You Begin
From the root of your repository execute `cd 8-OOP` So your current working directory is ...		

		/8-OOP $:
Next execute

		mkdir jar
to make a folder called `jar` in your codespace.

Then execute

		cd jar
to change directories into that folder. You should now see your terminal prompt as `/8-OOP/jar $`. You can now execute

		code jar.py
to make a file called `jar.py` where you’ll write your program.

# How to Test
> [!WARNING]  
> _This teast approach will only make sense after completing the optional Lecture 5 Unit Tests_ 

Here’s how to test your code manually:
1. Open your `test_jar.py` file and import your `Jar` class with from `jar import Jar`. Create a function called `test_init`, wherein you create a new instance of `Jar` with `jar = Jar()`. `assert` that this jar has the capacity it should, then run your tests with `pytest test_jar.py`.
2. Add another function to your `test_jar.py` file called `test_str`. In `test_str`, create a new instance of your `Jar` class and `deposit` a few cookies. `assert` that `str(jar)` prints out as many cookies as have been `deposit`ed, then run your tests with `pytest test_jar.py`.
3. Add another function to your `test_jar.py` file called `test_deposit`. In `test_deposit`, create a new instance of your `Jar` class and `deposit` a few cookies. `assert` that the jar’s `size` attribute is as large as the number of cookies that have been `deposit`ed. Also `assert` that, if you `deposit` more than the jar’s capacity, `deposit` should raise a `ValueError`. Run your tests with `pytest test_jar.py`.
4. Add another function to your `test_jar.py` file called `test_withdraw`. In `test_withdraw`, create a new instance of your `Jar` class and first `deposit` a few cookies. `assert` that `withdraw`ing from the jar leaves the appropriate number of cookies in the jar’s size attribute. Also `assert` that, if you `withdraw` more than the jar’s size, `withdraw` should raise a `ValueError`. Run your tests with `pytest test_jar.py`. 

# Commit your program to GITHUB
At the `/8-OOP/jar $` prompt in your terminal:

		git add -A 
Add all changed files in the repository to be committed

		git commit -m “Upload completed jar.py“
Commit all changes in the REPO with the comment “Upload completed jar.py“
*note: If the file is not complete, adjust the comment to describes what is being commited*

		git push 
Push all changes to the REPO