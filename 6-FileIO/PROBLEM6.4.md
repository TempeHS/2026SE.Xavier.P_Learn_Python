[Home](../README.md) | [Lecture 6](6-FileIO.md) | [Problem 6.1](PROBLEM6.1.md) | [Problem 6.2](PROBLEM4.2.md) | [Problem 6.3](PROBLEM4.3.md) | Problem 6.4

# CS50 P-Shirt
<img src="images/took.png" />
After finishing CS50 itself, students on campus at Harvard traditionally receive their very own [I took CS50 t-shirt](https://cs50.harvardshop.com/collections/print/products/i-took-cs50-unisex-t-shirt). No need to buy one online, but like to try one on virtually?

In a file called `shirt.py`, implement a program that expects exactly two command-line arguments:
- in `sys.argv[1]`, the name (or path) of a JPEG or PNG to read (i.e., open) as input
- in `sys.argv[2]`, the name (or path) of a JPEG or PNG to write (i.e., save) as output
The program should then overlay [shirt.png](https://cs50.harvardshop.com/collections/print/products/i-took-cs50-unisex-t-shirt) (which has a transparent background) on the input after resizing and cropping the input to be the same size, saving the result as its output.

Open the input with `Image.open`, per [pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open), resize and crop the input with `ImageOps.fit`, per [pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit](https://pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit), using default values for `method`, `bleed`, and `centering`, overlay the shirt with `Image.paste`, per [pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.paste](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.paste), and save the result with `Image.save`, per [pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save).

The program should instead exit via `sys.exit`:
- if the user does not specify exactly two command-line arguments,
- if the input’s and output’s names do not end in `.jpg`, `.jpeg`, or `.png`, case-insensitively,
- if the input’s name does not have the same extension as the output’s name, or
- if the specified input does not exist.
Assume that the input will be a photo of someone posing in just the right way, like these [demos](#demo), so that, when they’re resized and cropped, the shirt appears to fit perfectly.

If you’d like to run your program on a photo of yourself, first drag the photo over to VS Code’s file explorer, into the same folder as shirt.py. No need to submit any photos with your code.

### Demo
#### BEFORE
<img src="images/before1.jpg" width="150" /><img src="images/before2.jpg" width="150" /><img src="images/before3.jpg" width="150" />

#### AFTER
<img src="images/after1.jpg" width="150" /><img src="images/after2.jpg" width="150" /><img src="images/before3.jpg" width="150" />

## Hints
- Note that you can determine a file’s extension with `os.path.splitext`, per [docs.python.org/3/library/os.path.html#os.path.splitext](https://docs.python.org/3/library/os.path.html#os.path.splitext).
- Note that `open` can `raise` a `FileNotFoundError`, [per docs.python.org/3/library/exceptions.html#FileNotFoundError](https://docs.python.org/3/library/exceptions.html#FileNotFoundError).
- Note that the `Pillow` package comes with quite a few classes and methods, per [pypi.org/project/Pillow](https://pypi.org/project/Pillow/). You might find its [handbook](https://pillow.readthedocs.io/en/stable/handbook/) and [reference](https://pillow.readthedocs.io/en/stable/reference/) helpful to skim. You can install the package with:

		pip install Pillow
You can open an image (e.g., shirt.png) with code like:

		shirt = Image.open("shirt.png")
You can get the width and height, respectively, of that image as a tuple with code like:

		size = shirt.size
And you can overlay that image on top of another (e.g., photo) with code like

		photo.paste(shirt, shirt)
wherein the first shirt represents the image to overlay and the second shirt represents a “mask” indicating which pixels in photo to update.

- Note that you can open an image (e.g., shirt.png) in VS Code by running

		code shirt.png
or by double-clicking its icon in VS Code’s file explorer.

## Before You Begin
From the root of your repository execute `cd 6-FileIO` So your current working directory is ...		

		/6-FileIO $:
Next execute

		mkdir shirt
to make a folder called `shirt` in your codespace.

Then execute

		cd shirt
to change directories into that folder. You should now see your terminal prompt as `/6-FileIO/shirt $`. You can now execute

		code shirt.py
to make a file called `shirt.py` where you’ll write your program.

# How to Test
Here’s how to test your code manually:

1. Run your program with `python shirt.py`. Your program should exit using `sys.exit` and provide an error message:

		Too few command-line arguments   
2. Be sure to download [muppets.zip](files/muppets.zip) and extract a collection of muppet photos using `unzip muppets.zip`. Run your program with `python shirt.py before1.jpg before2.jpg before3.jpg`. Your program should output:

	Too many command-line arguments
3. Run your program with `python shirt.py before1.jpg invalid_format.bmp`. Your program should exit using `sys.exit` and provide an error message:

		Invalid output
4. Run your program with `python shirt.py before1.jpg after1.png`. Your program should exit using `sys.exit` and provide an error message:

		Input and output have different extensions
5. Run your program with `python shirt.py non_existent_image.jpg after1.jpg`. Your program should exit using `sys.exit` and provide an error message:

		Input does not exist
6. Run your program with `python shirt.py before1.jpg after1.jpg`. Assuming you’ve downloaded and unzipped [muppets.zip](files/muppets.zip), your program should create an image like the below:  
<img src="images/after1.jpg" width="150" />

# Commit your program to GITHUB
At the `/6-FileIO/shirt $` prompt in your terminal:

		git add -A 
Add all changed files in the repository to be committed

		git commit -m “Upload completed shirt.py“
Commit all changes in the REPO with the comment “Upload completed shirt.py“
*note: If the file is not complete, adjust the comment to describes what is being commited*

		git push 
Push all changes to the REPO