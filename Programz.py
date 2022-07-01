# Write a Python program to print the following string in a specific format
# "Twinkle, twinkle, -------- what you are" 
#print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")

# Write a Python program to get the Python version you are using. 
# import sys
# print("Python version")
# print (sys.version)

# print("Version info.")
# print (sys.version_info)

# Write a Python program to display the current date and time.
# import datetime
# now = datetime.datetime.now()
# print("Current date and time: ")
# print(str(now))

# Write a Python program which accepts the radius of a circle from the user and compute the area
# r = float(input("Enter radius of circle: "))
# a = 3.14159 * r * r
# print("Area of circle =", a)

# Print first and last name in reverse order with a space between them
# fname = input("Input your First Name : ")
# lname = input("Input your Last Name : ")
# print ("Hello  " + lname + " " + fname)

#Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
#  3, 5, 7, 23
# values = input("Input some comma seprated numbers : ")
# list = values.split(",")
# tuple = tuple(list)
# print('List : ',list)
# print('Tuple : ',tuple)

# Write a Python program to accept a filename from the user and print the extension of that
# filename= input("Enter Filename: ")
# f = filename.split(".")
# print ("Extension of the file is : ", f[-1])

# Write a Python program to display the first and last colors from the following list.
# color_list = ["Red","Green","White" ,"Black"]
# print(color_list [0],color_list[-1])

# Write a Python program to display the examination schedule.
# exam_st_date = (14,7,2022)
# print( "The examination will start from : %i / %i / %i"%exam_st_date)

# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn
# a = int(input("Input an integer : "))
# n1 = int( "%s" % a )
# n2 = int( "%s%s" % (a,a) )
# n3 = int( "%s%s%s" % (a,a,a) )
# print (n1+n2+n3)

# Write a Python program to print the documents of Python built-in function(s)
# print(abs.__doc__)

# Write a Python program to print the calendar of a given month and year.
# import calendar
# y = int(input("Input the year : "))
# m = int(input("Input the month : "))
# print(calendar.month(y, m))

#Write a Python program to print the following 
#Sample string :
# a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example

# print("""
# a string that you "don't" have to escape
# This
# is a  ....... multi-line
# heredoc string --------> example
# """)

# Write a Python program to calculate number of days between two dates
# from datetime import date
# f_date = date(2022, 7, 2)
# l_date = date(2022, 7, 11)
# Days = l_date - f_date
# print(Days.days)

# Write a Python program to get the volume of a sphere with radius 9
# pi = 3.1415926535897931
# r= 9.0
# V= 4.0/3.0*pi* r**3
# print('The volume of the sphere is: ',V)

# Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.
# def difference(n):
#     if n <= 17:
#         return 17 - n
#     else:
#         return (n - 17) * 2 

# print(difference(22))
# print(difference(14))

#  Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum
# def sum_thrice(x, y, z):

#      sum = x + y + z
  
#      if x == y == z:
#       sum = sum * 3
#      return sum
# print(sum_thrice(1, 2, 3))
# print(sum_thrice(6, 6, 6))

# Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user. 
# num = int(input("Enter a number: "))
# mod = num % 2
# if mod > 0:
#     print("This is an odd number.")
# else:
#     print("This is an even number.")  

#  Write a Python program to count the number 4 in a given list
# def count(lst, x):
#     count = 0
#     for num in lst:
#         if (num == x):
#             count = count + 1
#     return count
# lst = [4,7,7,4,9,4,7,4]
# x = 4
# print('{} has occurred {} times'.format(x, count(lst, x)))

# Write a Python program to test whether a passed letter is a vowel or not.
# def is_vowel(char):
#     all_vowels = 'aeiou'
#     return char in all_vowels
# print(is_vowel('a'))
# print(is_vowel('e'))

# Write a Python program to check whether a specified value is contained in a group of values. 
# def is_group_member(group_data, n):
#    for value in group_data:
#        if n == value:
#            return True
#    return False
# print(is_group_member([1, 5, 8, 3], 3))
# print(is_group_member([5, 8, 3], -1))

# Write a Python program to create a histogram from a given list of integers.
# def histogram( items ):
#     for n in items:
#         output = ''
#         times = n
#         while( times > 0 ):
#           output += '*'
#           times = times - 1
#         print(output)
# histogram([2, 7, 5, 6])

# Write a Python program to concatenate all elements in a list into a string and return it
# def concatenate_list_data(list):
#     result= ''
#     for element in list:
#         result += str(element)
#     return result
# print(concatenate_list_data([4, 5, 12, 6]))

# Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence
# numbers = [    
    # 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    # 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    # 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    # 958,743, 527
    # ]
    # 
# numbers = [    
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
#     958,743, 527
#     ]

# for x in numbers:
#     if x == 237:
#         print(x)
#         break;
#     elif x % 2 == 0:
#         print(x)

# Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])

# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# print("Original set elements:")
# print(color_list_1)
# print(color_list_2)
# print("\nDifferenct of color_list_1 and color_list_2:")
# print(color_list_1.difference(color_list_2))
# print("\nDifferenct of color_list_2 and color_list_1:")
# print(color_list_2.difference(color_list_1))

# Write a Python program that will accept the base and height of a triangle and compute the area. 
# b = int(input("Input the base : "))
# h = int(input("Input the height : "))
# area = b*h/2
# print("area = ", area)

# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero
# def sum_three(x, y, z):
#     if x == y or y == z or x==z:
#         sum = 0
#     else:
#         sum = x + y + z
#     return sum
# print(sum_three(2, 1, 2))
# print(sum_three(3, 2, 2))
# print(sum_three(2, 2, 2))
# print(sum_three(1, 2, 3))

# Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.
# def sum(x, y):
#     sum = x + y
#     if sum in range(15, 20):
#         return 20
#     else:
#         return sum

# print(sum(10, 6))
# print(sum(10, 2))
# print(sum(10, 12))

# Write a Python program to display your details like name, age, address in three different lines
# def personal_details():
#     name, age = "Shreee", 25
#     address = "Mohali, Chandigarh, India"
#     print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))
# personal_details()
		
# Write a Python program to solve (x + y) * (x + y).
# x= int(input("User Input Value1: "))
# y= int(input("User Input Value2: "))
# result = x * x + 2 * x * y + y * y
# print(result)

# Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years
#  amt = 10000, int = 3.5, years = 7
# amt = 10000
# int = 3.5
# years = 7
# future_value = amt*((1+(0.01*int)) ** years)
# print(round(future_value,2))

# Write a Python program to parse a string to Float or Integer.
# n = "348.3458"
# print(float(n))
# print(int(float(n)))

# Write a Python program to print without newline or space.
# for i in range(0, 10):
#     print('*', end="")
# print("\n")


# Write a Python program to convert height (in feet and inches) to centimeters.
# print("Input your height: ")
# h_ft = int(input("Feet: "))
# h_inch = int(input("Inches: "))
# h_inch += h_ft * 12
# h_cm = round(h_inch * 2.54, 1)
# print("Your height is : %d cm." % h_cm)


