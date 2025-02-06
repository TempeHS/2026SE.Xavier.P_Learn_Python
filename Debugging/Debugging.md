[Home](../README.md) | [Prev Lecture](../2-Loops/2-Loops.md) | [Next Lecture](../4-Libraries/4-Libraries.md)

# Short Lecture - Debugging

Watch the [Debugging](https://schoolsnsw.sharepoint.com/:v:/r/sites/TempeHS-SoftwareEngineering-SharedResources/Shared%20Documents/Resources/Harvard%20University%20-%20CS50%20Python%20Course/debugging-1080p.mp4?csf=1&web=1&e=Wbcfg8) video.

## Transcript

All right. This is CS50's Introduction to Programming with Python. My name is David Malan. And this is a look at debugging.

Odds are, by now, you've written quite a bit of code. And within that code is at least one, maybe even more, bugs, that is mistakes that you accidentally introduce to your code. Now, maybe your code doesn't even run at all. And you have some form of syntax error, or maybe you've gotten past that hurdle.

And you just have one or more logical bugs, so to speak, whereby when you run your code, it doesn't produce the output that you actually intended. So it's not quite correct. There are mistakes therein. And how do you go about, then, solving those problems?

Well, if you can't quite wrap your mind around what's going wrong by just reading with your own human eyes your own code from top to bottom, left to right, and you don't have, for instance, a teacher, a friend, a colleague, a rubber duck to help you reason through what might be wrong in your code, what kind of tools do we actually have for chasing down bugs in code and ultimately fixing them? Well, already, we actually have some tools at our disposal.

And for instance, let me propose that we build something like this in code. So pictured here is Mario from Super Mario Brothers, the original Nintendo game, jumping over a pyramid of sorts. And that period is implemented with these bricks of sorts. Let's go ahead and create a textual version thereof, whereby we use maybe hash symbols, simple hashes, to represent each of these bricks. And therefore, the goal in printing out a pyramid textually that resembles that of Mario here would be to print out one hash, and then two hashes, and then three hashes, and perhaps more if the pyramid itself is higher.

Well, let me propose that if I open up VS Code here-- and, in advance, I've created a file called mario.py. Let me propose that this is my intended solution to this problem. Let's go ahead and walk through what's here. I first, at the top of my file, have a main function defined, inside of which is a second line of code that calls input, asking the user for the height of this pyramid.

Immediately, the return value of input is passed to the input of int so as to convert that textual input, presumably, to the corresponding integer. And then I'm storing on the left-hand side of that equal sign the value that the user typed in, be it 1, 2, 3, or anything else. And then I'm using that variable as an input to a function that's apparently called pyramid so that I can ultimately print out a pyramid of that height.

All right. Well, what is this pyramid function? Well, it looks like, on this line six, that the pyramid function expects one argument called n, n presumably for number. And how am I using that number? Well, inside of this function, I have a for loop that's going to iterate, it would seem, n times.

And this is indeed our common paradigm, doing for i in the range of n allows us to iterate from zero on up. And then that innermost line of code is just going to go ahead and print out some number of hashes. And recall this trick, whereby we're using the multiplication operator but really just to automatically concatenate one or more of these hashes together.

So hopefully, the net effect of this program, once we actually run it per these final two lines, and main is invoked, and then pyramid is invoked, is that we'll get a pyramid of the corresponding height. But suppose now that I very enthusiastically went about trying to run this program. And so I went to my terminal window and ran python of mario.py.

And then I went ahead and proposed a height of three, the goal being to have one hash, two hashes, three hashes so that the total pyramid is of height three. I'm a little disappointed already to see that it's not quite correct, this output. I seem to have a pyramid really of height two because there's a blank line, and then a single hash, and then two hashes. But, again, what I wanted was one hash, then two hashes, then three hashes, forming a pyramid that's in total of height three.

Now, you might have an immediate instinct as to how to fix this problem. And indeed, relatively speaking, this isn't the most complicated program, at least if you're a few weeks into learning and writing code in Python. But suppose that it's just not obvious to me, or this is representative of an even more complicated problem down the road. And so I'd really like to start figuring out, systematically, how to solve this particular bug.

Well, what's one tool in my toolkit? Well, let me propose first that I do this. Let me clear my terminal window to get rid of the output from before. And let me propose that it might be helpful for me to maybe figure out if maybe i is wrong, right? i is my variable in this for loop that's responsible for printing out, presumably, one hash, then two hashes, then three hashes, and so forth.

So maybe just to check my understanding here I should-- maybe why don't I temporarily just print out i in addition to these hashes just so that I can make sure that i is what I expect next to the appropriate number of hashes? Which is to say, Print itself, the function we've been using now for quite some time, is a very reasonable, effective tool for debugging, at least in some cases.

It's a nice way to quickly and dirtily, kind of, see what's going on inside of your code. Well, let me do this. In addition to printing out that number of hashes, let me also print out the value of i. But rather than print out a new line, which I think is going to completely mess up the pyramid, let me just end the line with a single space just to kind of push the cursor over to the right so that my pyramid is printed to the right of all of these integers.

All right. Let me go down to my terminal window again and run python of mario.py Enter. I'm going to, again, type in 3 for the height. And now, I see essentially the same output. But I've prepended, so to speak, to each line the value of i. And now, maybe it makes a little more sense to me. Now, maybe the proverbial light bulb just went off over my head because, oh, the reason I'm seeing a blank line and then only one and only two hashes on the screen instead of one, two, and three respectively is because i, of course-- now I remember. --starts from zero, certainly when doing a for loop like the one I have here on line seven.

So how do I go about fixing this? Well, I think, instinctively, I could just do this. Let me go ahead and remove the previous print. Indeed, when using print to debug your code, it's usually temporary. So I should now undo that change because I don't want those numbers to appear ultimately in my program's output.

Let me go ahead now and print out-- OK. I don't want to print out zero hashes, and then one, and then two. I want to print out one more than the current value of i. And I bet there's a bunch of ways I can solve this. But I think the easiest way might be this.

Let me go ahead and in parentheses do i + 1 so that what I'm really doing is multiplying this single hash by i + 1. So instead of being zero, one, and two hashes respectively, now it's one, two, and three. And I've parenthesized it just to make clear to myself that indeed the math is going to happen first, just like in math class, inside of the parentheses. And then I'm going to use that total value for the concatenation of all of those hashes.

All right. Let me go ahead now back to my terminal window, clearing it, running python of mario.py once more. Let's again type in a height of 3. And now I have the intended pyramid. So a minor bug, if you will--

Certainly, if you're several weeks into learning python, already that kind of bug might have jumped out at you pretty quickly. But that's not always going to be the case. And so Print is the first of your friends when it comes to debugging your code. Using Print, you can temporarily, but pretty easily, just display the values of variables or other things in your program just so you can help see what the computer sees underneath the hood, so to speak.

But it turns out there's more powerful tools. And Print can start to get a little tedious, especially if you're adding a print up here, and up here, and up here, and up here, and all over the place in more complicated programs because then you have to clean up a whole mess that you've made.

And you might have put the Print in not the right location. And you have to remember what output is coming from one Print. So eventually, Print is not so much your friend. And we need better tools than that. So let me go ahead and clear my terminal window again.

Let me undo these changes so that I again have the same bug, where I'm now printing out i number of hashes, so zero, one, and two again. And let me propose that we use another tool that comes with a lot of programming environments nowadays, VS Code included.

Indeed, typically, I've hidden the so-called activity bar to the left-hand side here of VS Code. But I've revealed it today so that we can see some of the functionality that actually comes with VS Code, and other text editors, and other IDEs.

Integrated Development Environments often come with built-in debuggers. And indeed, a debugger is a special type of program whose purpose in life is to do just that, to help you debug your program. It doesn't necessarily solve the problems for you. So it's perhaps a bit of a misnomer. But it helps you.

It empowers you to solve bugs yourself and eliminate them more methodically than maybe Print alone would allow. So I'm going to do this first. I'm going to introduce this notion of what's called, generally, a breakpoint. A breakpoint is simply a mechanism when using a text editor or an IDE that allows you to specify on what line or what lines of code do you want to pause or break execution of the program just so you can start poking around at that line of code.

In other words, if I keep running mario.py in my terminal window, it pretty much runs from top to bottom, left to right, again and again, pausing of course for my own human input. But it's so darn fast, Python, that I can't really see what's happening on each individual line of code. So let me go back to VS Code and this time set a breakpoint.

Wouldn't it be nice if I could pump the brakes, so to speak, and slow down the execution of my program so that I can tell the computer when I, the human, am ready to step, step, step through each of my lines of code? So it turns out that to the left of the line numbers here in VS Code-- and this is a popular approach in other programs as well.

Notice if you hover over to the left of a line number, it becomes a grayed out form of red. And if you click on it once, it becomes really red. And what that indicates is that I've set one of these things called a breakpoint. I've indicated to VS code, in this case, that I want it to break, that is pause execution of my code just before main is called.

And I can actually set it on almost any of these lines of code. But I'm starting at the very bottom one because, of course, that's the line of code that we know is going to kick off the whole process of running my code. But it's going to allow me, therefore, to step through any and all of the specific lines therein. So let's go ahead and do this. But now, I'm not going to go ahead and just run python of mario.py.

I need to actually run the debugger. And the debugger in VS Code is pretty smart to figure out exactly what I want to run. And you can even configure it to be even more customized. I'm going to go ahead and, perhaps aptly, click on this icon here, a.k.a. Run and Debug. And it's the little Play icon with what appears to be an actual bug on it.

And when I click that, this additional panel opens up in VS Code. And its a big button there. It's called Run and Debug. Now, I could follow more of the directions and customize it further. But I'm just going to go ahead and click Run and Debug.

And using some default settings that I might have specified earlier too, it's going to run my program but pause it on this line here. Notice that in yellow on line 12, that's where I set the breakpoint. And the yellow highlight of line 12 means that line of code has not yet executed. But it's about to be executed if and when I am ready.

There's a bit of noise, or messy output, in my terminal window potentially. But that's just part of the debugging process in my terminal window. Eventually will I see that same prompt for height, but I don't yet because I'm not at that line of code.

Now let me draw your attention to all of these icons at the top of the screen. The first of these, which looks like a Play button with a line to the left of it, is this Continue button. If I click that button, the breakpoint is going to be left behind. And my code is just going to continue on to the end of the program. That's probably not what I want in this case because I actually do want to step through it line by line.

There's this next icon here, an arrow going over a single dot. That's the Step Over command. This would allow me to step over this line 12. It will execute it, but that's it. It's not going to step into that function so that I can go line by line through main or, in turn, pyramid either.

The one I really want to use now is this one in the middle, Step Into. And this is the line pointing down at the dot which is a symbol that indicates that if I click this button in a moment, I'm going to step into line 12. That is, I'm going to step inside of the main function. And from there, I can continue to step-by-step walk through my code. So watch what happens on the yellow on the screen here when I click Step Into like this.

You'll see that now line 12 has begun executing. But when we step into that function, notice now that the debugger has broken, or paused, on line two. Line two has not yet executed. But as soon as I step over this one, I think we're going to start to see some results.

And I was careful there to say step over instead of step into. Why? Well, notice on this line of code two, there's two functions, input and int. And I didn't implement either of those. And allow me to propose that the people who invented Python probably implemented input and int correctly.

So there's really no point in my stepping into their functions or even trying to. I really should only be stepping into my own functions. But I do want line two to execute. But let me call your attention to this. At the top left of VS Code now, there is, under the Run and Debug panel, some mention of variables, both locals and globals.

And there's nothing under locals at the moment because at this moment, before line two has been executed, no variables actually yet exist. In a moment, once I do execute this line of code and step over it, well, a variable called height should exist. So let's try that.

I'm not going to click Step Into. I'm going to click Step Over. But that will not ignore the line of code. It will execute it but not dive into it, if you will. Once I click Step Over, notice that the line is no longer highlighted because execution hasn't broken or paused yet. Notice in my terminal window, despite the output from earlier, I'm being prompted for the actual height of the pyramid. So this part is still interactive.

Let me go ahead and type 3 and hit Enter. And now we'll see what's happened at the top of the screen. Line two has just executed. The height variable now exists. And indeed, if you look up here, you'll see in the debugger a graphical summary of all, or in this case, the one variable that now exists. And better still, you see the value of that variable.

Now, that's not that helpful at the moment because I'm pretty sure the height is as the user typed in. So there's no off by one error or any bug there. I think then the bug is probably inside of my pyramid function. So here, I don't want to click Step Over because that's going to execute pyramid and not allow me a chance to step through each of its lines.

I'm going to, again, this time, because it's my function, Step Into the pyramid function. Once I do that, now it's line seven that's highlighted because I've stepped into the pyramid function. Notice that the panel up here has changed. The local variable, that is the variables that exist local to the pyramid function, are indeed n because n was the argument that was passed in with a value of 3.

i does not yet exist because line seven has not yet executed. But here comes my for loop. And here's where it's going to be interesting to step over and step over a few times. I don't want to step into because the range function, again, was invented by someone other than me. And let's just trust that it's correct.

So let's step over this line, thereby executing it. But watch the top left-hand corner of VS Code. Let's step over it once. And now notice not only does n equal 3, now there's another local variable called i that equals 0. And what am I about to do on line eight? Well, in a moment, I'm going to click Step Over again because I'm going to trust that print is correct.

So I don't need to step into print. But watch what happens now in my terminal window down here. No pyramid, no bricks have been printed. But as soon as I step over line eight, thereby executing it, we see the first of my-- wait a minute. I'm not seeing an actual brick.

If you notice, the cursor did move down. And effectively, a blank line was printed. And now there's an opportunity for that light bulb again to go off. Wait a minute. I saw the cursor move. It printed something, but it's really nothing. It's no bricks.

Oh. This is where now I might realize, this is why my program is flawed. Because when i equals 0, I'm apparently printing zero bricks. Aha. Now hopefully I understand. If not, no big deal. I can continue stepping over or stepping into each of my lines of code.

I can click the big Stop icon, or I can restart the whole process. Sometimes it might not be obvious the first time around. And sometimes you might want to unset or reset a different breakpoint so as to figure out what's actually going on. It's just part of the process of debugging.

For now that I figured it out, I'm going to go ahead and just continue my program because I know that it's flawed. But I now know what the problem is. Let me go ahead and close this panel over here. I'm going to get rid of the breakpoint because I've now, in my mind at least, solved this problem.

I'm going to clear my terminal window. I'm going to go in and just logically add what I think is the solution to this problem by doing i + 1 in parentheses again. I'm going to now run one final time mario.py with Python. I'm going to again type in height of 3. And there it is, my pyramid of height three.

So ultimately, what are the tools in your toolkit? Well, certainly Print is something that you can always reach for, not just in Python, but so many other languages as well or some equivalent thereof. But sometimes once your programs get sufficiently complicated, sufficiently sophisticated, or, heck, maybe it's someone else's code that you yourself didn't write and, therefore, you would especially benefit from stepping through it line by line, stepping into functions of interest, a debugger, like that that comes with VS Code, is going to be your new best friend.
