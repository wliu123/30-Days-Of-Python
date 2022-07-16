#Declare an empty list
empty = list()
#Declare a list with more than 5 items
new_list = [1, 3, 4, 3, 9]
#Find the length of your list
print(len(new_list))
#Get the first item, the middle item and the last item of the list
print(new_list[0])
print(new_list[2])
print(new_list[-1])

#Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['John', 15, 5.4, 'single', '123 Wallabee Rd']
#Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
#Print the list using print()
print(it_companies)
#Print the number of companies in the list
print(len(it_companies))
#Print the first, middle and last company
print(it_companies[0])
print(it_companies[-1])
print(it_companies[int(len(it_companies)/2)])
#Print the list after modifying one of the companies
it_companies[0] = 'Meta'
print(it_companies)
#Add an IT company to it_companies
it_companies.append('Salesforce')
#Insert an IT company in the middle of the companies list
it_companies.insert(int(len(it_companies)/2), 'Autodesk')
#Change one of the it_companies names to uppercase (IBM excluded!)
print(it_companies[0].upper())
#Join the it_companies with a string '#;  '
'#; '.join(it_companies)
#Check if a certain company exists in the it_companies list.
print('Meta' in it_companies)
#Sort the list using sort() method
it_companies.sort()
#Reverse the list in descending order using reverse() method
it_companies.sort(reverse=True)
#Slice out the first 3 companies from the list
it_companies[0:3]
#Slice out the last 3 companies from the list
print(it_companies[-3:])
#Slice out the middle IT company or companies from the list
mid = int(len(it_companies)/2)
print(it_companies[mid])
#Remove the first IT company from the list
it_companies.remove(it_companies[0])
#Remove the middle IT company or companies from the list
it_companies.remove(it_companies[mid])
#Remove the last IT company from the list
it_companies.remove(it_companies[-1])
#Remove all IT companies from the list
it_companies.clear()
#Destroy the IT companies list
del it_companies

#Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
#After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = front_end.copy()
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)

#The following is a list of 10 students ages:
# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age
# Add the min age and the max age again to the list
# Find the median age (one middle item or two middle items divided by two)
# Find the average age (sum of all items divided by their number )
# Find the range of the ages (max minus min)
# Compare the value of (min - average) and (max - average), use abs() method

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
minimum = min(ages)
maximum = max(ages)
ages.extend([minimum, maximum])
ages.sort()
def median(lst):
    length_list = len(lst)
    med = (length_list-1) // 2
    if (length_list % 2):
        return lst[med]
    else:
        return (lst[med] + lst[med + 1])/2.0

def average(lst):
    sum = 0
    length_list = len(lst)
    for age in ages:
        sum += age
    return sum/length_list

range = maximum - minimum
print(abs(minimum - average(ages)))
print(abs(maximum - average(ages)))





