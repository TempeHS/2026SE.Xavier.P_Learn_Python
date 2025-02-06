[Home](../README.md) | [Lecture 1](1-Conditionals.md) | [Problem 1.1](PROBLEM1.1.md) | [Problem 1.2](PROBLEM1.2.md) | Problem 1.3 | [Problem 1.4](PROBLEM1.4.md) | [Problem 1.5](PROBLEM1.5.md)

# File Extensions

Even though Windows and macOS sometimes hide them, most files have file extensions, a suffix that starts with a period (`.`) at the end of their name. For instance, file names for GIFs end with `.gif`, and file names for JPEGs end with `.jpg` or `.jpeg`. When you double-click on a file to open it, your computer uses its file extension to determine which program to launch.

Web browsers, by contrast, rely on media types, formerly known as MIME types, to determine how to display files that live on the web. When you download a file from a web server, that server sends an HTTP header, along with the file itself, indicating the file’s media type. For instance, the media type for a GIF is `image/gif`, and the media type for a JPEG is `image/jpeg`. To determine the media type for a file, a web server typically looks at the file’s extension, mapping one to the other.

See developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types for common types.

In a file called `extensions.py`, implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:

`.gif`
`.jpg`
`.jpeg`
`.png`
`.pdf`
`.txt`
`.zip`
If the file’s name ends with some other suffix or has no suffix at all, output `application/octet-stream` instead, which is a common default.

## Hints
- Recall that a `str` comes with quite a few methods, per <https://docs.python.org/3/library/stdtypes.html#string-methods>.

## Before You Begin
From the root of your repository execute `cd 1-Conditionals` So your current working directory is ...		

		/1-Conditionals $:
Next execute

		mkdir extensions
to make a folder called `extensions` in your codespace.

Then execute

		cd extensions
to change directories into that folder. You should now see your terminal prompt as `/1-Conditionals/extensions $`. You can now execute

		code extensions.py
to make a file called `extensions.py` where you’ll write your program.

# How to Test
Here’s how to test your code manually:

1. Run your program with `python extensions.py`. Type `happy.jpg` and press Enter. Your program should output:

		image/jpeg
2. Run your program with `python extensions.py`. Type `document.pdf` and press Enter. Your program should output:

		application/pdf
3. Be sure to test each of the other file formats, vary the casing of your input, and “accidentally” add spaces on either side of your input before pressing enter. Your program should behave as expected, case- and space-insensitively.

# Commit your program to GITHUB
At the `/1-Conditionals/extensions $` prompt in your terminal:

		git add -A 
Add all changed files in the repository to be committed

		git commit -m “Upload completed extensions.py“
Commit all changes in the REPO with the comment “Upload completed extensions.py“
*note: If the file is not complete, adjust the comment to describes what is being commited*

		git push 
Push all changes to the REPO
