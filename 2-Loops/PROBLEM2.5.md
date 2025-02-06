[Home](../README.md) | [Lecture 2](2-Loops.md) | [Problem 2.1](PROBLEM2.1.md) | [Problem 2.2](PROBLEM2.2.md) | [Problem 2.3](PROBLEM2.3.md) | [Problem 2.4](PROBLEM2.4.md) | Problem 2.5

# Nutrition Facts

The U.S. Food & Drug Adminstration (FDA) offers [downloadable/printable posters](https://www.fda.gov/food/food-labeling-nutrition/nutrition-information-raw-fruits-vegetables-and-fish) that “show nutrition information for the 20 most frequently consumed raw fruits … in the United States. Retail stores are welcome to download the posters, print, display and/or distribute them to consumers in close proximity to the relevant foods in the stores.”

In a file called `nutrition.py`, implement a program that prompts ~~consumers~~ users to input a fruit (case-insensitively) and then outputs the number of calories in one portion of that fruit, per the [FDA’s poster for fruits](https://cs50.harvard.edu/python/2022/psets/2/nutrition/Nutrition-Information-for-Raw-Fruits---small-PDF-Poster.pdf), which is also [available as text](https://www.fda.gov/food/food-labeling-nutrition/raw-fruits-poster-text-version-accessible-version). Capitalization aside, assume that users will input fruits exactly as written in the poster (e.g., `strawberries`, not `strawberry`). Ignore any input that isn’t a fruit.

## Hints
- Rather than use a conditional with 20 Boolean expressions, one for each fruit, better to use a `dict` to associate a fruit with its calories!
- If `k` is a `str` and `d` is a `dict`, you can check whether `k` is a key in `d` with code like:

		if k in d:
			...
- Take care to output the fruit’s calories, not calories from fat!

## Before You Begin
From the root of your repository execute `cd 2-Loops` So your current working directory is ...		

		/2-Loops $:
Next execute

		mkdir nutrition
to make a folder called `nutrition` in your codespace.

Then execute

		cd nutrition
to change directories into that folder. You should now see your terminal prompt as `/2-Loops/nutrition $`. You can now execute

		code nutrition.py
to make a file called `nutrition.py` where you’ll write your program.

# How to Test
Here’s how to test your code manually:

1. Run your program with `python nutrition.py`. Type `Apple` and press Enter. Your program should output:

		Calories: 130   
2. Run your program with `python nutrition.py`. Type `Avocado` and press Enter. Your program should output:

		Calories: 50
3. Run your program with `python nutrition.py`. Type `Sweet Cherries` and press Enter. Your program should output

		Calories: 100
4. Run your program with `python nutrition.py`. Type `Tomato` and press Enter. Your program should output nothing.

5. Be sure to try other fruits and vary the casing of your input. Your program should behave as expected, case-insensitively.


# Commit your program to GITHUB
At the `/2-Loops/nutrition $` prompt in your terminal:

		git add -A 
Add all changed files in the repository to be committed

		git commit -m “Upload completed nutrition.py“
Commit all changes in the REPO with the comment “Upload completed nutrition.py“
*note: If the file is not complete, adjust the comment to describes what is being commited*

		git push 
Push all changes to the REPO