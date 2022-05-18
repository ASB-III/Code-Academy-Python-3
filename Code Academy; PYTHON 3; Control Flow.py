Code Academy; PYTHON 3; Control Flow

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Cheat Sheet

elif Statement
The Python elif statement allows for continued checks to be performed after an initial if statement. An elif statement differs from the else statement because another expression is provided to be checked, just as with the initial if statement.

If the expression is True, the indented code following the elif is executed. If the expression evaluates to False, the code can continue to an optional else statement. Multiple elif statements can be used following an initial if to perform a series of checks. Once an elif expression evaluates to True, no further elif statements are executed.

# elif Statement
 
pet_type = "fish"
 
if pet_type == "dog":
  print("You have a dog.")
elif pet_type == "cat":
  print("You have a cat.")
elif pet_type == "fish":
  # this is performed
  print("You have a fish")
else:
  print("Not sure!")
or Operator
The Python or operator combines two Boolean expressions and evaluates to True if at least one of the expressions returns True. Otherwise, if both expressions are False, then the entire expression evaluates to False.

True or True      # Evaluates to True
True or False     # Evaluates to True
False or False    # Evaluates to False
1 < 2 or 3 < 1    # Evaluates to True
3 < 1 or 1 > 6    # Evaluates to False
1 == 1 or 1 < 2   # Evaluates to True
Equal Operator ==
The equal operator, ==, is used to compare two values, variables or expressions to determine if they are the same.

If the values being compared are the same, the operator returns True, otherwise it returns False.

The operator takes the data type into account when making the comparison, so a string value of "2" is not considered the same as a numeric value of 2.

# Equal operator
 
if 'Yes' == 'Yes':
  # evaluates to True
  print('They are equal')
 
if (2 > 1) == (5 < 10):
  # evaluates to True
  print('Both expressions give the same result')
 
c = '2'
d = 2
 
if c == d:
  print('They are equal')
else:
  print('They are not equal')
Not Equals Operator !=
The Python not equals operator, !=, is used to compare two values, variables or expressions to determine if they are NOT the same. If they are NOT the same, the operator returns True. If they are the same, then it returns False.

The operator takes the data type into account when making the comparison so a value of 10 would NOT be equal to the string value "10" and the operator would return True. If expressions are used, then they are evaluated to a value of True or False before the comparison is made by the operator.

# Not Equals Operator
 
if "Yes" != "No":
  # evaluates to True
  print("They are NOT equal")
 
val1 = 10
val2 = 20
 
if val1 != val2:
  print("They are NOT equal")
 
if (10 > 1) != (10 > 1000):
  # True != False
  print("They are NOT equal")
Comparison Operators
In Python, relational operators compare two values or expressions. The most common ones are:

< less than
> greater than
<= less than or equal to
>= greater than or equal too
If the relation is sound, then the entire expression will evaluate to True. If not, the expression evaluates to False.

a = 2
b = 3
a < b  # evaluates to True
a > b  # evaluates to False
a >= b # evaluates to False
a <= b # evaluates to True
a <= a # evaluates to True
if Statement
The Python if statement is used to determine the execution of code based on the evaluation of a Boolean expression.

If the if statement expression evaluates to True, then the indented code following the statement is executed.
If the expression evaluates to False then the indented code following the if statement is skipped and the program executes the next line of code which is indented at the same level as the if statement.
# if Statement
 
test_value = 100
 
if test_value > 1:
  # Expression evaluates to True
  print("This code is executed!")
 
if test_value > 1000:
  # Expression evaluates to False
  print("This code is NOT executed!")
 
print("Program continues at this point.")
else Statement
The Python else statement provides alternate code to execute if the expression in an if statement evaluates to False.

The indented code for the if statement is executed if the expression evaluates to True. The indented code immediately following the else is executed only if the expression evaluates to False. To mark the end of the else block, the code must be unindented to the same level as the starting if line.

# else Statement
 
test_value = 50
 
if test_value < 1:
  print("Value is < 1")
else:
  print("Value is >= 1")
 
test_string = "VALID"
 
if test_string == "NOT_VALID":
  print("String equals NOT_VALID")
else:
  print("String equals something else!")
and Operator
The Python and operator performs a Boolean comparison between two Boolean values, variables, or expressions. If both sides of the operator evaluate to True then the and operator returns True. If either side (or both sides) evaluates to False, then the and operator returns False. A non-Boolean value (or variable that stores a value) will always evaluate to True when used with the and operator.

True and True     # Evaluates to True
True and False    # Evaluates to False
False and False   # Evaluates to False
1 == 1 and 1 < 2  # Evaluates to True
1 < 2 and 3 < 1   # Evaluates to False
"Yes" and 100     # Evaluates to True
Boolean Values
Booleans are a data type in Python, much like integers, floats, and strings. However, booleans only have two values:

True
False
Specifically, these two values are of the bool type. Since booleans are a data type, creating a variable that holds a boolean value is the same as with other data types.

is_true = True
is_false = False
 
print(type(is_true)) 
# will output: <class 'bool'>
not Operator
The Python Boolean not operator is used in a Boolean expression in order to evaluate the expression to its inverse value. If the original expression was True, including the not operator would make the expression False, and vice versa.

not True     # Evaluates to False
not False    # Evaluates to True
1 > 2        # Evaluates to False
not 1 > 2    # Evaluates to True
1 == 1       # Evaluates to True
not 1 == 1   # Evaluates to False
SyntaxError
A SyntaxError is reported by the Python interpreter when some portion of the code is incorrect. This can include misspelled keywords, missing or too many brackets or parenthesis, incorrect operators, missing or too many quotation marks, or other conditions.

age = 7 + 5 = 4
 
File "<stdin>", line 1
SyntaxError: can't assign to operator

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Introduction to Control Flow
Imagine waking up in the morning.

You wake up and think, “Ugh. Is it a weekday?”

If so, you have to get up and get dressed and get ready for work or school. If not, you can sleep in a bit longer and catch a couple extra Z’s. But alas, it is a weekday, so you are up and dressed and you go to look outside, “What’s the weather like? Do I need an umbrella?”

These questions and decisions control the flow of your morning, each step and result is a product of the conditions of the day and your surroundings. Your computer, just like you, goes through a similar flow every time it executes code. A program will run (wake up) and start moving through its checklists, is this condition met, is that condition met, okay let’s execute this code and return that value.

This is the control flow of your program. In Python, your script will execute from the top down, until there is nothing left to run. It is your job to include gateways, known as conditional statements, to tell the computer when it should execute certain blocks of code. If these conditions are met, then run this function.

Over the course of this lesson, you will learn how to build conditional statements using boolean expressions, and manage the control flow in your code.

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Boolean Expressions
In order to build control flow into our program, we want to be able to check if something is true or not. A boolean expression is a statement that can either be True or False.

Let’s go back to the ‘waking up’ example. The first question, “Is today a weekday?” can be written as a boolean expression:

Today is a weekday.
This expression can be True if today is Tuesday, or it can be False if today is Saturday. There are no other options.

Consider the phrase:

Friday is the best day of the week.
Is this a boolean expression?

No, this statement is an opinion and is not objectively True or False. Someone else might say that “Wednesday is the best weekday,” and their statement would be no less True or False than the one above.

How about the phrase:

Sunday starts with the letter 'C'.
Is this a boolean expression?

Yes! This expression can only be True or False, which makes it a boolean expression. Even though the statement itself is false (Sunday starts with the letter ‘C’), it is still a boolean expression.

Instructions
1.
Determine if the following statements are boolean expressions or not. If they are, set the matching variable to the right to "Yes" and if not set the variable to "No". Here’s an example of what to do:

Example statement:

My dog is the cutest dog in the world.
This is an opinion and not a boolean expression, so you would set example_statement to "No" in the editor to the right. Okay, now it’s your turn:

Statement one:

Dogs are mammals.
Statement two:

My dog is named Pavel.
Statement three:

Dogs make the best pets.
Statement four:

Cats are female dogs.

example_statement = "No"

statement_one = "Yes"

statement_two = "Yes"

statement_three = "No"

statement_four = "Yes"

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Relational Operators: Equals and Not Equals

Now that we understand what boolean expressions are, let’s learn to create them in Python. We can create a boolean expression by using relational operators.

Relational operators compare two items and return either True or False. For this reason, you will sometimes hear them called comparators.

The two relational operators we’ll cover first are:

Equals: ==
Not equals: !=
These operators compare two items and return True or False if they are equal or not.

We can create boolean expressions by comparing two values using these operators:

1 == 1     # True
 
2 != 4     # True
 
3 == 5     # False
 
'7' == 7   # False
Each of these is an example of a boolean expression.

Why is the last statement false? The '' marks in '7' make it a string, which is different from the integer value 7, so they are not equal. When using relational operators it is important to always be mindful of type.

Instructions
1.
Determine if the following boolean expressions are True or False. Input your answer as True or False in the appropriate variable to the right.

Statement one:

(5 * 2) - 1 == 8 + 1

Statement two:

13 - 6 != (3 * 2) + 1

Statement three:

3 * (2 - 1) == 4 - 1

statement_one = True

statement_two = False

statement_three = True

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Boolean Variables

Before we go any further, let’s talk a little bit about True and False. You may notice that when you type them in the code editor (with uppercase T and F), they appear in a different color than variables or strings. This is because True and False are their own special type: bool.

True and False are the only bool types, and any variable that is assigned one of these values is called a boolean variable.

Boolean variables can be created in several ways. The easiest way is to simply assign True or False to a variable:

set_to_true = True
set_to_false = False
You can also set a variable equal to a boolean expression.

bool_one = 5 != 7 
bool_two = 1 + 1 != 2
bool_three = 3 * 3 == 9
These variables now contain boolean values, so when you reference them they will only return the True or False values of the expression they were assigned.

print(bool_one)    # True
 
print(bool_two)    # False
 
print(bool_three)  # True

1.
Create a variable named my_baby_bool and set it equal to "true".

Checkpoint 2 Passed

Stuck? Get a hint
2.
Check the type of my_baby_bool using type(my_baby_bool).

You’ll have to print it to get the results to display in the terminal.

Checkpoint 3 Passed

Stuck? Get a hint
3.
It’s not a boolean variable! Boolean values True and False always need to be capitalized and do not have quotation marks.

Create a variable named my_baby_bool_two and set it equal to True.

Checkpoint 4 Passed

Stuck? Get a hint
4.
Check the type of my_baby_bool_two and make sure you successfully created a boolean variable.

You’ll have to print it to get the results to display in the terminal.

my_baby_bool = "true"

print(type(my_baby_bool))

my_baby_bool_two = True

print(type(my_baby_bool_two))

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

If Statement

“Okay okay okay, boolean variables, boolean expressions, blah blah blah, I thought I was learning how to build control flow into my code!”

You are, I promise you!

Understanding boolean variables and expressions is essential because they are the building blocks of conditional statements.

Recall the waking-up example from the beginning of this lesson. The decision-making process of “Is it raining? If so, bring an umbrella” is a conditional statement.

Here it is phrased in a different way:

If it is raining, then bring an umbrella.
Can you pick out the boolean expression here?

Right, "it is raining" is the boolean expression, and this conditional statement is checking to see if it is True.

If "it is raining" == True then the rest of the conditional statement will be executed and you will bring an umbrella.

This is the form of a conditional statement:

If [it is raining], then [bring an umbrella]
In Python, it looks very similar:

if is_raining:
  print("bring an umbrella")
You’ll notice that instead of “then” we have a colon, :. That tells the computer that what’s coming next is what should be executed if the condition is met.

Let’s take a look at another conditional statement:

if 2 == 4 - 2: 
  print("apple")
Will this code print apple to the terminal?

Yes, because the condition of the if statement, 2 == 4 - 2 is True.

Let’s work through a couple more together.

Instructions
1.
In script.py, there is an if statement. I wrote this because my coworker Dave kept using my computer without permission and he is a real doofus. If the user_name is Dave, it tells him to stay off my computer.

Enter a user name in the field for user_name and try running the program.

2.
Oh no! We got a SyntaxError! This happens when we make a small error in the syntax of the conditional statement.

Read through the error message carefully and see if you can find the error. Then, fix it, and run the code again.

Checkpoint 3 Passed

Stuck? Get a hint
3.
Ugh! Dave got around my security and has been logging onto my computer using our coworker Angela’s user name, angela_catlady_87.

Set your user_name to be angela_catlady_87.

Update the program with a second if statement so it checks for Angela’s user name as well and prints

"I know it is you, Dave! Go away!"
in response. That’ll teach him!

# Enter a user name here, make sure to make it a string
user_name = "angela_catlady_87"

if user_name == "Dave":
  print("Get off my computer Dave!")

if user_name == "angela_catlady_87":
  print("I know it is you, Dave! Go away!")

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Relational Operators II
Now that we’ve added conditional statements to our toolkit for building control flow, let’s explore more ways to create boolean expressions. So far we know two relational operators, equals and not equals, but there are a ton (well, four) more:

> greater than
>= greater than or equal to
< less than
<= less than or equal to
Let’s say we’re running a movie streaming platform and we want to write a program that checks if our users are over 13 when showing them a PG-13 movie. We could write something like:

if age <= 13:
  print("Sorry, parental control required")
This function will take the user’s age and compare it to the number 13. If age is less than or equal to 13, it will print out a message.

Let’s try some more!

Instructions
1.
Create an if statement that checks if x and y are equal, print the string below if so:

"These numbers are the same"

Stuck? Get a hint
2.
The nearby college, Calvin Coolidge’s Cool College (or 4C, as the locals call it) requires students to earn 120 credits to graduate.

Write an if statement that checks if the student has enough credits to graduate. If they do, print the string:

"You have enough credits to graduate!"
Can a student with 120 credits graduate from Calvin Coolidge’s Cool College?

x = 20
y = 20

# Write the first if statement here:

if x == y:
  print("These numbers are the same")

credits = 120

# Write the second if statement here:

if credits >= 120:
  print("You have enough credits to graduate!")

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Boolean Operators: and
Often, the conditions you want to check in your conditional statement will require more than one boolean expression to cover. In these cases, you can build larger boolean expressions using boolean operators. These operators (also known as logical operators) combine smaller boolean expressions into larger boolean expressions.

There are three boolean operators that we will cover:

and
or
not
Let’s start with and.

and combines two boolean expressions and evaluates as True if both its components are True, but False otherwise.

Consider the example:

Oranges are a fruit and carrots are a vegetable.
This boolean expression is comprised of two smaller expressions, oranges are a fruit and carrots are a vegetable, both of which are True and connected by the boolean operator and, so the entire expression is True.

Let’s look at an example of some AND statements in Python:

(1 + 1 == 2) and (2 + 2 == 4)   # True
 
(1 > 9) and (5 != 6)            # False
 
(1 + 1 == 2) and (2 < 1)        # False
 
(0 == 10) and (1 + 1 == 1)      # False
Notice that in the second and third examples, even though part of the expression is True, the entire expression as a whole is False because the other statement is False. The fourth statement is also False because both components are False.

Instructions
1.
Set the variables statement_one and statement_two equal to the results of the following boolean expressions:

Statement one:

(2 + 2 + 2 >= 6) and (-1 * -1 < 0)
Statement two:

(4 * 2 <= 8) and (7 - 1 == 6)

2.
Let’s return to Calvin Coolidge’s Cool College. 120 credits aren’t the only graduation requirement, you also need to have a GPA of 2.0 or higher.

Rewrite the if statement so that it checks to see if a student meets both requirements using an and statement.

If they do, return the string:

"You meet the requirements to graduate!"



statement_one = (2 + 2 + 2 >= 6) and (-1 * -1 < 0)

statement_two = (4 * 2 <= 8) and (7 - 1 == 6)

credits = 120
gpa = 3.4

if credits >= 120 and gpa >= 2.0 :
  print("You meet the requirements to graduate!")

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Boolean Operators: or
The boolean operator or combines two expressions into a larger expression that is True if either component is True.

Consider the statement

Oranges are a fruit or apples are a vegetable.
This statement is composed of two expressions: oranges are a fruit which is True and apples are a vegetable which is False. Because the two expressions are connected by the or operator, the entire statement is True. Only one component needs to be True for an or statement to be True.

In English, or implies that if one component is True, then the other component must be False. This is not true in Python. If an or statement has two True components, it is also True.

Let’s take a look at a couple of examples in Python:

True or (3 + 4 == 7)    # True
(1 - 1 == 0) or False   # True
(2 < 0) or True         # True
(3 == 8) or (3 > 4)     # False
Notice that each or statement that has at least one True component is True, but the final statement has two False components, so it is False.

Instructions
1.
Set the variables statement_one and statement_two equal to the results of the following boolean expressions:

Statement one:

(2 - 1 > 3) or (-5 * 2 == -10)
Statement two:

(9 + 5 <= 15) or (7 != 4 + 3)

2.
The registrar’s office at Calvin Coolidge’s Cool College has another request. They want to send out a mailer with information on the commencement ceremonies to students who have met at least one requirement for graduation (120 credits and 2.0 GPA).

Write an if statement that checks if a student either has 120 or more credits or a GPA 2.0 or higher, and if so prints:

"You have met at least one of the requirements."


statement_one = (2 - 1 > 3) or (-5 * 2 == -10)

statement_two = (9 + 5 <= 15) or (7 != 4 + 3)

credits = 118
gpa = 2.0

if credits >= 120 or gpa >= 2.0:
  print("You have met at least one of the requirements.")

  /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Boolean Operators: not
The final boolean operator we will cover is not. This operator is straightforward: when applied to any boolean expression it reverses the boolean value. So if we have a True statement and apply a not operator we get a False statement.

not True == False
not False == True
Consider the following statement:

Oranges are not a fruit.
Here, we took the True statement oranges are a fruit and added a not operator to make the False statement oranges are not a fruit.

This example in English is slightly different from the way it would appear in Python because in Python we add the not operator to the very beginning of the statement. Let’s take a look at some of those:

not 1 + 1 == 2  # False
not 7 < 0       # True
Instructions
1.
Set the variables statement_one and statement_two equal to the results of the following boolean expressions:

Statement one:

not (4 + 5 <= 9)
Statement two:

not (8 * 2) != 20 - 4
Checkpoint 2 Passed
2.
The registrar’s office at Calvin Coolidge’s Cool College has been so impressed with your work so far that they have another task for you.

They want you to return to a previous if statement and add in several checks using and and not statements:

If a student’s credits is not greater or equal to 120, it should print:
"You do not have enough credits to graduate."
If their gpa is not greater or equal to 2.0, it should print:
"Your GPA is not high enough to graduate."
If their credits is not greater than or equal to 120 and their gpa is not greater than or equal to 2.0, it should print:
"You do not meet either requirement to graduate!"
Make sure your return value matches those strings exactly. Capitalization, punctuation, and spaces matter!


statement_one = not (4 + 5 <= 9)

statement_two = not (8 * 2) != 20 - 4

credits = 120
gpa = 1.8

if not credits >= 120:
  print("You do not have enough credits to graduate")
if not gpa >= 2.0:
  print("Your GPA is not high enough to graduate")
if not (credits >= 120) and not (gpa >= 2.0):
  print("You do not meet either requirement to graduate!")

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Else Statements
As you can tell from your work with Calvin Coolidge’s Cool College, once you start including lots of if statements in a function the code becomes a little cluttered and clunky. Luckily, there are other tools we can use to build control flow.

else statements allow us to elegantly describe what we want our code to do when certain conditions are not met.

else statements always appear in conjunction with if statements. Consider our waking-up example to see how this works:

if weekday:
  print("wake up at 6:30")
else:
  print("sleep in")
In this way, we can build if statements that execute different code if conditions are or are not met. This prevents us from needing to write if statements for each possible condition, we can instead write a blanket else statement for all the times the condition is not met.

Let’s return to our if statement for our movie streaming platform. Previously, all it did was check if the user’s age was over 13 and if so, print out a message. We can use an else statement to return a message in the event the user is too young to watch the movie.

if age >= 13:
  print("Access granted.")
else:
  print("Sorry, you must be 13 or older to watch this movie.")
Instructions
1.
Calvin Coolidge’s Cool College has another request for you. They want you to add an additional check to a previous if statement. If a student is failing to meet both graduation requirements, they want it to print:

"You do not meet the requirements to graduate."
Add an else statement to the existing if statement.

credits = 120
gpa = 1.9

if (credits >= 120) and (gpa >= 2.0):
  print("You meet the requirements to graduate!")
else:
  print("You do not meet the requirements to graduate")

  /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Else If Statements
We have if statements, we have else statements, we can also have elif statements.

Now you may be asking yourself, what the heck is an elif statement? It’s exactly what it sounds like, “else if”. An elif statement checks another condition after the previous if statements conditions aren’t met.

We can use elif statements to control the order we want our program to check each of our conditional statements. First, the if statement is checked, then each elif statement is checked from top to bottom, then finally the else code is executed if none of the previous conditions have been met.

Let’s take a look at this in practice. The following if statement will display a “thank you” message after someone donates to a charity; there will be a curated message based on how much was donated.

print("Thank you for the donation!")
 
if donation >= 1000:
  print("You've achieved platinum status")
elif donation >= 500:
  print("You've achieved gold donor status")
elif donation >= 100:
  print("You've achieved silver donor status")
else:
  print("You've achieved bronze donor status")
Take a second to think about this function. What would happen if all of the elif statements were simply if statements? If you donated $1100.00, then the first three messages would all print because each if condition had been met.

But because we used elif statements, it checks each condition sequentially and only prints one message. If I donate $600.00, the code first checks if that is over 1000, which it is not, then it checks if it’s over 500, which it is, so it prints that message, then because all of the other statements are elif and else, none of them get checked and no more messages get printed.

Try your hand at some other elif statements.

Instructions
1.
Calvin Coolidge’s Cool College has noticed that students prefer to get letter grades.

Write an if/elif/else statement that:

If grade is 90 or higher, print "A"
Else if grade is 80 or higher, print "B"
Else if grade is 70 or higher, print "C"
Else if grade is 60 or higher, print "D"
Else, print "F"



grade = 86

if grade >= 90:
  print("A")
elif grade >= 80:
  print("B")
elif grade >= 70:
  print("C")
elif grade >= 60:
  print("D")
else:
  print("F")

  /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Review


Great job! We covered a ton of material in this lesson and we’ve increased the number of tools in our Python toolkit by several-fold. Let’s review what we’ve learned this lesson:

Boolean expressions are statements that can be either True or False
A boolean variable is a variable that is set to either True or False.
We can create boolean expressions using relational operators:
==: Equals
!=: Not equals
>: Greater than
>=: Greater than or equal to
<: Less than
<=: Less than or equal to
if statements can be used to create control flow in your code.
else statements can be used to execute code when the conditions of an if statement are not met.
elif statements can be used to build additional checks into your if statements
Let’s put these skills to the test!

1.
Optional: Little Codey is an interplanetary space boxer, who is trying to win championship belts for various weight categories on other planets within the solar system.

Write a space.py program that helps him keep track of his target weight by:

Checks which number planet is equal to.
It should then compute his weight on the destination planet.
Here is the table of conversion:

#	Planet	Relative Gravity
1	Venus	0.91
2	Mars	0.38
3	Jupiter	2.34
4	Saturn	1.06
5	Uranus	0.92
6	Neptune	1.19

print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
 
weight = 185
planet = 3

# Write an if statement below:

if planet == 1:
  weight = weight * 0.91
elif planet == 2:
  weight = weight * 0.38
elif planet == 3:
  weight = weight * 2.34
elif planet == 4:
  weight = weight * 1.06
elif planet == 5:
  weight = weight * 0.92
elif planet == 6:
  weight = weight * 1.19

print("Your weight:", weight)

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Magic 8-Ball
The Magic 8-Ball is a popular toy developed in the 1950s for fortune-telling or advice seeking.

Write a magic8.py Python program that can answer any “Yes” or “No” question with a different fortune each time it executes.

Magic 8-Ball, should I do this project?

We’ll be using the following 9 possible answers for our Magic 8-Ball:

Yes - definitely.
It is decidedly so.
Without a doubt.
Reply hazy, try again.
Ask again later.
Better not tell you now.
My sources say no.
Outlook not so good.
Very doubtful.
The output of the program will have the following format:

[Name] asks: [Question]
Magic 8-Ball’s answer: [Answer]
For example:

Joe asks: Is this real life?
Magic 8-Ball's answer: Better not tell you now

Let’s get started!

1.
In magic8.py, declare a variable name and assign it to the name of the person who will be asking the Magic 8-Ball.


Stuck? Get a hint
2.
Next, declare a variable question, and assign to a “Yes” or “No” question you’d like to ask the Magic 8-Ball.


Stuck? Get a hint
3.
We want to store the answer of the Magic 8-Ball in another variable, which we’ll call answer. For now, assign this variable to an empty string.


Stuck? Get a hint
Generating a random number
4.
In order for the answer to be different each time we run the program, we will utilize randomly generated values.

Note: This will be something new! But don’t worry, we will try to explain this topic thoroughly and also supply the code.

In Python, we can use the .randint() function from the random module to generate a random number from a range.

But first, let’s import this module so we can use its functions. Add this line of code to the top of magic8.py:

import random

Stuck? Get a hint
5.
Next, we’ll create a variable to store the randomly generated value. Declare a variable called random_number, and assign it to the function call:

random.randint(1, 9)
which will generate a random number between 1 (inclusive) and 9 (inclusive).

Next, add a print() statement that outputs the value of random_number, and run the program several times to ensure random values are being generated as expected.

Once you’re sure this is working as we expected, feel free to comment out this print() statement.


Stuck? Get a hint
Control Flow
6.
Now that we’ve declared all the variables needed, it’s time to implement the core logic of our program!

For this section, we’ll be utilizing control flow using an if/elif/else statement to assign different answers for each randomly generated value.

First, write an if statement where if the random_number is equal to 1, answer is assigned to the phrase “Yes - definitely.”


Stuck? Get a hint
7.
Next, write an elif statement after the if statement where if the random_number is equal to 2, answer is assigned to the phrase “It is decidedly so”.

Then, continue writing elif statements for each of the remaining phrases for the values 3 to 9.

Recall that the 9 possible answers of the Magic 8-Ball are:

Yes - definitely.

It is decidedly so.

Without a doubt.

Reply hazy, try again.

Ask again later.

Better not tell you now.

My sources say no.

Outlook not so good.

Very doubtful.


Stuck? Get a hint
8.
Following the if/elif statements, add an else statement that will set answer to the string “Error”, if the number was accidentally assigned a value outside of our range.


Stuck? Get a hint
Seeing the result
9.
Now, let’s see our program in action! Write a print() statement to output the asker’s name and their question, which should be in the following format:

[Name] asks: [Question]
For example, when we run the program, the output should look something like:

Joe asks: Will I win the lottery?

Stuck? Get a hint
10.
Add a second print() statement that will output the Magic 8-Ball’s answer in the following format:

Magic 8-Ball's answer: [answer]
For example, when running the program it should look something like:

Magic 8-Ball's answer: My sources say no

Stuck? Get a hint
11.
Great job! You’ve successfully utilized your knowledge of conditionals and previous fundamental Python concepts to create a program that generates different fortunes.

Run your program several times to see that it’s working as expected.


Stuck? Get a hint
Optional Challenges
12.
If you’re up for some more challenges, try implementing the following features to your program.

So far, the Magic 8-Ball provides 9 possible fortunes. Try to add a few more possible answers to the program.

To do this, you will need to increase the range of randomly generated numbers and add additional elif statements for each new answer.


Stuck? Get a hint
13.
What if the asker does not provide a name, such that the value of name is an empty string? If the name string is empty, the output of the program looks like the following:

 asks: Will I win the lottery?
Magic 8 Ball's answer: Outlook not so good
As you can see, the formatting of the output can use some improvement when there is no name provided.

We can address this by printing out just the question, such that it looks like the following:

Question: Will I win the lottery?
Magic 8-Ball's answer: Outlook not so good
You can implement this by creating an if/else statement such that:

If the name is an empty string, it will only print the question.
Else, the player’s name and question are both printed.

Stuck? Get a hint
14.
What if the question string is empty? If the user does not provide any question, then the Magic 8-Ball cannot provide a fortune, otherwise, the fabric of reality is at risk!

To ensure that the fabric of reality is safe, we can create an if/else statement where:

If the question is an empty string, print out a message to the user.
Else, print the name and question, with the Magic 8-Ball’s answer.

Stuck? Get a hint
Solution
15.
Don’t forget to check off all the tasks before moving on.

Sample solutions:

magic8.py
P.S. If you make something cool, share it with us!


import random

name = "joe"

question = "Will I win the lottery"

answer = ""

random_number = random.randint(1, 10)
# print(random_number)

if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer ="It is decidedly so."
elif random_number == 3:
  answer ="Without a doubt."
elif random_number == 4:
  answer ="Reply hazy, try again."
elif random_number == 5:
  answer ="Ask again later."
elif random_number == 6:
  answer ="Better not tell you now."
elif random_number == 7:
  answer ="My sources say no."
elif random_number == 8:
  answer ="Outlook not so good."
elif random_number == 9:
  answer ="Very Doubtful."
elif random_number == 10:
  answer ="Signs point to yes"
#...
else:
  answer = "Error"
if name == "":
  print("Question: " + question)
else:  
  print(name + " asks: " + question)

print("Magic 8-Ball's answer: " + answer)

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Sal's Shipping

Sal runs the biggest shipping company in the tri-county area, Sal’s Shippers. Sal wants to make sure that every single one of his customers has the best, and most affordable experience shipping their packages.

In this project, you’ll build a program that will take the weight of a package and determine the cheapest way to ship that package using Sal’s Shippers.

Sal’s Shippers has several different options for a customer to ship their package:

Ground Shipping, which is a small flat charge plus a rate based on the weight of your package.
Ground Shipping Premium, which is a much higher flat charge, but you aren’t charged for weight.
Drone Shipping (new), which has no flat charge, but the rate based on weight is triple the rate of ground shipping.
Here are the prices:

Ground Shipping

Weight of Package	Price per Pound	Flat Charge
2 lb or less	$1.50	$20.00
Over 2 lb but less than or equal to 6 lb	$3.00	$20.00
Over 6 lb but less than or equal to 10 lb	$4.00	$20.00
Over 10 lb	$4.75	$20.00

Ground Shipping Premium

Flat charge: $125.00

Drone Shipping

Weight of Package	Price per Pound	Flat Charge
2 lb or less	$4.50	$0.00
Over 2 lb but less than or equal to 6 lb	$9.00	$0.00
Over 6 lb but less than or equal to 10 lb	$12.00	$0.00
Over 10 lb	$14.25	$0.00

Write a shipping.py Python program that asks the user for the weight of their package and then tells them which method of shipping is cheapest and how much it will cost to ship their package using Sal’s Shippers.

Tasks
8/9 Complete
Mark the tasks as complete by checking them off
Ground Shipping:
1.
First things first, define a weight variable and set it equal to any number.


Stuck? Get a hint
2.
Next, we need to know how much it costs to ship a package of given weight by normal ground shipping based on the “Ground shipping” table above.

Write a comment that says “Ground Shipping”.

Create an if/elif/else statement for the cost of ground shipping. It should check for weight, and print the cost of shipping a package of that weight.


Stuck? Get a hint
3.
A package that weighs 8.4 pounds should cost $53.60 to ship with normal ground shipping:

8.4\ lb \times \$4.00 + \$20.00 = \$53.608.4 lb×$4.00+$20.00=$53.60
Test that your ground shipping function gets the same value.


Stuck? Get a hint
Ground Shipping Premium:
4.
We’ll also need to make sure we include the price of premium ground shipping in our code.

Create a variable for the cost of premium ground shipping.

Note: This does not need to be an if statement because the price of premium ground shipping does not change with the weight of the package.


Stuck? Get a hint
5.
Print it out for the user just in case they forgot!


Stuck? Get a hint
Drone Shipping:
6.
Write a comment for this section of the code, “Drone Shipping”.

Create an if/elif/else statement for the cost of drone shipping. This statement should check against weight and print the cost of shipping a package of that weight.


Hint
This if statement should look very similar to the if statement you wrote for ground shipping. You can even copy the syntax directly and just change the numbers!

7.
A package that weighs 1.5 pounds should cost $6.75 to ship by drone:

1.5\ lb \times \$4.50 + \$0.00 = \$6.751.5 lb×$4.50+$0.00=$6.75
Test that your drone shipping function gets the same value.

Solution:
8.
Great job! Now, test everything one more time!

What is the cheapest method of shipping a 4.8 pound package and how much would it cost?

What is the cheapest method of shipping a 41.5 pound package and how much would it cost?

(See hint for answers)


Stuck? Get a hint
9.
Don’t forget to check off all the tasks before moving on.

Sample solutions:

shipping.py
P.S. If you make something cool, share it with us!

#Al
#Sal's shipping

weight = 1.5

#ground shipping calculator

if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight <= 6:
  cost_ground = weight * 3.00 + 20
elif weight <= 10:
  cost_ground = weight * 4.00 + 20
else:
  cost_ground = weight * 4.75 + 20

print("Ground Shipping Cost $", cost_ground)

cost_ground_premium = 125.00

print("Ground Shipping Premium $", cost_ground_premium)

#Drone Shipping Calculator

if weight <= 2:
  cost_drone = weight * 4.5
elif weight <= 6:
  cost_drone = weight * 9.00
elif weight <= 10:
  cost_drone = weight * 12.00
else:
  cost_drone = weight * 14.25

print("Drone Shipping Cost $", cost_drone)

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

