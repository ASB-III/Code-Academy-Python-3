Code Academy; Python 3; Working With Lists

Now that we know how to create and access list data, we can start to explore additional ways of working with lists.

In this lesson, you’ll learn how to:

Add and remove items from a list using a specific index.
Create lists with continuous values.
Get the length of a list.
Select portions of a list (called slicing).
Count the number of times that an element appears in a list.
Sort a list of items.
Note: In some of the exercises, we will be using built-in functions in Python. If you haven’t yet explored the concept of a function, it may look a bit new. Below we compare it to the method syntax we learned in the earlier lesson.

Here is a preview:

# Example syntax for methods
list.method(input)
 
# Example syntax for a built-in function 
builtinfuncion(input)
Instructions
Take a second to preview some of the things we will be learning by examining the graphic of common list methods and built-in functions.

When you’re ready, continue to the next exercise.



////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

CHEAT SHEET

Lists
In Python, lists are ordered collections of items that allow for easy use of a set of data.

List values are placed in between square brackets [ ], separated by commas. It is good practice to put a space between the comma and the next value. The values in a list do not need to be unique (the same value can be repeated).

Empty lists do not contain any values within the square brackets.

primes = [2, 3, 5, 7, 11]
print(primes)
 
empty_list = []
Adding Lists Together
In Python, lists can be added to each other using the plus symbol +. As shown in the code block, this will result in a new list containing the same items in the same order with the first list’s items coming first.

Note: This will not work for adding one item at a time (use .append() method). In order to add one item, create a new list with a single value and then use the plus symbol to add the list.

items = ['cake', 'cookie', 'bread']
total_items = items + ['biscuit', 'tart']
print(total_items)
# Result: ['cake', 'cookie', 'bread', 'biscuit', 'tart']
Python Lists: Data Types
In Python, lists are a versatile data type that can contain multiple different data types within the same square brackets. The possible data types within a list include numbers, strings, other objects, and even other lists.

numbers = [1, 2, 3, 4, 10]
names = ['Jenny', 'Sam', 'Alexis']
mixed = ['Jenny', 1, 2]
list_of_lists = [['a', 1], ['b', 2]]
List Method .append()
In Python, you can add values to the end of a list using the .append() method. This will place the object passed in as a new element at the very end of the list. Printing the list afterwards will visually show the appended value. This .append() method is not to be confused with returning an entirely new list with the passed object.

orders = ['daisies', 'periwinkle']
orders.append('tulips')
print(orders)
# Result: ['daisies', 'periwinkle', 'tulips']
Zero-Indexing
In Python, list index begins at zero and ends at the length of the list minus one. For example, in this list, 'Andy' is found at index 2.

names = ['Roger', 'Rafael', 'Andy', 'Novak']
List Indices
Python list elements are ordered by index, a number referring to their placement in the list. List indices start at 0 and increment by one.

To access a list element by index, square bracket notation is used: list[index].

berries = ["blueberry", "cranberry", "raspberry"]
 
berries[0]   # "blueberry"
berries[2]   # "raspberry"
Negative List Indices
Negative indices for lists in Python can be used to reference elements in relation to the end of a list. This can be used to access single list elements or as part of defining a list range. For instance:

To select the last element, my_list[-1].
To select the last three elements, my_list[-3:].
To select everything except the last two elements, my_list[:-2].
soups = ['minestrone', 'lentil', 'pho', 'laksa']
soups[-1]   # 'laksa'
soups[-3:]  # 'lentil', 'pho', 'laksa'
soups[:-2]  # 'minestrone', 'lentil'
Modifying 2D Lists
In order to modify elements in a 2D list, an index for the sublist and the index for the element of the sublist need to be provided. The format for this is list[sublist_index][element_in_sublist_index] = new_value.

# A 2D list of names and hobbies
class_name_hobbies = [["Jenny", "Breakdancing"], ["Alexus", "Photography"], ["Grace", "Soccer"]]
 
# The sublist of Jenny is at index 0. The hobby is at index 1 of the sublist. 
class_name_hobbies[0][1] = "Meditation"
print(class_name_hobbies)
 
# Output
# [["Jenny", "Meditation"], ["Alexus", "Photography"], ["Grace", "Soccer"]]
Accessing 2D Lists
In order to access elements in a 2D list, an index for the sublist and the index for the element of the sublist both need to be provided. The format for this is list[sublist_index][element_in_sublist_index].

# 2D list of people's heights
heights = [["Noelle", 61], ["Ali", 70], ["Sam", 67]]
# Access the sublist at index 0, and then access the 1st index of that sublist. 
noelles_height = heights[0][1] 
print(noelles_height)
 
# Output
# 61
List Method .remove()
The .remove() method in Python is used to remove an element from a list by passing in the value of the element to be removed as an argument. In the case where two or more elements in the list have the same value, the first occurrence of the element is removed.

# Create a list
shopping_line = ["Cole", "Kip", "Chris", "Sylvana", "Chris"]
 
# Removes the first occurance of "Chris"
shopping_line.remove("Chris")
print(shopping_line)
 
# Output
# ["Cole", "Kip", "Sylvana", "Chris"]
List Method .count()
The .count() Python list method searches a list for whatever search term it receives as an argument, then returns the number of matching entries found.

backpack = ['pencil', 'pen', 'notebook', 'textbook', 'pen', 'highlighter', 'pen']
numPen = backpack.count('pen')
 
print(numPen)
# Output: 3
Determining List Length with len()
The Python len() function can be used to determine the number of items found in the list it accepts as an argument.

knapsack = [2, 4, 3, 7, 10]
size = len(knapsack)
print(size) 
# Output: 5
List Method .sort()
The .sort() Python list method will sort the contents of whatever list it is called on. Numerical lists will be sorted in ascending order, and lists of Strings will be sorted into alphabetical order. It modifies the original list, and has no return value.

exampleList = [4, 2, 1, 3]
exampleList.sort()
print(exampleList)
# Output: [1, 2, 3, 4]
List Slicing
A slice, or sub-list of Python list elements can be selected from a list using a colon-separated starting and ending point.

The syntax pattern is myList[START_NUMBER:END_NUMBER]. The slice will include the START_NUMBER index, and everything until but excluding the END_NUMBER item.

When slicing a list, a new list is returned, so if the slice is saved and then altered, the original list remains the same.

tools = ['pen', 'hammer', 'lever']
tools_slice = tools[1:3] # ['hammer', 'lever']
tools_slice[0] = 'nail'
 
# Original list is unaltered:
print(tools) # ['pen', 'hammer', 'lever']
sorted() Function
The Python sorted() function accepts a list as an argument, and will return a new, sorted list containing the same elements as the original. Numerical lists will be sorted in ascending order, and lists of Strings will be sorted into alphabetical order. It does not modify the original, unsorted list.

unsortedList = [4, 2, 1, 3]
sortedList = sorted(unsortedList)
print(sortedList)
# Output: [1, 2, 3, 4]
List Method .insert()
The Python list method .insert() allows us to add an element to a specific index in a list.

It takes in two inputs:

The index that you want to insert into.
The element that you want to insert at the specified index.
# Here is a list representing a line of people at a store
store_line = ["Karla", "Maxium", "Martim", "Isabella"]
 
# Here is how to insert "Vikor" after "Maxium" and before "Martim"
store_line.insert(2, "Vikor")
 
print(store_line) 
# Output: ['Karla', 'Maxium', 'Vikor', 'Martim', 'Isabella']
List Method .pop()
The .pop() method allows us to remove an element from a list while also returning it. It accepts one optional input which is the index of the element to remove. If no index is provided, then the last element in the list will be removed and returned.

cs_topics = ["Python", "Data Structures", "Balloon Making", "Algorithms", "Clowns 101"]
 
# Pop the last element
removed_element = cs_topics.pop()
 
print(cs_topics)
print(removed_element)
 
# Output:
# ['Python', 'Data Structures', 'Balloon Making', 'Algorithms']
# 'Clowns 101'
 
# Pop the element "Baloon Making"
cs_topics.pop(2)
print(cs_topics)
 
# Output:
# ['Python', 'Data Structures', 'Algorithms']

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Adding by Index: Insert

The Python list method .insert() allows us to add an element to a specific index in a list.

The .insert() method takes in two inputs:

The index you want to insert into.
The element you want to insert at the specified index.
The .insert() method will handle shifting over elements and can be used with negative indices.

To see it in action let’s imagine we have a list representing a line at a store:

store_line = ["Karla", "Maxium", "Martim", "Isabella"]
"Maxium" saved a spot for his friend "Vikor" and we need to adjust the list to add him into the line right behind "Maxium".

For this example, we can assume that "Karla" is the front of the line and the rest of the elements are behind her.

Here is how we would use the .insert() method to insert "Vikor" :

store_line.insert(2, "Vikor")
print(store_line) 
Would output:

 ['Karla', 'Maxium', 'Vikor', 'Martim', 'Isabella']
Some important things to note:

The order and number of the inputs is important. The .insert() method expects two inputs, the first being a numerical index, followed by any value as the second input.

When we insert an element into a list, all elements from the specified index and up to the last index are shifted one index to the right. This does not apply to inserting an element to the very end of a list as it will simply add an additional index and no other elements will need to shift.

Let’s practice using .insert()!

Instructions
1.
We are helping out a popular grocery store called Jiho’s Produce.

Every week the store has to choose the order in which it displays some of its popular items on sale in the front window to attract customers.

Jiho, the store owner, likes to store the items for the display in a list.

Check out the current display list in our code editor. Click Run to print out the list.

2.
Jiho found out some great news! "Pineapple" is back in stock.

Jiho would like to put "Pineapple" in the front of the list so it is the first item customers see in the display window.

Use .insert() to add "Pineapple" to the front of the list.

Print the resulting list to see the change.

Note: For this list, the front will be the element at index 0

front_display_list = ["Mango", "Filet Mignon", "Chocolate Milk"]
print(front_display_list)

# Your code below: 
front_display_list.insert(0, "Pineapple")
print(front_display_list)

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Removing by Index: Pop

Just as we learned to insert elements at specific indices, Python gives us a method to remove elements at a specific index using a method called .pop().

The .pop() method takes an optional single input:

The index for the element you want to remove.
To see it in action, let’s consider a list called cs_topics that stores a collection of topics one might study in a computer science program.

cs_topics = ["Python", "Data Structures", "Balloon Making", "Algorithms", "Clowns 101"]
Two of these topics don’t look like they belong, let’s see how we remove them using .pop().

First let’s remove "Clowns 101":

removed_element = cs_topics.pop()
print(cs_topics)
print(removed_element)
Would output:

['Python', 'Data Structures', 'Balloon Making', 'Algorithms']
'Clowns 101'
Notice two things about this example:

The method can be called without a specific index. Using .pop() without an index will remove whatever the last element of the list is. In our case "Clowns 101" gets removed.

.pop() is unique in that it will return the value that was removed. If we wanted to know what element was deleted, simply assign a variable to the call of the .pop() method. In this case, we assigned it to removed_element.

Lastly let’s remove "Balloon Making":

cs_topics.pop(2)
print(cs_topics)
Would output:

['Python', 'Data Structures', 'Algorithms']
Notice two things about this example:

The method can be called with an optional specific index to remove. In our case, the index 2 removes the value of "Balloon Making".
We don’t have to save the removed value to any variable if we don’t care to use it later.
Note: Passing in an index that does not exist or calling .pop() on an empty list will both result in an IndexError.

Let’s apply what we learned about the .pop() method.

Instructions
1.
We have decided to pursue the study of data science in addition to our computer science coursework. We signed up for an online school that would help us become proficient.

Check out the current list of topics we will be studying in our code editor.

Click Run to print out the list.

2.
It looks like we have an overlap with our computer science curriculum for the topic of "Python 3".

Let’s remove the topic from the list of data_science_topics using our newly learned .pop() method.

Print data_science_topics to see your result.


Stuck? Get a hint
3.
Looks like there is overlap on the "Algorithms" topic as well. Let’s use .pop() to remove it as well.

Print data_science_topics to see the changes.

data_science_topics = ["Machine Learning", "SQL", "Pandas", "Algorithms", "Statistics", "Python 3"]
print(data_science_topics)

# Your code below: 

data_science_topics.pop()
print(data_science_topics)

data_science_topics.pop(3)
print(data_science_topics)

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Consecutive Lists: Range

Often, we want to create a list of consecutive numbers in our programs. For example, suppose we want a list containing the numbers 0 through 9:

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Typing out all of those numbers takes time and the more numbers we type, the more likely it is that we have a typo that can cause an error.

Python gives us an easy way of creating these types of lists using a built-in function called range().

The function range() takes a single input, and generates numbers starting at 0 and ending at the number before the input.

So, if we want the numbers from 0 through 9, we use range(10) because 10 is 1 greater than 9:

my_range = range(10)
print(my_range)
Would output:

range(0, 10)
Notice something different? The range() function is unique in that it creates a range object. It is not a typical list like the ones we have been working with.

In order to use this object as a list, we have to first convert it using another built-in function called list().

The list() function takes in a single input for the object you want to convert.

We use the list() function on our range object like this:

print(list(my_range))
Would output:

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Let’s try out using range()!

Instructions
1.
Modify number_list so that it is a range containing numbers starting at 0 and up to, but not including, 9.

Checkpoint 2 Passed

Stuck? Get a hint
2.
Create a range called zero_to_seven with the numbers 0 through 7.

Print the result in list form.

number_list = range(3)
print(list(number_list))

number_list = range(9)
print(list(number_list))

zero_to_seven = range(8)
print(list(zero_to_seven))

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

The Power of Range!

By default, range() creates a list starting at 0. However, if we call range() with two inputs, we can create a list that starts at a different number.

For example, range(2, 9) would generate numbers starting at 2 and ending at 8 (just before 9):

my_list = range(2, 9)
print(list(my_list))
Would output:

[2, 3, 4, 5, 6, 7, 8]
If we use a third input, we can create a list that “skips” numbers.

For example, range(2, 9, 2) will give us a list where each number is 2 greater than the previous number:

my_range2 = range(2, 9, 2)
print(list(my_range2))
Would output:

[2, 4, 6, 8]
We can skip as many numbers as we want!

For example, we’ll start at 1 and skip in increments of 10 between each number until we get to 100:

my_range3 = range(1, 100, 10)
print(list(my_range3))
Would output:

[1, 11, 21, 31, 41, 51, 61, 71, 81, 91]
Our list stops at 91 because the next number in the sequence would be 101, which is greater than 100 (our stopping point).

Let’s experiment with our additional range() inputs!

Instructions
1.
Modify the range() function that created the range range_five_three such that it:

Starts at 5
Has a difference of 3 between each item
Ends before 15
Checkpoint 2 Passed

Stuck? Get a hint
2.
Create a range called range_diff_five that:

Starts at 0
Has a difference of 5 between each item
Ends before 40

range_five_three = range(5, 15, 3)
print(range_five_three)

range_diff_five = range(0, 40, 5)
print(range_diff_five)

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Length

Often, we’ll need to find the number of items in a list, usually called its length.

We can do this using a built-in function called len().

When we apply len() to a list, we get the number of elements in that list:

my_list = [1, 2, 3, 4, 5]
 
print(len(my_list))
Would output:

5
Let’s find the length of various lists!

Instructions
1.
Calculate the length of long_list and save it to the variable long_list_len.


Stuck? Get a hint
2.
Use print() to examine long_list_len.


Stuck? Get a hint
3.
We have provided a completed range() function for the variable range_list.

Calculate its length using the function len() and save it to a variable called range_list_length.

Note: Range objects do not need to be converted to lists in order to determine their length


Stuck? Get a hint
4.
Use print() to examine range_list_length.


Stuck? Get a hint
5.
Change the range() function that generates range_list so that it skips 100 instead of 10 steps between items.

How does this change range_list_len?

long_list = [1, 5, 6, 7, -23, 69.5, True, "very", "long", "list", "that", "keeps", "going.", "Let's", "practice", "getting", "the", "length"]

range_list = range(2, 3000, 100)

# Your code below: 

long_list_len = len(long_list)
#print(len(long_list))

print(long_list_len)

range_list_length = len(range_list)
print(range_list_length)

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Slicing Lists I

In Python, often we want to extract only a portion of a list. Dividing a list in such a manner is referred to as slicing.

Lets assume we have a list of letters:

letters = ["a", "b", "c", "d", "e", "f", "g"]
Suppose we want to select from "b" through "f".

We can do this using the following syntax: letters[start:end], where:

start is the index of the first element that we want to include in our selection. In this case, we want to start at "b", which has index 1.
end is the index of one more than the last index that we want to include. The last element we want is "f", which has index 5, so end needs to be 6.
sliced_list = letters[1:6]
print(sliced_list)
Would output:

["b", "c", "d", "e", "f"]
Notice that the element at index 6 (which is "g") is not included in our selection.

Instructions
1.
Use print() to examine the variable beginning.

Before hitting Run think about what elements beginning will contain?

2.
Modify beginning, so that it selects the first 2 elements of suitcase.


Stuck? Get a hint
3.
Create a new list called middle that contains the middle two items ( ["pants", "pants"] ) from suitcase.

Print middle to see the slice!

Slicing Lists I
In Python, often we want to extract only a portion of a list. Dividing a list in such a manner is referred to as slicing.

Lets assume we have a list of letters:

letters = ["a", "b", "c", "d", "e", "f", "g"]
Suppose we want to select from "b" through "f".

We can do this using the following syntax: letters[start:end], where:

start is the index of the first element that we want to include in our selection. In this case, we want to start at "b", which has index 1.
end is the index of one more than the last index that we want to include. The last element we want is "f", which has index 5, so end needs to be 6.
sliced_list = letters[1:6]
print(sliced_list)
Would output:

["b", "c", "d", "e", "f"]
Notice that the element at index 6 (which is "g") is not included in our selection.

Instructions
1.
Use print() to examine the variable beginning.

Before hitting Run think about what elements beginning will contain?

Checkpoint 2 Passed
2.
Modify beginning, so that it selects the first 2 elements of suitcase.

Checkpoint 3 Passed

Stuck? Get a hint
3.
Create a new list called middle that contains the middle two items ( ["pants", "pants"] ) from suitcase.

Print middle to see the slice!

suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

beginning = suitcase[0:2]

# Your code below: 

print(beginning)

middle = suitcase[2:4]
print(middle)

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Slicing Lists II

Slicing syntax in Python is very flexible. Let’s look at a few more problems we can tackle with slicing.

Take the list fruits as our example:

fruits = ["apple", "cherry", "pineapple", "orange", "mango"]
If we want to select the first n elements of a list, we could use the following code:

fruits[:n]
For our fruits list, suppose we wanted to slice the first three elements.

The following code would start slicing from index 0 and up to index 3. Note that the fruit at index 3 (orange) is not included in the results.

print(fruits[:3])
Would output:

['apple', 'cherry', 'pineapple']
We can do something similar when we want to slice the last n elements in a list:

fruits[-n:]
For our fruits list, suppose we wanted to slice the last two elements.

This code slices from the element at index -2 up through the last index.

print(fruits[-2:])
Would output:

['orange', 'mango']
Negative indices can also accomplish taking all but n last elements of a list.

fruits[:-n]
For our fruits example, suppose we wanted to slice all but the last element from the list.

This example starts counting from the 0 index up to the element at index -1.

print(fruits[:-1])
Would output:

['apple', 'cherry', 'pineapple', 'orange']
Let’s practice some of these extra slicing techniques!

Instructions
1.
Create a new list called last_two_elements containing the final two elements of suitcase.

Print last_two_elements to see your result.


Stuck? Get a hint
2.
Create a new list called slice_off_last_three containing all but the last three elements.

Print slice_off_last_three to see your result.

suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

# Your code below: 
last_two_elements = suitcase[-2:]
print(last_two_elements)

slice_off_last_three = suitcase[:-3]
print(slice_off_last_three)

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Counting in a List

In Python, it is common to want to count occurrences of an item in a list.

Suppose we have a list called letters that represents the letters in the word “Mississippi”:

letters = ["m", "i", "s", "s", "i", "s", "s", "i", "p", "p", "i"]
If we want to know how many times i appears in this word, we can use the list method called .count():

num_i = letters.count("i")
print(num_i)
Would output:

4
Notice that since .count() returns a value, we can assign it to a variable to use it.

We can even use .count() to count element appearances in a two-dimensional list.

Let’s use the list number_collection as an example:

number_collection = [[100, 200], [100, 200], [475, 29], [34, 34]]
If we wanted to know how often the sublist [100, 200] appears:

num_pairs = number_collection.count([100, 200])
print(num_pairs)
Would output:

2
Let’s count some list items using the .count() method!

Instructions
1.
Mrs. Wilson’s class is voting for class president. She has saved each student’s vote into the list votes.

Use .count() to determine how many students voted for "Jake" and save the value to a variable called jake_votes.


Stuck? Get a hint
2.
Use print() to examine jake_votes.

votes = ["Jake", "Jake", "Laurie", "Laurie", "Laurie", "Jake", "Jake", "Jake", "Laurie", "Cassie", "Cassie", "Jake", "Jake", "Cassie", "Laurie", "Cassie", "Jake", "Jake", "Cassie", "Laurie"]

# Your code below: 
jake_votes = votes.count("Jake")
print(jake_votes)

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Sorting Lists I

Often, we will want to sort a list in either numerical (1, 2, 3, …) or alphabetical (a, b, c, …) order.

We can sort a list using the method .sort().

Suppose that we have a list of names:

names = ["Xander", "Buffy", "Angel", "Willow", "Giles"]
Let’s see what happens when we apply .sort():

names.sort()
print(names)
Would output:

['Angel', 'Buffy', 'Giles', 'Willow', 'Xander']
As we can see, the .sort() method sorted our list of names in alphabetical order.

.sort() also provides us the option to go in reverse. Instead of sorting in ascending order like we just saw, we can do so in descending order.

names.sort(reverse=True)
print(names)
Would output:

['Xander', 'Willow', 'Giles', 'Buffy', 'Angel']
Note: The .sort() method does not return any value and thus does not need to be assigned to a variable since it modifies the list directly. If we do assign the result of the method, it would assign the value of None to the variable.

Let’s experiment sorting various lists!

Instructions
1.
Use .sort() to sort addresses.


Stuck? Get a hint
2.
Use print() to see how addresses changed.

3.
Remove the # and whitespace in front of the line sort(names). Edit this line so that it runs without producing a NameError.


Stuck? Get a hint
4.
Use print to examine sorted_cities. Why is it not the sorted version of cities?


Stuck? Get a hint
5.
Edit the .sort() call on cities such that it sorts the cities in reverse order (descending).

Print cities to see the result.

Sorting Lists I
Often, we will want to sort a list in either numerical (1, 2, 3, …) or alphabetical (a, b, c, …) order.

We can sort a list using the method .sort().

Suppose that we have a list of names:

names = ["Xander", "Buffy", "Angel", "Willow", "Giles"]
Let’s see what happens when we apply .sort():

names.sort()
print(names)
Would output:

['Angel', 'Buffy', 'Giles', 'Willow', 'Xander']
As we can see, the .sort() method sorted our list of names in alphabetical order.

.sort() also provides us the option to go in reverse. Instead of sorting in ascending order like we just saw, we can do so in descending order.

names.sort(reverse=True)
print(names)
Would output:

['Xander', 'Willow', 'Giles', 'Buffy', 'Angel']
Note: The .sort() method does not return any value and thus does not need to be assigned to a variable since it modifies the list directly. If we do assign the result of the method, it would assign the value of None to the variable.

Let’s experiment sorting various lists!

Instructions
1.
Use .sort() to sort addresses.

Checkpoint 2 Passed

Stuck? Get a hint
2.
Use print() to see how addresses changed.

Checkpoint 3 Passed
3.
Remove the # and whitespace in front of the line sort(names). Edit this line so that it runs without producing a NameError.

Checkpoint 4 Passed

Stuck? Get a hint
4.
Use print to examine sorted_cities. Why is it not the sorted version of cities?

Checkpoint 5 Passed

Stuck? Get a hint
5.
Edit the .sort() call on cities such that it sorts the cities in reverse order (descending).

Print cities to see the result.

Checkpoint 6 Passed

Hint
To reverse a list using .sort(), add an optional input keyword argument and assign it the value of True.

list.sort(reverse=True)

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Sorting Lists II

A second way of sorting a list in Python is to use the built-in function sorted().

The sorted() function is different from the .sort() method in two ways:

It comes before a list, instead of after as all built-in functions do.
It generates a new list rather than modifying the one that already exists.
Let’s return to our list of names:

names = ["Xander", "Buffy", "Angel", "Willow", "Giles"]
Using sorted(), we can create a new list, called sorted_names:

sorted_names = sorted(names)
print(sorted_names)
This yields the list sorted alphabetically:

['Angel', 'Buffy', 'Giles', 'Willow', 'Xander']
Note that using sorted did not change names:

print(names)
Would output:

['Xander', 'Buffy', 'Angel', 'Willow', 'Giles']
Instructions
1.
Use sorted() to order games and create a new list called games_sorted.


Stuck? Get a hint
2.
Print both games and games_sorted. How are they different?

games = ["Portal", "Minecraft", "Pacman", "Tetris", "The Sims", "Pokemon"]

# Your code below:
games_sorted = sorted(games)

print(games)
print(games_sorted)

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Review

In this lesson, we learned how to:

Add elements to a list by index using the .insert() method.
Remove elements from a list by index using the .pop() method.
Generate a list using the range() function.
Get the length of a list using the len() function.
Select portions of a list using slicing syntax.
Count the number of times that an element appears in a list using the .count() method.
Sort a list of items using either the .sort() method or sorted() function.
As you go through the exercises, feel free to use print() to see changes when not explicitly asked to do so.

Instructions
1.
Our friend Jiho has been so successful in both the flower and grocery business that she has decided to open a furniture store.

Jiho has compiled a list of inventory items into a list called inventory and wants to know a few facts about it.

First, how many items are in the warehouse?

Save the answer to a variable called inventory_len.


Stuck? Get a hint
2.
Select the first element in inventory. Save it to a variable called first.


Stuck? Get a hint
3.
Select the last element from inventory. Save it to a variable called last.


Stuck? Get a hint
4.
Select items from the inventory starting at index 2 and up to, but not including, index 6.

Save your answer to a variable called inventory_2_6.


Stuck? Get a hint
5.
Select the first 3 items of inventory. Save it to a variable called first_3.


Stuck? Get a hint
6.
How many 'twin bed's are in inventory? Save your answer to a variable called twin_beds.


Stuck? Get a hint
7.
Remove the 5th element in the inventory. Save the value to a variable called removed_item.


Stuck? Get a hint
8.
There was a new item added to our inventory called "19th Century Bed Frame".

Use the .insert() method to place the new item as the 11th element in our inventory.


Stuck? Get a hint
9.
Sort inventory using the .sort() method or the sorted() function.

Remember, the sorted() function doesn’t change the original list — it creates a new list with the elements properly sorted. If you use sorted() you’ll have to set inventory equal to the value returned by sorted().

Print inventory to see the result.

inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

inventory_len = len(inventory)

first = inventory[0]

last = inventory[-1]

inventory_2_6 = inventory[2:6]

first_3 = inventory[:3]

twin_beds = inventory.count('twin bed')

removed_item = inventory.pop(4)

inventory.insert(10, "19th Century Bed Frame")

inventory.sort()
print(inventory)

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Len's Slice
You work at Len’s Slice, a new pizza joint in the neighborhood. You are going to use your knowledge of Python lists to organize some of your sales data.

Tasks
0/14 Complete
Mark the tasks as complete by checking them off
Make Some Pizzas
1.
To keep track of the kinds of pizzas you sell, create a list called toppings that holds the following:

"pepperoni"
"pineapple"
"cheese"
"sausage"
"olives"
"anchovies"
"mushrooms"

Stuck? Get a hint
2.
To keep track of how much each kind of pizza slice costs, create a list called prices that holds the following integer values:

2
6
1
3
2
7
2

Stuck? Get a hint
3.
Your boss wants you to do some research on $2 slices.

Count the number of occurrences of 2 in the prices list, and store the result in a variable called num_two_dollar_slices. Print it out.


Stuck? Get a hint
4.
Find the length of the toppings list and store it in a variable called num_pizzas.


Stuck? Get a hint
5.
Print the string We sell [num_pizzas] different kinds of pizza!, where [num_pizzas] represents the value of our variable num_pizzas.


Stuck? Get a hint
6.
Convert our toppings and prices lists into a two-dimensional list called pizza_and_prices that has the following associated values.

Each sublist in pizza_and_prices should have one pizza topping and an associated price.

Price	Topping
2	"pepperoni"
6	"pineapple"
1	"cheese"
3	"sausage"
2	"olives"
7	"anchovies"
2	"mushrooms"

For this project make sure the prices come before the topping name like so:

[price, topping_name]

Stuck? Get a hint
7.
Print pizza_and_prices.

Does it look the way you expect?


Stuck? Get a hint
Sorting and Slicing Pizzas
8.
Sort pizza_and_prices so that the pizzas are in the order of increasing price (ascending).


Stuck? Get a hint
9.
Store the first element of pizza_and_prices in a variable called cheapest_pizza.


Stuck? Get a hint
10.
A man walks into the pizza store and shouts “I will have your MOST EXPENSIVE pizza!”

Get the last item of the pizza_and_prices list and store it in a variable called priciest_pizza.


Stuck? Get a hint
11.
It looks like the most expensive pizza from the previous step was our very last "anchovies" slice. Remove it from our pizza_and_prices list since the man bought the last slice.


Stuck? Get a hint
12.
Since there is no longer an "anchovies" pizza, you want to add a new topping called "peppers" to keep your customers excited about new toppings. Here is what your new topping looks like:

[2.5, "peppers"]
Add the new peppers pizza topping to our list pizza_and_prices.

Note: Make sure to position it relative to the rest of the sorted data in pizza_and_prices, otherwise our data will not be correctly sorted anymore!


Stuck? Get a hint
13.
Three mice walk into the store. They don’t have much money (they’re mice), but they do each want different pizzas.

Slice the pizza_and_prices list and store the 3 lowest cost pizzas in a list called three_cheapest.


Stuck? Get a hint
14.
Great job! The mice are very pleased and will be leaving you a 5-star review.

Print the three_cheapest list.

# Your code below:

toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

prices = [2, 6, 1, 3, 2, 7, 2]

#occurrences of 2 in the prices
num_two_dollar_slices = prices.count(2)

#length of the toppings list
num_pizzas = len(toppings)

print("We sell " + str(num_pizzas) + " different kinds of pizzas!")

pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]

#print(pizza_and_prices)

pizza_and_prices.sort()
#print(pizza_and_prices)

cheapest_pizza = pizza_and_prices[1]
#print(cheapest_pizza)

priciest_pizza = pizza_and_prices[-1]
#print(priciest_pizza)

pizza_and_prices.pop()
#print(pizza_and_prices)

pizza_and_prices.insert(4, [2.5, "sausage"])
print(pizza_and_prices)

three_cheapest = pizza_and_prices[:3]
print(three_cheapest)

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Combining Lists: The Zip Function
Learn about a popular Python built-in function called zip().

In Python, we have an assortment of built-in functions that allow us to build our programs faster and cleaner. One of those functions is zip().

The zip() function allows us to quickly combine associated data-sets without needing to rely on multi-dimensional lists. While zip() can work with many different scenarios, we are going to explore only a single one in this article.

Let’s use a list of student names and associated heights as our example data set:

Jenny is 61 inches tall
Alexus is 70 inches tall
Sam is 67 inches tall
Grace is 64 inches tall
Suppose that we already had a list of names and a list of heights:

names = ["Jenny", "Alexus", "Sam", "Grace"]
heights = [61, 70, 67, 65]
If we wanted to create a nested list that paired each name with a height, we could use the built-in function zip().

The zip() function takes two (or more) lists as inputs and returns an object that contains a list of pairs. Each pair contains one element from each of the inputs. This is how we would do it for our names and heights lists:

names_and_heights = zip(names, heights)
If we were to then examine this new variable names_and_heights, we would find it looks a bit strange:

print(names_and_heights)
Would output:

<zip object at 0x7f1631e86b48>
This zip object contains the location of this variable in our computer’s memory. Don’t worry though, it is fairly simple to convert this object into a useable list by using the built-in function list():

converted_list = list(names_and_heights)
print(converted_list)
Outputs:

[('Jenny', 61), ('Alexus', 70), ('Sam', 67), ('Grace', 65)]
Notice two things:

Our data set has been converted from a zip memory object to an actual list (denoted by [ ])

Our inner lists don’t use square brackets [ ] around the values. This is because they have been converted into tuples (an immutable type of list).

Let’s practice using zip()!

Use zip() to create a new variable called names_and_dogs_names that combines owners and dogs_names lists into a zip object.

Then, create a new variable named list_of_names_and_dogs_names by calling the list() function on names_and_dogs_names.

Print list_of_names_and_dogs_names.

owners = ["Jenny", "Alexus", "Sam", "Grace"]
dogs_names = ["Elphonse", "Dr. Doggy DDS", "Carter", "Ralph"]

names_and_dogs_names = zip(owners, dogs_names)

list_of_names_and_dogs_names = list(names_and_dogs_names)

print(list_of_names_and_dogs_names)
