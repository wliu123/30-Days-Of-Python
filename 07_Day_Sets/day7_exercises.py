# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Exercises: Level 1
# Find the length of the set it_companies
# Add 'Twitter' to it_companies
# Insert multiple IT companies at once to the set it_companies
# Remove one of the companies from the set it_companies
# What is the difference between remove and discard

len(it_companies)
it_companies.add('Twitter')
it_companies.update(['Nvidia', 'Autodesk', 'Handshake'])
it_companies.remove('Facebook')
#remove will throw an error if the item doesn't exist within the set. discard will not.

# Exercises: Level 2
# Join A and B
# Find A intersection B
# Is A subset of B
# Are A and B disjoint sets
# Join A with B and B with A
# What is the symmetric difference between A and B
# Delete the sets completely

A.union(B)
A.intersection(B)
A.issubset(B)
A.union(B)
B.union(A)
A.symmetric_difference(B)
del A
del B

#Exercises: Level 3
# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
# Explain the difference between the following data types: string, list, tuple and set
# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
new_set = set(age)
print(len(age))
print(len(new_set))
# string is made up of characters, list is an ordered colelction of elements with index capabilities and is mutable
# tuple is an immutable, ordered data structure but can have tuples joined up and sets can have elements added and removed but no indexing
# sets also unordered and have unique values only
sentence = 'I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence?'
list_sent = sentence.split(' ')
set_sent = set(list_sent)
len(set_sent)
print(len(set_sent))
