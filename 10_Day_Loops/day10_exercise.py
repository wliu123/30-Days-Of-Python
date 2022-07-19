# Exercises: Level 1
# Iterate 0 to 10 using for loop, do the same using while loop.

# Iterate 10 to 0 using for loop, do the same using while loop.

# Write a loop that makes seven calls to print(), so we get on the output the following triangle:

#   #
#   ##
#   ###
#   ####
#   #####
#   ######
#   #######
# Use nested loops to create the following:

# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# Print the following pattern:

# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100
# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

# Use for loop to iterate from 0 to 100 and print only even numbers

# Use for loop to iterate from 0 to 100 and print only odd numbers

for i in range(10):
    print(i)

num = 0
while num < 10:
   print(num)
   num += 1

for j in reversed(range(10)):
    print(j)

nums = 10
while nums >= 0:
    print(nums)
    nums -= 1


for i in range(8):
    for j in range(i+1):
       print('#', end=" ")
    print('\n')
