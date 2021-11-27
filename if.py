# number to find the factorial of
number = 6   

# start with our product equal to one
product = 1

# track the current number being multiplied
current = 1

# write your while loop here
while (current <= number):
    # multiply the product so far by the current number
    
    product *= current
    
    # increment current with each iteration until it reaches number     
    current += 1
   
# print the factorial of number
print(product)


# number we'll find the factorial of
number = 6
# start with our product equal to one
product = 1

# calculate factorial of number with a for loop
for num in range(2, number + 1):
    product *= num

# print the factorial of number
print(product)



start_num =1 #provide some start number
end_num = 80#provide some end number that you stop when you hit
count_by =2 #provide some number to count by 

# write a while loop that uses break_num as the ongoing number to 
#   check against end_num
break_num = start_num
while break_num < end_num:
  print(start_num)
  # if start_num == break_num:
  #   break
  break_num += count_by

print(break_num)

start_num =20 #provide some start number
end_num = 100#provide some end number that you stop when you hit
count_by = 2#provide some number to count by 

# write a condition to check that end_num is larger than start_num before looping
# write a while loop that uses break_num as the ongoing number to 
#   check against end_num

if start_num > end_num:
    result = "Oops! Looks like your start value is greater than the end value. Please try again."

else:
    break_num = start_num
    while break_num < end_num:
        break_num += count_by

    result = break_num

print(result)
    
