# Exercises: Level 1
# Write a function which count number of lines and number of words in a text. All the files are in the data the folder: a) Read obama_speech.txt file and count number of lines and words b) Read michelle_obama_speech.txt file and count number of lines and words c) Read donald_speech.txt file and count number of lines and words d) Read melina_trump_speech.txt file and count number of lines and words

# Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages
#Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries
import json

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

with open("../data/countries_data.json") as country:
    countries_data = country.read()
    def most_spoken(data):
        test = json.loads(data)
        empty = dict()
        
        for language in test['languages']:
            if language in empty:
                empty[language] += 1
            else:
                empty[language] = 0
        return empty
    most_spoken(countries_data)
# countries_data = json.loads("../data/countries_data.json")
# print(countries_data)
# def most_spoken(file):
