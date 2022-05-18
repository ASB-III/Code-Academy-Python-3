Code Academy: PYTHON 3 Hello World 

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Cheet Sheet

Comments
A comment is a piece of text within a program that is not executed. It can be used to provide additional information to aid in understanding the code.

The # character is used to start a comment and it continues until the end of the line.

# Comment on a single line
 
user = "JDoe" # Comment after code
Arithmetic Operations
Python supports different types of arithmetic operations that can be performed on literal numbers, variables, or some combination. The primary arithmetic operators are:

+ for addition
- for subtraction
* for multiplication
/ for division
% for modulus (returns the remainder)
** for exponentiation
# Arithmetic operations
 
result = 10 + 30
result = 40 - 10
result = 50 * 5
result = 16 / 4
result = 25 % 2
result = 5 ** 3
Plus-Equals Operator +=
The plus-equals operator += provides a convenient way to add a value to an existing variable and assign the new value back to the same variable. In the case where the variable and the value are strings, this operator performs string concatenation instead of addition.

The operation is performed in-place, meaning that any other variable which points to the variable being updated will also be updated.

# Plus-Equal Operator
 
counter = 0
counter += 10
 
# This is equivalent to
 
counter = 0
counter = counter + 10
 
# The operator will also perform string concatenation
 
message = "Part 1 of message "
message += "Part 2 of message"
Variables
A variable is used to store data that will be used by the program. This data can be a number, a string, a Boolean, a list or some other data type. Every variable has a name which can consist of letters, numbers, and the underscore character _.

The equal sign = is used to assign a value to a variable. After the initial assignment is made, the value of a variable can be updated to new values as needed.

# These are all valid variable names and assignment
 
user_name = "@sonnynomnom"
user_id = 100
verified = False
 
# A variable's value can be changed after assignment
 
points = 100
points = 120
Modulo Operator %
A modulo calculation returns the remainder of a division between the first and second number. For example:

The result of the expression 4 % 2 would result in the value 0, because 4 is evenly divisible by 2 leaving no remainder.
The result of the expression 7 % 3 would return 1, because 7 is not evenly divisible by 3, leaving a remainder of 1.
# Modulo operations
 
zero = 8 % 4
 
nonzero = 12 % 5
Integers
An integer is a number that can be written without a fractional part (no decimal). An integer can be a positive number, a negative number or the number 0 so long as there is no decimal portion.

The number 0 represents an integer value but the same number written as 0.0 would represent a floating point number.

# Example integer numbers
 
chairs = 4
tables = 1
broken_chairs = -2
sofas = 0
 
# Non-integer numbers
 
lights = 2.5
left_overs = 0.0
String Concatenation
Python supports the joining (concatenation) of strings together using the + operator. The + operator is also used for mathematical addition operations. If the parameters passed to the + operator are strings, then concatenation will be performed. If the parameter passed to + have different types, then Python will report an error condition. Multiple variables or literal strings can be joined together using the + operator.

# String concatenation
 
first = "Hello "
second = "World"
 
result = first + second
 
long_result = first + second + "!"
Errors
The Python interpreter will report errors present in your code. For most error cases, the interpreter will display the line of code where the error was detected and place a caret character ^ under the portion of the code where the error was detected.

if False ISNOTEQUAL True:
                  ^
SyntaxError: invalid syntax
ZeroDivisionError
A ZeroDivisionError is reported by the Python interpreter when it detects a division operation is being performed and the denominator (bottom number) is 0. In mathematics, dividing a number by zero has no defined value, so Python treats this as an error condition and will report a ZeroDivisionError and display the line of code where the division occurred. This can also happen if a variable is used as the denominator and its value has been set to or changed to 0.

numerator = 100
denominator = 0
bad_results = numerator / denominator
 
ZeroDivisionError: division by zero
Strings
A string is a sequence of characters (letters, numbers, whitespace or punctuation) enclosed by quotation marks. It can be enclosed using either the double quotation mark " or the single quotation mark '.

If a string has to be broken into multiple lines, the backslash character \ can be used to indicate that the string continues on the next line.

user = "User Full Name"
game = 'Monopoly'
 
longer = "This string is broken up \
over multiple lines"
SyntaxError
A SyntaxError is reported by the Python interpreter when some portion of the code is incorrect. This can include misspelled keywords, missing or too many brackets or parenthesis, incorrect operators, missing or too many quotation marks, or other conditions.

age = 7 + 5 = 4
 
File "<stdin>", line 1
SyntaxError: can't assign to operator
NameError
A NameError is reported by the Python interpreter when it detects a variable that is unknown. This can occur when a variable is used before it has been assigned a value or if a variable name is spelled differently than the point at which it was defined. The Python interpreter will display the line of code where the NameError was detected and indicate which name it found that was not defined.

misspelled_variable_name
 
NameError: name 'misspelled_variable_name' is not defined
Floating Point Numbers
Python variables can be assigned different types of data. One supported data type is the floating point number. A floating point number is a value that contains a decimal portion. It can be used to represent numbers that have fractional quantities. For example, a = 3/5 can not be represented as an integer, so the variable a is assigned a floating point value of 0.6.

# Floating point numbers
 
pi = 3.14159
meal_cost = 12.99
tip_percent = 0.20
print() Function
The print() function is used to output text, numbers, or other printable information to the console.

It takes one or more arguments and will output each of the arguments to the console separated by a space. If no arguments are provided, the print() function will output a blank line.

print("Hello World!")
 
print(100)
 
pi = 3.14159
print(pi)

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Welcome
Python is a programming language. Like other languages, it gives us a way to communicate ideas. In the case of a programming language, these ideas are “commands” that people use to communicate with a computer!

We convey our commands to the computer by writing them in a text file using a programming language. These files are called programs. Running a program means telling a computer to read the text file, translate it to the set of operations that it understands, and perform those actions.

Instructions
Change Codecademy to your name in the script to the right. Run the code to see what it does!

As soon as you’re ready, move on to the next exercise to begin learning to write your own Python programs!


my_name = "Al"
print("Hello and welcome " + my_name + "!")

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Comments
Ironically, the first thing we’re going to do is show how to tell a computer to ignore a part of a program. Text written in a program but not run by the computer is called a comment. Python interprets anything after a # as a comment.

Comments can:

Provide context for why something is written the way it is:

# This variable will be used to count the number of times anyone tweets the word persnickety
persnickety_count = 0
Help other people reading the code understand it faster:

# This code will calculate the likelihood that it will rain tomorrow
complicated_rain_calculation_for_tomorrow()
Ignore a line of code and see how a program will run without it:

# useful_value = old_sloppy_code()
useful_value = new_clean_code()
Instructions
1.
Documentation is an important step in programming. Write a comment describing the first program you want to write!

# I want to use python to code for business intelligence / data analytics. I dont know what that program will look like yet

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Print
Now what we’re going to do is teach our computer to communicate. The gift of speech is valuable: a computer can answer many questions we have about “how” or “why” or “what” it is doing. In Python, the print() function is used to tell a computer to talk. The message to be printed should be surrounded by quotes:

# from Mary Shelley's Frankenstein
print("There is something at work in my soul, which I do not understand.")
In the above example, we direct our program to print() an excerpt from a notable book. The printed words that appear as a result of the print() function are referred to as output. The output of this example program would be:

There is something at work in my soul, which I do not understand.
Instructions
1.
Print the distinguished greeting “Hello world!”

# from Mary Shelley's Frankenstein
print("There is something at work in my soul, which I do not understand.")

print("Hello world!")

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Strings
Computer programmers refer to blocks of text as strings. In our last exercise, we created the string “Hello world!”. In Python a string is either surrounded by double quotes ("Hello world") or single quotes ('Hello world'). It doesn’t matter which kind you use, just be consistent.

Instructions
1.
Print your name using the print() command.

Checkpoint 2 Passed

Stuck? Get a hint
2.
If your print statement uses double-quotes ", change them to single-quotes '. If it uses single-quotes ', change them to double-quotes ".

Try running your code again after switching the type of quote-marks. Is anything different about the output?

print("albert")

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Variables
Programming languages offer a method of storing data for reuse. If there is a greeting we want to present, a date we need to reuse, or a user ID we need to remember we can create a variable which can store a value. In Python, we assign variables by using the equals sign (=).

message_string = "Hello there"
# Prints "Hello there"
print(message_string)
In the above example, we store the message “Hello there” in a variable called message_string. Variables can’t have spaces or symbols in their names other than an underscore (_). They can’t begin with numbers but they can have numbers after the first letter (e.g., cool_variable_5 is OK).

It’s no coincidence we call these creatures “variables”. If the context of a program changes, we can update a variable but perform the same logical process on it.

# Greeting
message_string = "Hello there"
print(message_string)
 
# Farewell
message_string = "Hasta la vista"
print(message_string)
Above, we create the variable message_string, assign a welcome message, and print the greeting. After we greet the user, we want to wish them goodbye. We then update message_string to a departure message and print that out.

Instructions
1.
Update the variable meal to reflect each meal of the day before we print it.

# We've defined the variable "meal" here to the name of the food we ate for breakfast!
meal = "An english muffin"

# Printing out breakfast
print("Breakfast:")
print(meal)

# Now update meal to be lunch!
meal = "A Cheeseburger"

# Printing out lunch
print("Lunch:")
print(meal)

# Now update "meal" to be dinner
meal = "A steak with with wine"
# Printing out dinner
print("Dinner:")
print(meal)

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Errors
Humans are prone to making mistakes. Humans are also typically in charge of creating computer programs. To compensate, programming languages attempt to understand and explain mistakes made in their programs.

Python refers to these mistakes as errors and will point to the location where an error occurred with a ^ character. When programs throw errors that we didn’t expect to encounter we call those errors bugs. Programmers call the process of updating the program so that it no longer produces unexpected errors debugging.

Two common errors that we encounter while writing Python are SyntaxError and NameError.

SyntaxError means there is something wrong with the way your program is written — punctuation that does not belong, a command where it is not expected, or a missing parenthesis can all trigger a SyntaxError.

A NameError occurs when the Python interpreter sees a word it does not recognize. Code that contains something that looks like a variable but was never defined will throw a NameError.

Instructions
1.
You might encounter a SyntaxError if you open a string with double quotes and end it with a single quote. Update the string so that it starts and ends with the same punctuation.

You might encounter a NameError if you try to print a single word string but fail to put any quotes around it. Python expects the word of your string to be defined elsewhere but can’t find where it’s defined. Add quotes to either side of the string to squash this bug.

Update the malformed strings in the workspace to all be strings.

Abracadabra = "magic"
print('This message has mismatched quote marks!')
print(Abracadabra)

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Numbers
Computers can understand much more than just strings of text. Python has a few numeric data types. It has multiple ways of storing numbers. Which one you use depends on your intended purpose for the number you are saving.

An integer, or int, is a whole number. It has no decimal point and contains all counting numbers (1, 2, 3, …) as well as their negative counterparts and the number 0. If you were counting the number of people in a room, the number of jellybeans in a jar, or the number of keys on a keyboard you would likely use an integer.

A floating-point number, or a float, is a decimal number. It can be used to represent fractional quantities as well as precise measurements. If you were measuring the length of your bedroom wall, calculating the average test score of a seventh-grade class, or storing a baseball player’s batting average for the 1998 season you would likely use a float.

Numbers can be assigned to variables or used literally in a program:

an_int = 2
a_float = 2.1
 
print(an_int + 3)
# Output: 5
Above we defined an integer and a float as the variables an_int and a_float. We printed out the sum of the variable an_int with the number 3. We call the number 3 here a literal, meaning it’s actually the number 3 and not a variable with the number 3 assigned to it.

Floating-point numbers can behave in some unexpected ways due to how computers store them. For more information on floating-point numbers and Python, review Python’s documentation on floating-point limitations.

Instructions
1.
A recent movie-going experience has you excited to publish a review. You rush out of the cinema and hastily begin programming to create your movie-review website: The Big Screen’s Greatest Scenes Decided By A Machine.

Create the following variables and assign integer numbers to them: release_year and runtime.

# Define the release and runtime integer variables below:
release_year = 2021
runtime = 2

# Define the rating_out_of_10 float variable below: 

rating_out_of_10 = 7.9

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Calculations
Computers absolutely excel at performing calculations. The “compute” in their name comes from their historical association with providing answers to mathematical questions. Python performs addition, subtraction, multiplication, and division with +, -, *, and /.

# Prints "500"
print(573 - 74 + 1)
 
# Prints "50"
print(25 * 2)
 
# Prints "2.0"
print(10 / 5)
Notice that when we perform division, the result has a decimal place. This is because Python converts all ints to floats before performing division. In older versions of Python (2.7 and earlier) this conversion did not happen, and integer division would always round down to the nearest integer.

Division can throw its own special error: ZeroDivisionError. Python will raise this error when attempting to divide by 0.

Mathematical operations in Python follow the standard mathematical order of operations.

Instructions
1.
Print out the result of this equation: 25 * 68 + 13 / 28

# Prints "500"
print(573 - 74 + 1)
 
# Prints "50"
print(25 * 2)
 
# Prints "2.0"
print(10 / 5)

# Prints something
print(25 * 68 + 13 / 28)

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Changing Numbers
Variables that are assigned numeric values can be treated the same as the numbers themselves. Two variables can be added together, divided by 2, and multiplied by a third variable without Python distinguishing between the variables and literals (like the number 2 in this example). Performing arithmetic on variables does not change the variable — you can only update a variable using the = sign.

coffee_price = 1.50
number_of_coffees = 4
 
# Prints "6.0"
print(coffee_price * number_of_coffees)
# Prints "1.5"
print(coffee_price)
# Prints "4"
print(number_of_coffees)
 
# Updating the price 
coffee_price = 2.00
 
# Prints "8.0"
print(coffee_price * number_of_coffees)
# Prints "2.0"
print(coffee_price)
# Prints "4"
print(number_of_coffees)
We create two variables and assign numeric values to them. Then we perform a calculation on them. This doesn’t update the variables! When we update the coffee_price variable and perform the calculations again, they use the updated values for the variable!

Instructions
1.
You’ve decided to get into quilting! To calculate the number of squares you’ll need for your first quilt let’s create two variables: quilt_width and quilt_length. Let’s make this first quilt 8 squares wide and 12 squares long.

Checkpoint 2 Passed
2.
Print out the number of squares you’ll need to create the quilt!

Checkpoint 3 Passed
3.
It turns out that quilt required a little more material than you have on hand! Let’s only make the quilt 8 squares long. How many squares will you need for this quilt instead?

print('quilt width = 8')
quilt_width = 8
print('quilt length = 8')
quilt_length = 8

# print number of squares in quilt (area)
print('number of squares in quilt (the area)')
print(quilt_width * quilt_length)

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Exponents
Python can also perform exponentiation. In written math, you might see an exponent as a superscript number, but typing superscript numbers isn’t always easy on modern keyboards. Since this operation is so related to multiplication, we use the notation **.

# 2 to the 10th power, or 1024
print(2 ** 10)
 
# 8 squared, or 64
print(8 ** 2)
 
# 9 * 9 * 9, 9 cubed, or 729
print(9 ** 3)
 
# We can even perform fractional exponents
# 4 to the half power, or 2
print(4 ** 0.5)
Here, we compute some simple exponents. We calculate 2 to the 10th power, 8 to the 2nd power, 9 to the 3rd power, and 4 to the 0.5th power.

Instructions
1.
You really like how the square quilts from last exercise came out, and decide that all quilts that you make will be square from now on.

Using the exponent operator, print out how many squares you’ll need for a 6x6 quilt, a 7x7 quilt, and an 8x8 quilt.

Checkpoint 2 Passed
2.
Your 6x6 quilts have taken off so well, 6 people have each requested 6 quilts. Print out how many tiles you would need to make 6 quilts apiece for 6 people.

# Calculation of squares for:
# 6x6 quilt
print('squares for 6x6 quilt')
print(6 ** 2)
# 7x7 quilt
print('squares for 7x7 quilt')
print(7 ** 2)
# 8x8 quilt
print('squares for 8x8 quilt')
print(8 ** 2)
# How many squares for 6 people to have 6 quilts each that are 6x6?
print(' Print out how many tiles you would need to make 6 quilts apiece for 6 people.')
print(6 ** 4)

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Modulo
Python offers a companion to the division operator called the modulo operator. The modulo operator is indicated by % and gives the remainder of a division calculation. If the number is divisible, then the result of the modulo operator will be 0.

# Prints 4 because 29 / 5 is 5 with a remainder of 4
print(29 % 5)
 
# Prints 2 because 32 / 3 is 10 with a remainder of 2
print(32 % 3)
 
# Modulo by 2 returns 0 for even numbers and 1 for odd numbers
# Prints 0
print(44 % 2)
Here, we use the modulo operator to find the remainder of division operations. We see that 29 % 5 equals 4, 32 % 3 equals 2, and 44 % 2 equals 0.

The modulo operator is useful in programming when we want to perform an action every nth-time the code is run. Can the result of a modulo operation be larger than the divisor? Why or why not?

Instructions
1.
You’re trying to divide a group into four teams. All of you count off, and you get number 27.

Find out your team by computing 27 modulo 4. Save the value to my_team.

Checkpoint 2 Passed
2.
Print out my_team. What number team are you on?

Checkpoint 3 Passed
3.
Food for thought: what number team are the two people next to you (26 and 28) on? What are the numbers for all 4 teams? (Optional Challenge Question)

print(29 % 5)
print(32%3)
print(44 % 2)

print(27 % 4)
my_team =3
print(my_team)

print(26 % 4)
print(28 % 4)

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Concatenation
The + operator doesn’t just add two numbers, it can also “add” two strings! The process of combining two strings is called string concatenation. Performing string concatenation creates a brand new string comprised of the first string’s contents followed by the second string’s contents (without any added space in-between).

greeting_text = "Hey there!"
question_text = "How are you doing?"
full_text = greeting_text + question_text
 
# Prints "Hey there!How are you doing?"
print(full_text)
In this sample of code, we create two variables that hold strings and then concatenate them. But we notice that the result was missing a space between the two, let’s add the space in-between using the same concatenation operator!

full_text = greeting_text + " " + question_text
 
# Prints "Hey there! How are you doing?"
print(full_text)
Now the code prints the message we expected.

If you want to concatenate a string with a number you will need to make the number a string first, using the str() function. If you’re trying to print() a numeric variable you can use commas to pass it as a different argument rather than converting it to a string.

birthday_string = "I am "
age = 10
birthday_string_2 = " years old today!"
 
# Concatenating an integer with strings is possible if we turn the integer into a string first
full_birthday_string = birthday_string + str(age) + birthday_string_2
 
# Prints "I am 10 years old today!"
print(full_birthday_string)
 
# If we just want to print an integer 
# we can pass a variable as an argument to 
# print() regardless of whether 
# it is a string.
 
# This also prints "I am 10 years old today!"
print(birthday_string, age, birthday_string_2)
Using str() we can convert variables that are not strings to strings and then concatenate them. But we don’t need to convert a number to a string for it to be an argument to a print statement.

Instructions
1.
Concatenate the strings and save the message they form in the variable message.

Now uncomment the print statement and run your code to see the result in the terminal!

string1 = "The wind, "
string2 = "which had hitherto carried us along with amazing rapidity, "
string3 = "sank at sunset to a light breeze; "
string4 = "the soft air just ruffled the water and "
string5 = "caused a pleasant motion among the trees as we approached the shore, "
string6 = "from which it wafted the most delightful scent of flowers and hay."

# Define message below:
message = string1 + string2 + string3 + string4 + string5 + string6

#print(message)

print(message)

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Plus Equals
Python offers a shorthand for updating variables. When you have a number saved in a variable and want to add to the current value of the variable, you can use the += (plus-equals) operator.

# First we have a variable with a number saved
number_of_miles_hiked = 12
 
# Then we need to update that variable
# Let's say we hike another two miles today
number_of_miles_hiked += 2
 
# The new value is the old value
# Plus the number after the plus-equals
print(number_of_miles_hiked)
# Prints 14
Above, we keep a running count of the number of miles a person has gone hiking over time. Instead of recalculating from the start, we keep a grand total and update it when we’ve gone hiking further.

The plus-equals operator also can be used for string concatenation, like so:

hike_caption = "What an amazing time to walk through nature!"
 
# Almost forgot the hashtags!
hike_caption += " #nofilter"
hike_caption += " #blessed"
We create the social media caption for the photograph of nature we took on our hike, but then update the caption to include important social media tags we almost forgot.

Instructions
1.
We’re doing a little bit of online shopping and find a pair of new sneakers. Right before we check out, we spot a nice sweater and some fun books we also want to purchase!

Use the += operator to update the total_price to include the prices of nice_sweater and fun_books.

The prices (also included in the workspace) are:

new_sneakers = 50.00
nice_sweater = 39.00
fun_books = 20.00

total_price = 0

new_sneakers = 50.00
nice_sweater = 39.00
fun_books = 20.00

total_price += new_sneakers
total_price += nice_sweater
total_price += fun_books

nice_sweater = 39.00
fun_books = 20.00
# Update total_price here:

print("The total price is", total_price)

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Multi-line Strings
Python strings are very flexible, but if we try to create a string that occupies multiple lines we find ourselves face-to-face with a SyntaxError. Python offers a solution: multi-line strings. By using three quote-marks (""" or ''') instead of one, we tell the program that the string doesn’t end until the next triple-quote. This method is useful if the string being defined contains a lot of quotation marks and we want to be sure we don’t close it prematurely.

leaves_of_grass = """
Poets to come! orators, singers, musicians to come!
Not to-day is to justify me and answer what I am for,
But you, a new brood, native, athletic, continental, greater than
  before known,
Arouse! for you must justify me.
""'
In the above example, we assign a famous poet’s words to a variable. Even though the quote contains multiple linebreaks, the code works!

If a multi-line string isn’t assigned a variable or used in an expression it is treated as a comment.

Instructions
1.
Assign the string

Stranger, if you passing meet me and desire to speak to me, why
  should you not speak to me?
And why should I not speak to you?
to the variable to_you.

# Assign the string here
to_you = ''' Stranger, if you passing meet me and desire to speak to me, why 
should you not speak to me?
And why should I not speak to you?
'''


print(to_you)

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Review
In this lesson, we accomplished a lot of things! We instructed our computers to print messages, we stored these messages as variables, and we learned to update those messages depending on the part of the program we were in. We performed mathematical calculations and explored some of the mathematical expressions that Python offers us. We learned about errors and other valuable skills that will continue to serve us as we develop our programming skills.

Good job!

Instructions
1.
Create variables:

my_age
half_my_age
greeting
name
greeting_with_name
Assign values to each using your knowledge of division and concatenation!

my_age = 26
print('my age')
print(my_age)
half_my_age = (my_age / 2)
print('half_my_age')
print(half_my_age)
greeting = "hello there"
name = "albert"
greeting_with_name = greeting + " " + name
print(greeting_with_name)

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Block Letters
ASCII art is a graphic design technique that uses computers for presentation and consists of pictures pieced together from individual characters.

Write a Python program called initials.py that displays the initials of your name in block letters as shown and dip your toes into ASCII art.

Block Letters

Happy coding!

Tasks
5/5 Complete
Mark the tasks as complete by checking them off
What we are building in this project:
1.
Take a look at the complete alphabet and find your initials. Notice how each block letter is 7x5 and formed by the letter itself.

My initials are S and L, so my initials.py program should output:

 SSS   L
S   S  L
S      L
 SSS   L
    S  L
S   S  L
 SSS   LLLLL
Once you are ready, mark this task complete by checking off the box.


Stuck? Get a hint
Setting up:
2.
First, write two comments with:

Your first and last name.
A fun fact about yourself.

Stuck? Get a hint
3.
Output your first initial as a block letter. There are a few ways to do this!

Press Save to run your program.


Stuck? Get a hint
4.
Output your second initial as a block letter by adding to the print() statements.

Press Save to run your program.


Stuck? Get a hint
Solution:
5.
Don’t forget to check off all the tasks before moving on.

Sample solutions:

initials.py
snowman.py
P.S. If you make something cool, share it with us!

# Albert Beattie
# Ligma

name = '''
            A                   S S S       B B B B B                      
          A   A               S       S     B        B         
        A       A             S             B        B         
      A A A A A A A             S S S       B B B B B          
    A               A                S      B        B         
  A                   A       S      S      B        B         
A                       A  *    S S S    *  B B B B B   *
'''
print(name)

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Receipts for Lovely Loveseats
We’ve decided to pursue the dream of small-business ownership and open up a furniture store called Lovely Loveseats for Neat Suites on Fleet Street. With our newfound knowledge of Python programming, we’re going to build a system to help speed up the process of creating receipts for your customers.

In this project, we will be storing the names and prices of a furniture store’s catalog in variables. You will then process the total price and item list of customers, printing them to the output terminal.

Please note: Projects do not run tests against your code. This experience is more open to your interpretation and gives you the freedom to explore. Remember that all variables must be declared before they are referenced in your code.

If you get stuck during this project or would like to see an experienced developer work through it, click “Get Unstuck“ to see a project walkthrough video.

Tasks
20/20 Complete
Mark the tasks as complete by checking them off
Adding In The Catalog
1.
Let’s add in our first item, the Lovely Loveseat that is the store’s namesake. Create a variable called lovely_loveseat_description and assign to it the following string:

Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.

Stuck? Get a hint
2.
Great, now let’s create a price for the loveseat. Create a variable lovely_loveseat_price and set it equal to 254.00.


Stuck? Get a hint
3.
Let’s extend our inventory with another characteristic piece of furniture! Create a variable called stylish_settee_description and assign to it the following string:

Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.
4.
Now let’s set the price for our Stylish Settee. Create a variable stylish_settee_price and assign it the value of 180.50.

5.
Fantastic, we just need one more item before we’re ready for business. Create a new variable called luxurious_lamp_description and assign it the following:

Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.
6.
Let’s set the price for this item. Create a variable called luxurious_lamp_price and set it equal to 52.15.

7.
In order to be a business, we should also be calculating sales tax. Let’s store that in a variable as well.

Define the variable sales_tax and set it equal to .088. That’s 8.8%.

Our First Customer
8.
Our first customer is making their purchase! Let’s keep a running tally of their expenses by defining a variable called customer_one_total. Since they haven’t purchased anything yet, let’s set that variable equal to 0 for now.

9.
We should also keep a list of the descriptions of things they’re purchasing. Create a variable called customer_one_itemization and set that equal to the empty string "". We’ll tack on the descriptions to this as they make their purchases.


Stuck? Get a hint
10.
Our customer has decided they are going to purchase our Lovely Loveseat! Add the price to customer_one_total.


Stuck? Get a hint
11.
Let’s start keeping track of the items our customer purchased. Add the description of the Lovely Loveseat to customer_one_itemization.


Stuck? Get a hint
12.
Our customer has also decided to purchase the Luxurious Lamp! Let’s add the price to the customer’s total.


Stuck? Get a hint
13.
Let’s keep the itemization up-to-date and add the description of the Luxurious Lamp to our itemization.

14.
They’re ready to check out! Let’s begin by calculating sales tax. Create a variable called customer_one_tax and set it equal to customer_one_total times sales_tax.


Stuck? Get a hint
15.
Add the sales tax to the customer’s total cost.


Stuck? Get a hint
16.
Let’s start printing up their receipt! Begin by printing out the heading for their itemization. Print the phrase "Customer One Items:".


Stuck? Get a hint
17.
Print customer_one_itemization.


Stuck? Get a hint
18.
Now add a heading for their total cost: Print out "Customer One Total:"

19.
Now print out their total! Our first customer now has a receipt for the things they purchased.

20.
Congratulations! We created our catalog and served our first customer. We used our knowledge of strings and numbers to create and update variables. We were able to print out an itemized list and a total cost for our customer. Lovely!

lovely_loveseat_description = 'Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. red or white. '

lovely_loveseat_price = 254.00

stylish_settee_description = 'Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black'

stylish_settee_price = 180.50

luxurious_lamp_description = 'Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.'

luxurious_lamp_price = 52.15

sales_tax = .088


customer_one_total = 0

customer_one_itemization = ""

customer_one_total += lovely_loveseat_price

customer_one_itemization += lovely_loveseat_description

customer_one_total += luxurious_lamp_price

customer_one_itemization += luxurious_lamp_description

customer_one_tax = customer_one_total * sales_tax

customer_one_total += customer_one_tax

print("Customer One Items:")
print(customer_one_itemization)

print("Customer One Total:")
print(customer_one_total)

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////