IntegerToCharString
===================
Abstract
--------
The Problem is to write an algorithm that prints the headings commonly seen in spreadsheets.  They start with A, incrementing every column to the next letter.  when all single letters are taken, move to combinations such as AA for column 26, AB for column 27 and so on.  Column 1381 should have the name 'BAD'

Background
----------
This problem was found on the blog http://myagileeducation.com/2012/can-tdd-help-with-a-gnarly-problem/.  I like solving challenging problems so I decided to give it a try.  Right away I saw this was a great opportunity for a recursive solution(which made the solution a little extra juicy).  If found the solution to be quite compact and elegant; take a look at convert.py

The problem was fun, but my main purpose was to add perspective for another solution to the problem posed.  Note original github repo: (https://github.com/angelaharms/Integers-as-letters).

###Why not a pull request###
So the solution in the for-mentioned github repo is written in the J programming language.  In the interest of keeping things simple and solving one problem at a time, I solved the logically hard problem of the algorithm and left the more technical aspects of J alone for now.  

Method
------
The method to produce the resulting string is pretty simple.  It is the same process used to convert a base 10 number to any other bases.  Usually we see this when converting between base 10, 2, and 8.  This time we are coveting to base 26, and using the uppercase alphabet to indicate placeholder value.  A more visual description can be found here - http://www.purplemath.com/modules/numbbase.htm

Files
-----
*convert holds the main functionality, don't blink it only about 8 lines long.  But there is some recursive goodness in it.  
*EntryPoint is a simple example using the convert function.  It hopefully shows the expected pattern that I'm are trying to achieve.  
*tests holds 6 test cases.  
