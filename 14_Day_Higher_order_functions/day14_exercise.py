countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
import functools
# Exercises: Level 1
# Explain the difference between map, filter, and reduce.
# map iterates through a list and changes the values within the list. Filter takes in a boolean fxn and iterates through list to see when true. Reduce iterates through list and sums everything.
# Explain the difference between higher order function, closure and decorator.
# higher order have functions within them giving inner functions access to any variables called in the higher function. decorator refers back to the function that is @
# Define a call function before map, filter or reduce, see examples.
# Use for loop to print each country in the countries list.
# Use for to print each name in the names list.
# Use for to print each number in the numbers list.

for country in countries:
    print(country)
for name in names:
    print(name)
for number in numbers:
    print(number)

# Exercises: Level 2
# Use map to create a new list by changing each country to uppercase in the countries list
# Use map to create a new list by changing each number to its square in the numbers list
# Use map to change each name to uppercase in the names list
# Use filter to filter out countries containing 'land'.
# Use filter to filter out countries having exactly six characters.
# Use filter to filter out countries containing six letters and more in the country list.
# Use filter to filter out countries starting with an 'E'
# Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
# Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
# Use reduce to sum all the numbers in the numbers list.
# Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries

countries_upper = list(map(lambda x:x.upper(), countries))
numbers_square= list(map(lambda x:x**2, numbers))
names_upper = list(map(lambda x:x.upper(), names))

def filter_land(country):
    if 'land' in country:
        return True
    return False
country_filter = list(filter(filter_land, countries))

def filter_six(country):
    if len(country) == 6:
        return True
    return False
country_six = list(filter(filter_six, countries))

def filter_six_or_more(country):
    if len(country) >= 6:
        return True
    return False
country_six_or_more = list(filter(filter_six_or_more, countries))

def starts_with_e(country):
    if country.startswith('E'):
        return True
    return False
country_starts_with_e = list(filter(starts_with_e, countries))

def get_string_lists(lists):
    return str(lists)
convert_to_string = list(map(get_string_lists, numbers))

def add_two_nums(x, y):
    return int(x) + int(y)
sum_list = functools.reduce(add_two_nums, numbers)

def concat_sent(country1, country2):
    return str(country1) + ", " + str(country2) 
sentence = functools.reduce(concat_sent, countries)
print(sentence + " are North European countries")
