# Exercises: Day 17
# names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']. Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.
names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
fin, swe, nor, den, ice, *rest = names
nordic_countries = fin, swe, nor, den, ice, rest
print(names)
print(nordic_countries)
*before, es, ru = names

