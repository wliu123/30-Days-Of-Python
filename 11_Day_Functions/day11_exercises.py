# Exercises: Level 1
# Declare a function add_two_numbers. It takes two parameters and it returns a sum.
# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
# print(reverse_list([1, 2, 3, 4, 5]))
# # [5, 4, 3, 2, 1]
# print(reverse_list1(["A", "B", "C"]))
# # ["C", "B", "A"]
# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
# print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
# numbers = [2, 3, 7, 9];
# print(add_item(numbers, 5))      [2, 3, 7, 9, 5]
# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
# print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
# numbers = [2, 3, 7, 9];
# print(remove_item(numbers, 3))  # [2, 7, 9]
# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
# print(sum_of_numbers(5))  # 15
# print(sum_all_numbers(10)) # 55
# print(sum_all_numbers(100)) # 5050
# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
import math
def add_two_numbers(num1, num2):
    return num1 + num2
def area_of_circle(radius):
    pi = 3.14
    area = pi * radius ** 2
    return area
def add_all_nums(*args):
    sum = 0
    for each in args:
        if type(each) == int:
            sum += each
        else:
            print("sum only integers")
    return sum
def convert_temp(degrees_celsius):
    fahreinheit = (degrees_celsius * (9/5)) + 32
    return fahreinheit
def check_season(month):
    spring = ['March', 'April', 'May']
    summer = ['June', 'July', 'August']
    fall = ['September', 'October', 'November']
    winter = ['December', 'January', 'February']
    if month in spring:
        return 'Spring'
    elif month in summer:
        return 'Summer'
    elif month in fall:
        return 'Fall'
    elif month in winter:
        return 'Winter'
    else:
        return 'Not in a season'
def print_list(list):
    for each in list:
        print(each)
def reverse_list(list):
    new_array = []
    for i in reversed(range(len(list))):
        new_array.append(list[i])
    return new_array
def capitalize_list_items(list):
    new_array = []
    for each in list:
        new_array.append(each.capitalize())
    return new_array
def add_item(list, item):
    return list.append(item)
def remove_item(list, item):
    return list.remove(item)
def sum_of_numbers(number):
    sum = 0
    for i in range(number+1):
        sum += i
    return sum
def sum_of_odds(number):
    sum = 0
    for i in range(number+1):
        if i % 2 != 0:
            sum += i
    return sum
def sum_of_evens(number):
    sum = 0
    for i in range(number+1):
        if i % 2 == 0:
            sum += i
    return sum

# Exercises: Level 2
# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
#     print(evens_and_odds(100))
#     # The number of odds are 50.
#     # The number of evens are 51.
# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
# Call your function is_empty, it takes a parameter and it checks if it is empty or not
# Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).

def evens_and_odds(int):
    even_count = 0
    odd_count = 0
    for i in range(int + 1):
        if i % 2 == 0:
            even_count += 1
        else: 
            odd_count += 1
    print('The number of evens are ' + str(even_count))
    print('The number of odds are ' + str(odd_count))

def factorial(num):
    sum = 1
    for i in range(1, num + 1):
        sum *= i
    return sum

def factorial_rec(num):
    if num == 1:
        return num
    else: 
        return num * factorial_rec(num - 1)

def is_empty(param):
    return len(param) == 0

def calculate_mean(list):
    sum = 0
    for each in list:
        sum += each
    return sum/len(list)

def calculate_median(list):
    mid = len(list) // 2
    list.sort()
    for i in range(len(list)):
        if len(list) % 2 != 0:
            return list[mid]
        else: 
            return (list[mid] + list[mid-1])/2

def calculate_mode(list):
   return max(set(list), key = list.count)

def calculate_range(list):
    return list[len(list) - 1] - list[0]

def calculate_variance(list):
    mean = calculate_mean(list)
    sum = 0
    for each in list:
        sum += (each - mean)**2
    return sum/len(list)

def calculate_std(list):
    var = calculate_variance(list)
    return math.sqrt(var)

# Exercises: Level 3
# Write a function called is_prime, which checks if a number is prime.
# Write a functions which checks if all items are unique in the list.
# Write a function which checks if all the items of the list are of the same data type.
# Write a function which check if provided variable is a valid python variable

def is_prime(num):
    if num > 1:
        for i in range(2, int(num/2) + 1):
            if (num % 2) == 0:
                print(str(num) + ' is not a prime number')
                break
            else:
                print(str(num) + ' is a prime number')
    else: 
        print(str(num) + ' is a prime number')

def is_unique(list):
    list_set = set(list)
    return len(list_set) == len(list)

def same_type(list):
    return all(isinstance(each, type(list[0])) for each in list[1:])

def is_valid(variable):
    return variable.isidentifier()
print(is_valid('1hello'))