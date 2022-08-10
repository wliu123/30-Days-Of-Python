# Exercises: Level 1
# Write a function which count number of lines and number of words in a text. All the files are in the data the folder: a) Read obama_speech.txt file and count number of lines and words b) Read michelle_obama_speech.txt file and count number of lines and words c) Read donald_speech.txt file and count number of lines and words d) Read melina_trump_speech.txt file and count number of lines and words

# Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages
#Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries
import json
from unittest import skip

def count_lines(file):
    with open(file) as f:
        lines = f.read().splitlines()     
        print("Number of lines: " + str(len(lines)))

def count_words(file):
    with open(file) as f:
        words = f.read().split()
        print("Number of words: " + str(len(words)))

count_lines("../data/obama_speech.txt")
count_words("../data/obama_speech.txt")
count_lines("../data/michelle_obama_speech.txt")
count_words("../data/michelle_obama_speech.txt")
count_lines("../data/donald_speech.txt")
count_words("../data/donald_speech.txt")
count_lines("../data/melina_trump_speech.txt")
count_words("../data/melina_trump_speech.txt")

def most_spoken(file, query):
    with open(file) as country:
        countries_data = json.loads(country.read())
        new_dict = dict()
        for each in countries_data:
            for language in each['languages']:
                if language in new_dict:
                    new_dict[language] += 1
                else:
                    new_dict[language] = 1
        sort_spoken = sorted(new_dict.items(), key=lambda x:x[1])
        return sort_spoken[-int(query):]
print(most_spoken("../data/countries_data.json", 10))

def most_populated(file, query):
    with open(file) as country:
        countries_data = json.loads(country.read())
        sort_pop = sorted(countries_data, key=lambda d:d['population'])
        new_list = list()
        for name in sort_pop[-int(query):]:
            new_list.append(name['name'])
        return new_list

print(most_populated("../data/countries_data.json", 10))

# Exercises: Level 2
# Extract all incoming email addresses as a list from the email_exchange_big.txt file.
# Find the most common words in the English language. Call the name of your function find_most_common_words, it will take two parameters - a string or a file and a positive integer, indicating the number of words. Your function will return an array of tuples in descending order. Check the output

def extract_email(file):
    with open(file) as f:
        lines = f.read().splitlines()
        new_list = list()
        for line in lines:
            if line.startswith('From'):
                email = line.split()[1]
                new_list.append(email)
        return new_list
print(extract_email('../data/email_exchanges_big.txt'))
