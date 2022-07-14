# Declare your age as integer variable
age = 20
# Declare your height as a float variable
height = 5.4
# Declare a variable that store a complex number
complex_number = 1 + 5j
# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = input("Enter base: ")
height = input("Enter height: ")
areaTri = 0.5 * base * height
print ("The area of the triangle is " + str(areaTri))
# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
a = input("Enter side a: ")
b = input("Enter side b: ")
c = input("Enter side c: ")
perimeter = a + b + c
print ("The perimeter of the triangle is " + str(perimeter))
# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = input("Enter length: ")
width = input("Enter width: ")
areaRec = length * width
print ("The area of rectangle is " + str(areaRec))
#Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius = input("Enter radius: ")
areaCir = 3.14 * radius
print("The area of the cirlce is " + str(areaCir))
#Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
y2 = 10
y1 = 2
x2 = 6
x1 = 2
slope = (y2 - y1)/(x2 - x1)
print ("Slope is " + str(slope))
#Find the length of 'python' and 'dragon' and make a falsy comparison statement.
a = len('dragon')
b = len('python')
print (a != b)
#Use and operator to check if 'on' is found in both 'python' and 'dragon'
print ('on' in 'python' and 'on' in 'dragon')
#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
sentence = "I hope this course is not full of jargon"
print ('jargon' in sentence)
#There is no 'on' in both dragon and python
print(not 'on' in 'dragon' and 'on' in 'python')
#Find the length of the text python and convert the value to float and convert it to string
convFloat = float(len('python'))
print(str(convFloat))
#Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
# check if number % 2 == 0 means it's even, if not it's odd

#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print(int(2.7) == 7//3)

#Check if type of '10' is equal to type of 10
print(type('10') == type(10))

#Check if int('9.8') is equal to 10

print(int(9.8) == 10)









