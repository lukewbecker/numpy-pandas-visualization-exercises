# Numpy Exercises - .py version


#!/usr/bin/env python
# coding: utf-8

# ### NumPy Exercises
# - Learning numpy array structures
# - Comprehending difference between numpy arrays and python lists
# - Practice iterating through numpy arrays


import numpy as np



# Use the following code for the questions below:

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])



# How many negative numbers are there?
# (To prove to myself I know how to use .shape in this context)
a[a < 0].shape

print(f"There are {a[a < 0].shape} negative numbers in this array")




# Using len:

len(a[a < 0])




# How many positive numbers are there?
# 0 doesn't count, as it is this origin integer.

a[a > 0].shape



# How many even positive numbers are there?

a[(a > 0) & (a % 2 == 0)].shape



# If you were to add 3 to each data point, how many positive numbers would there be?

a[(a + 3) > 0].shape



# If you squared each number, what would the new mean and standard deviation be?

(a ** 2).std()
(a ** 2).mean()

# Printing results for output to screen:
print(f"The new std. dev would be: {(a ** 2).std()}")
print(f"The new mean would be: {(a ** 2).mean()}")




# A common statistical operation on a dataset is centering. This means to adjust 
# the data such that the center of the data is at 0. This is done by subtracting the mean 
# from each data point. Center the data set.

a - a.mean()




# Using list comphrension: (Again, I'm doing this just so I can wrap my head around what numpy is doing.)

array_mean = a.mean()
array_mean

centered_array = [x - array_mean for x in a]
centered_array



# #### Calculate the z-score for each data point. Recall that the z-score is given by:
# $Z = (x - u) / std$
# 


z_score = (a - a.mean())/a.std()
z_score


# ### Copy the setup and exercise directions from More Numpy Practice into your numpy_exercises.py and add your solutions.



## Setup 1
a2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# #### Use python's built in functionality/operators to determine the following:



# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list

# I think these first four are pretty straightforward unless I'm missing something in the instructions.

sum_of_a = sum(a2)
sum_of_a




# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list

min_of_a = min(a2)
min_of_a



# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list

max_of_a = max(a2)
max_of_a




# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list

mean_of_a = sum(a2) / len(a2)
mean_of_a




# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together

# I decided to use a function since that's what made the most sense to me in this moment. 
# I'm sure there is a way to use list comprehension, but this is what clicked for me in the moment. 
# And I figured that was ok to do since functions are a based part of Python, unless I mis-read the instructions

def multiply_list(value):
    result = 1
    for x in value:
        result = result * x
    return result


product_of_a = multiply_list(a2)
product_of_a


# Exercise 6 - Make a variable named squares_of_a. It should hold each number 
# in a squared like [1, 4, 9, 16, 25...]

# Still trying to use list comprehensions wherever I can, since it look a lot of work for those to finally click in my mind.
# Don't want to lose that in my short-term memory!

# I'm iterating through the a2 list, and squaring each element of that list, and then returning the results in a new list: squares_of_a

squares_of_a = ([i ** 2 for i in a2])
squares_of_a




# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers

# Finding the numbers in the list that are not divisible by 0, and creating a new list from those odd numbers.

odds_in_a = [x for x in a2 if x % 2 == 1]
odds_in_a




# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.

# Finding the numbers in the list that are divisible by 0, and creating a new list from those even numbers.

evens_in_a = [x for x in a2 if x % 2 == 0]
evens_in_a




## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.

b = [
    [3, 4, 5],
    [6, 7, 8]
    ]




# I figured out to not use list comprehensions in [] brackets, but I don't fully understand why I can't use the [].

# Tried using brackets and get an invalid syntax error...

# sum_of_b = sum[sum(x) for x in b]f
# sum_of_b

# Found this solution here:
# https://stackoverflow.com/questions/9497290/how-would-i-sum-a-multi-dimensional-array-in-the-most-succinct-python


# Find the sum of a 2d list

sum_of_b = sum(sum(x) for x in b)
sum_of_b



# Find the min of a 2d list

min_of_b = min(min(x) for x in b)
min_of_b




# Find the max of a 2d list

max_of_b = max(max(x) for x in b)
max_of_b




# Find the average of a 2d list.
# This one was a bit more tricky, as I was first trying len([len(x) for x in b]). But that's not the right answer, as I needed to sum the results of that first len(), which is 6.
# Then I could take the sum of all elements / the sum of all the lengths = average of b.

average_of_b = (sum(sum(x) for x in b)) / (sum(len(x) for x in b))
average_of_b




# Can't do this using the function I had before, as this is a 2 dimensional list.

# def multiply_list_b(value):
#     result = 1
#     for x in value:
#         result = result * x
#     return result


# product_of_b = multiply_list_b(b)
# product_of_b




# Refactorting b as a numpy array:

b = [
    [3, 4, 5],
    [6, 7, 8]
    ]


ba = np.array([[3, 4, 5],
                [6, 7, 8]])




npb = np.array(b)
npb




# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. 
# **Hint, you'll first need to make sure that the "b" variable is a numpy array**

# Original code:
sum_of_b = 0
for row in b:
    sum_of_b += sum(row)

# Using numpy's sum() function the code becomes:
ba.sum()




# Exercise 2 - refactor the following to use numpy. 

# This is using list comprehension:
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])

# Using numpy's min function:
ba.min()



# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.

# Python list comprehension:
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])

# Using numpy's max():
ba.max()




# Exercise 4 - refactor the following using numpy to find the mean of b

# Python list comprehension:
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))

# Using numpy's max():
ba.max()




# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number

# Using numpy:
ba.prod()




# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)
        
squares_of_b

# Using numpy:
np.square(ba)


# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)
            
# Using numpy:
odds_in_b = (ba[ba % 2 == 1])
print(odds_in_b)

# Link to article that I used for help:
# https://stackoverflow.com/questions/51617421/how-to-get-only-odd-numbers-in-array-and-square-them-using-numpy-for-python




# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)
            
# Using numpy:
evens_in_b = (ba[ba % 2 == 0])
print(evens_in_b)




# Exercise 9 - print out the shape of the array b.
print(np.shape(ba))

# Array has 2 dimensions, and each dimension (list) has 3 elements.



# Exercise 10 - transpose the array b.

np.transpose(ba)
# This is cool - so I can reorient the order of any 2d (or multidimensional) array. I can see that will be very useful and powerful going forward.



# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)

flatb = ba.flatten()
print(flatb)

# Got help from this article:
# https://www.kite.com/python/answers/how-to-convert-a-2d-numpy-array-to-a-1d-array-in-python



# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)

# Ok, so I'll actually use reshape on this one.

baarrsix = ba.reshape(6, 1)
print(baarrsix)



## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.

c = np.array(c)



# Exercise 1 - Find the min, max, sum, and product of c.

c.max()
c.min()
c.sum()
c.prod()



# Exercise 2 - Determine the standard deviation of c.

c.std()



# Exercise 3 - Determine the variance of c.

c.var()




print(np.shape(c))



# Exercise 5 - Transpose c and print out transposed result.

c.transpose()
print(np.shape(c))



# Exercise 6 - Get the dot product of the array c with c. 

np.dot(c, c)



# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261

c_times_c = np.sum(c * (np.transpose(c)))
c_times_c



# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.

c_prod_c = np.prod(c * (np.transpose(c)))
c_prod_c



## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

# Changing to numpy array:
dnp = np.array(d)
dnp



# Exercise 1 - Find the sine of all the numbers in d

np.sin(dnp)




# Exercise 2 - Find the cosine of all the numbers in d

np.cos(dnp)



# Exercise 3 - Find the tangent of all the numbers in d

np.tan(dnp)



# Exercise 4 - Find all the negative numbers in d

negative_in_d = (dnp[dnp < 0])
print(negative_in_d)



# Exercise 5 - Find all the positive numbers in d

positive_in_d = (dnp[dnp > 0])
print(positive_in_d)



# Exercise 6 - Return an array of only the unique numbers in d

dnp = np.array(d)
print(dnp)
# Printed out dnp array here so I could visually compare the results of the np.unique() function. Just for a "gut check".

np.unique(dnp)



# Exercise 7 - Determine how many unique numbers there are in d.

len(np.unique(dnp))



# Exercise 8 - Print out the shape of d.

np.shape(dnp)




# Exercise 9 - Transpose and then print out the shape of d.

print(np.transpose(dnp))

# For further personal comprehension of what transpose is doing, I'm going to use shape on this new array:
newshape_dnp = np.transpose(dnp)
print("     ")
print(np.shape(newshape_dnp))

# So the shape is the opposite, (6, 3), which is the opposite of (3, 6).




# Exercise 10 - Reshape d into an array of 9 x 2

np.reshape(dnp, (9, 2))