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

def find_most_common_words(file, num_words):
    new_dict = dict()
    with open(file) as f:
        read_doc = f.read()
        for word in read_doc:
            if word in new_dict:
                new_dict[word] += 1
            else:
                new_dict[word] = 1
        sort_doc = sorted(new_dict.items(), key=lambda x:x[1], reverse=True)
        return sort_doc[:num_words+1]

# Use the function, find_most_frequent_words to find: a) The ten most frequent words used in Obama's speech b) The ten most frequent words used in Michelle's speech c) The ten most frequent words used in Trump's speech d) The ten most frequent words used in Melina's speech
# Write a python application that checks similarity between two texts. It takes a file or a string as a parameter and it will evaluate the similarity of the two texts. For instance check the similarity between the transcripts of Michelle's and Melina's speech. You may need a couple of functions, function to clean the text(clean_text), function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity). List of stop words are in the data directory
# Find the 10 most repeated words in the romeo_and_juliet.txt
# Read the hacker news csv file and find out: a) Count the number of lines containing python or Python b) Count the number lines containing JavaScript, javascript or Javascript c) Count the number lines containing Java and not JavaScript

def most_frequent_o(file):
    new_dict = dict()
    with open(file) as f:
        read_file = f.read().lower().split()
        for word in read_file:
            if word in new_dict:
                new_dict[word] += 1
            else:
                new_dict[word] = 1
        sort_word = sorted(new_dict.items(), key=lambda x:x[1], reverse=True)
        return sort_word[:11]
print(most_frequent_o('../data/obama_speech.txt'))
print(most_frequent_o('../data/michelle_obama_speech.txt'))
print(most_frequent_o('../data/donald_speech.txt'))
print(most_frequent_o('../data/melina_trump_speech.txt'))

