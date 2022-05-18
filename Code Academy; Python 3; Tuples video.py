Code Academy; Python 3; Tuples video

tuple is a data structure in pyhon tha allows us to store multiple pieces of data inside of it. Except it is immutable. once data has been entered it cant be changed.

my_info = ('Mike', 24, 'Programmer')

#print?
my_info

my_info[0]
'Mike'

my_info[1]
24

my_info[-1]
'programmer'


my_info[0] = 'Michael'
#this will throw up a TypeError 'tuple' object does not support item assignment

#unpacking tuple
name, age, occupation = my_info

#print 'name' variable will print first item in tuple it is assigned to.
name
'Mike'

age
'24'

occupation
'Programmer'

#as long as you have a number of variables on the left equal to the number of elements in the tuple then all of the elements will be stored inside the variable respectively.


#SPECIAL CASE
#One Element Tuple

one_element_tuple = (4)

#print
one_element_tuple

#returns
4

#REASON: it didn't actually create a tuple, because in python you can use parathesis to surround expressions inside of them. you can use parathesis to express order of operations.

(1+3) * 8

#will return

32

#to create a tuple you must put a comma ',' after the first element. This is called a trailing comma.
one_element_tuple = (4,)

#print
one_element_tuple

#returns which is now a tuple
(4,)
