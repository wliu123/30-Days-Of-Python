# Exercises: Level 1
# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
# Enter your age: 30
# You are old enough to learn to drive.
# Output:
# Enter your age: 15
# You need 3 more years to learn to drive.
# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
# Enter your age: 30
# You are 5 years older than me.

from urllib import request


your_age = int(input('Enter your age: '))
if your_age >= 18:
    print('You are old enough to drive')
else: 
    print('Wait for ' + str((18 - your_age)) + ' years before driving')

my_age = 25

if your_age > my_age:
    if (your_age - my_age) > 1:
        print('You are ' + str((your_age - my_age)) + ' years older than me')
    else:
        print('You are 1 year older than me')

elif your_age < my_age:
    if (my_age - your_age) > 1:
        print('You are ' + str((my_age - your_age)) + ' years younger than me')
    else:
        print('You are 1 year younger than me')
else:
    print("We are the same age!")

# Exercises: Level 2
# Write a code which gives grade to students according to theirs scores:

# 90-100, A
# 70-89, B
# 60-69, C
# 50-59, D
# 0-49, F

# The following list contains some fruits:

# fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That 
# fruit already exist in the list')
grade = int(input('What grade did you receive?'))
if grade >= 0 and grade <= 49:
    print('F')
elif grade >= 50 and grade <= 59:
    print('D')
elif grade >= 60 and grade <= 69:
    print('C')
elif grade >= 70 and grade <= 89:
    print('B')
else: 
    print('A')

fruits = ['banana', 'orange', 'mango', 'lemon']
request_fruit = input('What fruit do you want?')
if not request_fruit in fruits:
    fruits.append(request_fruit)
else:
    print('That fruit already exists in the list')

print(fruits)