#  Exercises: Day 8
# Create an empty dictionary called dog
# Add name, color, breed, legs, age to the dog dictionary
# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
# Get the length of the student dictionary
# Get the value of skills and check the data type, it should be a list
# Modify the skills values by adding one or two skills
# Get the dictionary keys as a list
# Get the dictionary values as a list
# Change the dictionary to a list of tuples using items() method
# Delete one of the items in the dictionary
# Delete one of the dictionaries

dog = {}
dog['name'] = 'bill'
dog['color'] = 'black'
dog['breed'] = 'corgi'
dog['legs'] = 4
dog['age'] = 3

student_dictionary = {
    'first_name':'John',
    'last_name':'Gold',
    'gender':'Male',
    'age':20,
    'marital_status':'single',
    'skills':['rowing', 'sleeping'],
    'country':'USA',
    'city':'New York',
    'address':'123 Broadway'
}
len(student_dictionary)
type(student_dictionary['skills'])
student_dictionary['skills'].extend(['talking', 'eating'])
student_dictionary.keys()
student_dictionary.values()
student_dictionary.items()
student_dictionary.pop('country')
del dog