[Home](../README.md) | [Lecture 4](4-Libraries.md) | [Problem 4.1](PROBLEM4.1.md) | [Problem 4.2](PROBLEM4.2.md) | Problem 4.3 | [Problem 4.4](PROBLEM4.4.md) | [Problem 4.5](PROBLEM4.5.md) | [Problem 4.6](PROBLEM4.6.md)

# Adieu, Adieu
Watch: https://youtu.be/Qy9_lfjQopU

In [The Sound of Music](https://en.wikipedia.org/wiki/The_Sound_of_Music_(film)), there’s a song sung largely in English, [So Long, Farewell](https://www.youtube.com/watch?v=Qy9_lfjQopU), with these [lyrics](https://www.lyrics.com/lyric/3998488/Julie+Andrews/So+Long%2C+Farewell), wherein “adieu” means “goodbye” in French:

> Adieu, adieu, to yieu and yieu and yieu

Of course, the line isn’t grammatically correct, since it would typically be written (with an [Oxford comma](https://en.wikipedia.org/wiki/Serial_comma)) as:

> Adieu, adieu, to yieu, yieu, and yieu

To be fair, “yieu” isn’t even a word; it just rhymes with “you”!

In a file called `adieu.py`, implement a program that prompts the user for names, one per line, until the user inputs control-d. Assume that the user will input at least one name. Then bid adieu to those names, separating two names with one `and`, three names with two commas and one `and`, and _n_ names with _n-1_ commas and one `and`, as in the below:

> Adieu, adieu, to Liesl  
> Adieu, adieu, to Liesl and Friedrich  
> Adieu, adieu, to Liesl, Friedrich, and Louisa  
> Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt  
> Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta  
> Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta  
> Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl  

## Hints
- Note that the `inflect` module comes with quite a few methods, per [pypi.org/project/inflect](https://pypi.org/project/inflect/). You can install it with:

		pip install inflect

## Before You Begin
From the root of your repository execute `cd 4-Libraries` So your current working directory is ...		

		/4-Libraries $:
Next execute

		mkdir adieu
to make a folder called `adieu` in your codespace.

Then execute

		cd adieu
to change directories into that folder. You should now see your terminal prompt as `/4-Libraries/adieu $`. You can now execute

		code adieu.py
to make a file called `adieu.py` where you’ll write your program.

# How to Test
Here’s how to test your code manually:

1. Run your program with `python adieu.py`. Type `Liesl` and press Enter, followed by control-d. Your program should output:

		Adieu, adieu, to Liesl 
2. Run your program with `python adieu.py`. Type `Liesl` and press Enter, then type `Friedrich` and press Enter, followed by control-d. Your program should output:

		Adieu, adieu, to Liesl and Friedrich
3. Run your program with `python adieu.py`. Type `Liesl` and press Enter, then type `Friedrich` and press Enter. Now type `Louisa` and press Enter, followed by control-d. Your program should output:

		Adieu, adieu, to Liesl, Friedrich, and Louisa

# Commit your program to GITHUB
At the `/4-Libraries/adieu $` prompt in your terminal:

		git add -A 
Add all changed files in the repository to be committed

		git commit -m “Upload completed adieu.py“
Commit all changes in the REPO with the comment “Upload completed adieu.py“
*note: If the file is not complete, adjust the comment to describes what is being commited*

		git push 
Push all changes to the REPO