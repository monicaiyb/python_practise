# Unpack a tuple in a for loop
letters = ['a', 'b', 'c']
nums = [1, 2, 3]

for letter, num in zip(letters, nums):
    print("{}: {}".format(letter, num))

# Unzip a list into tuples using zip and an *
some_list = [('a', 1), ('b', 2), ('c', 3)]
letter1, nums = zip(*some_list)
print(letter1)
print(nums)


# Enumerate creates number indices for a list and the values of a list
letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letters):
    print(i, letter)

# Create a for loop that creates a string spcificying a label and coordinates of each point
x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
# write your for loop here
for point in zip(labels, x_coord,y_coord,z_coord):
    
    points.append("{}: {},{},{}".format(*point))

    print(points)

for point in points:
    print(point)

# Create a dictionary with names as keys and cast_heights as values
cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = []

for name, height in zip(cast_names, cast_heights):
    print("{}: {}".format(name, height))
    cast.append("{}: {}".format(name, height))

print(cast)


# Unzip the cast tuple into two names and heights tuples.
cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))

# define names and heights here

names, heights = zip(*cast)
print(names)
print(heights)


# Use zip to transpose data from a 4-by-3 matrix to a 3-by-4 matrix. There's actually 
# a cool trick for this! Feel free to look at the solutions if you can't figure it out.
data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

data_transpose = tuple(zip(*data))
print(data_transpose)

# 
for i, character in enumerate(cast):
    cast[i] = character + " " + str(heights[i])

print(cast)