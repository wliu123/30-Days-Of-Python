# Exercises: Level 1
# Write a function which generates a six digit/character random_user_id.
#   print(random_user_id());
#   '1ee33d'
# Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
# print(user_id_gen_by_user()) # user input: 5 5
# #output:
# #kcsy2
# #SMFYb
# #bWmeq
# #ZXOYh
# #2Rgxf
   
# print(user_id_gen_by_user()) # 16 5
# #1GCSgPLMaBAVQZ26
# #YD7eFwNQKNs7qXaT
# #ycArC5yrRupyG00S
# #UbGxOFI7UXSWAyKN
# #dIV0SSUTgAdKwStr
# Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
# print(rgb_color_gen())
# # rgb(125,244,255) - the output should be in this form
from random import randint
import random
import string

def random_user_id():
    random_id = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(7)])
    print(random_id)
random_user_id()

def user_id_gen_by_user():
    characters = input('How many characters? ')
    id_number = input('How many ids to be generated? ')
    for i in range(int(characters) + 1):
        print(''.join([random.choice(string.ascii_letters + string.digits) for i in range(int(id_number))]))

user_id_gen_by_user()

def rgb_color_gen():
    new_list=[]
    for i in range(4):
        numbers = randint(0, 256)
        new_list.append(numbers)
    return 'rgb({}, {}, {})'.format(new_list[0], new_list[1], new_list[2])
print(rgb_color_gen())


# Exercises: Level 2
# Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
# Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
# Write a function generate_colors which can generate any number of hexa or rgb colors.
#    generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
#    generate_colors('hexa', 1) # ['#b334ef']
#    generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
#    generate_colors('rgb', 1)  # ['rgb(33,79, 176)']

def list_of_hexa_colors(nums):
    new_list = []
    for i in range(nums):
        hexa = ''.join([random.choice(string.ascii_letters + string.digits) for j in range(6)])
        new_list.append('#' + hexa)
    return new_list

def list_of_rgb_colors(nums):
    
    new_list=[]
    for i in range(nums):
        # rgb = ''.join([randint(0, 257) for j in range(3)])
        color_list = random.choices(range(256), k=3)
        each_color = 'rgb({}, {}, {})'.format(color_list[0], color_list[1], color_list[2])
        new_list.append(each_color)
    return new_list

def generate_colors(type_of, nums):
    if type_of == 'hexa':
        print(list_of_hexa_colors(nums))
    elif type_of == 'rgb':
        print(list_of_rgb_colors(nums))
    else:
        print('not a valid type')

# Exercises: Level 3
# Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
# Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.

def shuffle_list(new_list):   
    return random.sample(new_list, k=len(new_list))

print(shuffle_list([1, 2, 3, 4]))

def random_nums():
    new_set = set()
    while len(new_set) < 7:
        new_set.add(randint(0, 9))
    return list(new_set)
print(random_nums())