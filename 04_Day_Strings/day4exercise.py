#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
thirty = 'Thirty'
days = 'Days'
of = 'Of'
language = 'Python'
full_sentence = thirty + days + of + language
print(full_sentence)

#Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"
#Print the variable company using print().
print(company)
#Print the length of the company string using len() method and print().
print(len(company))
#Change all the characters to uppercase letters using upper() method.
print(company.upper())
#Change all the characters to lowercase letters using lower() method.
print(company.lower())
#Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())
#Cut(slice) out the first word of Coding For All string.
print(company[:6])
#Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.find('Coding'))
#Replace the word coding in the string 'Coding For All' to Python.
company_new = company.replace('Coding', 'Python')
#Change Python for Everyone to Python for All using the replace method or other methods.
print(company_new.replace('Everyone', 'All'))
#Split the string 'Coding For All' using space as the separator (split()) .
print(company.split(' '))
#"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
test_string = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(test_string.split(','))
#What is the character at index 0 in the string Coding For All.
print(company[0])
#What is the last index of the string Coding For All.
print(company[-1])
#What character is at index 10 in "Coding For All" string.
print(company[10])
#Create an acronym or an abbreviation for the name 'Python For Everyone'.
name = "Python For Everyone"
def acronym(string): 
    words = string.split()
    new_string = ""
    for word in words:
        new_string += word[0]
    new_string.upper()
    return new_string
print(acronym(name))

#Create an acronym or an abbreviation for the name 'Coding For All'.
name_coding = "Coding For All"
print(acronym(name_coding))

#Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index('C'))
#Use index to determine the position of the first occurrence of F in Coding For All.
print(company.index('F'))
#Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(company.rfind('l'))
#Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.index('because'))
#Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rindex('because'))
#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
new_sentence = "You cannot end a sentence with because because because is a conjunction"
print(new_sentence.find('because'))
print(new_sentence.rfind('because'))
print(new_sentence[31:54])
#Does ''Coding For All' start with a substring Coding?
print(name_coding.find('Coding') == 0)
#Does 'Coding For All' end with a substring coding?
print(name_coding.rfind('coding') != -1)
#'   Coding For All      '  , remove the left and right trailing spaces in the given string.
given = "   Coding For All      "
print(given.strip(' '))

#The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(libraries))
#Use the new line escape sequence to separate the following sentences.
print("I am enjoying this challenge.\nI just wonder what is next.")
#Use a tab escape sequence to write the following lines.
print('Name\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinki')
#Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
result = 'The area of a circle with radius {} is {} meters square.'.format(str(radius), str(int(area)))
print(result)
#Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144
first_int = 8
second_int = 6
print('{}+{}={}'.format(first_int, second_int, first_int + second_int))
print('{}-{}={}'.format(first_int, second_int, first_int - second_int))
print('{}*{}={}'.format(first_int, second_int, first_int * second_int))
print('{}/{}={:.2f}'.format(first_int, second_int, first_int / second_int))
print('{}%{}={}'.format(first_int, second_int, first_int % second_int))
print('{}//{}={}'.format(first_int, second_int, first_int // second_int))
print('{}**{}={}'.format(first_int, second_int, first_int ** second_int))

