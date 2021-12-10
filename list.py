list_of_random_things = [1, 3.4, 'a string', True]
print(list_of_random_things[1:2])
print(list_of_random_things[:2])
print(list_of_random_things[1:])

# this in or not in
words='this is a string'
'this' in words

# List Mutability
my_lst = [1, 2, 3, 4, 5]
my_lst[0] = 'one'
print(my_lst)

# string immutability
greeting = "Hello there"
# greeting[0] = 'M'



# use list indexing to determine the number of days in month
month = 8
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
num_days=days_in_month[7]
print(num_days)


# Select the three most recent dates from this list using list slicing notation. Hint: negative indexes work in slices!
eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']
                 
                 
# TODO: Modify this line so it prints the last three elements of the list


print(eclipse_dates[7:])


# join methods
new_str = "-".join(["fore", "aft", "starboard", "port"])
print(new_str)

# sorting a list
names = ["Carol", "Albert", "Ben", "Donna"]
names.append("Eugenia")
print(sorted(names))