#Exercises: Level 1
# Create an empty tuple
# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
# Join brothers and sisters tuples and assign it to siblings
# How many siblings do you have?
# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
tuple()
brothers = ('John', 'Bill')
sisters = ('Mary', 'Lisa')
siblings = brothers + sisters
len(siblings)
list_siblings = list(siblings)
list_siblings.extend(['Father', 'Mother'])
print(list_siblings)
family_members = tuple(list_siblings)

#Exercises: Level 2
# Unpack siblings and parents from family_members
# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
# Change the about food_stuff_tp tuple to a food_stuff_lt list
# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
# Slice out the first three items and the last three items from food_staff_lt list
# Delete the food_staff_tp tuple completely
# Check if an item exists in tuple:
# Check if 'Estonia' is a nordic country

# Check if 'Iceland' is a nordic country

# nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
del family_members
fruits = ('apple', 'orange', 'banana')
vegetables = ('celery', 'brocolli', 'lettuce')
animal_products = ('milk', 'chicken', 'eggs')
food_stuff_tp = fruits + vegetables + animal_products
food_stuff_lt = list(food_stuff_tp)
middle = len(food_stuff_lt)//2
food_stuff_lt[middle]
food_stuff_lt[0:3]
food_stuff_lt[-3:]
del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
'Estonia' in nordic_countries
'Iceland' in nordic_countries

