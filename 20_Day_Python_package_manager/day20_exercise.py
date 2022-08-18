# Exercises: Day 20
# Read this url and find the 10 most frequent words. romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
# Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
# the min, max, mean, median, standard deviation of cats' weight in metric units.
# the min, max, mean, median, standard deviation of cats' lifespan in years.
import requests
import collections
import numpy as np

url = 'http://www.gutenberg.org/files/1112/1112.txt'
response = requests.get(url)
each_word = response.text.split()
counteach = collections.Counter(each_word).most_common(10)

cats_api = 'https://api.thecatapi.com/v1/breeds'
cats_response = requests.get(cats_api)
data = cats_response.json()
metric_list = []
for each in data:
    each_number = each['weight']['metric'].split()
    metric_list.append(int(each_number[0]))
    metric_list.append(int(each_number[-1]))
# print(min(metric_list))
# print(max(metric_list))
# print(np.mean(metric_list))
# print(np.median(metric_list))
# print(np.std(metric_list))
# life_span_list = []
# for life in data:
#     each_life = life['life_span'].split()
#     life_span_list.append(int(each_life[0]))
#     life_span_list.append(int(each_life[-1]))
# print(min(life_span_list))
# print(max(life_span_list))
# print(np.mean(life_span_list))
# print(np.median(life_span_list))
# print(np.std(life_span_list))

# Read the countries API and find
# the 10 largest countries
# the 10 most spoken languages
# the total number of languages in the countries API

import json
with open('../data/countries_data.json') as f:
    country_pop = dict()
    language_count = dict()
    countries_data = json.loads(f.read())
    for each in countries_data:
        country_pop[each['name']] = each['population']
        for language in each['languages']:
            if language not in language_count:
                language_count[language] = 1
            else:
                language_count[language] += 1
    print(sorted(country_pop.items(), key=lambda x:x[1], reverse=True)[:10])
    print(sorted(language_count.items(), key=lambda x:x[1], reverse=True)[:10])
    print(len(language_count))
   