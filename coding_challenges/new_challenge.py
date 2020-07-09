# Add up and print the sum of the all of the minimum elements of each inner array:
# [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
# The expected output is given by:
# 4 + -1 + 9 + -56 + 201 + 18 = 175
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. 
# Run through the UPER problem solving framework while going through your thought process.

# store main array in a variable to iterate in a for loop
# for each element in the main array
# use the min python meth to find the smallest number
# add those smallest number to append them to another list 
# which would stored in a new variable
# then sum up all of those integers

array1 = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]

num = [min(x) for x in array1]
print(sum(num))
