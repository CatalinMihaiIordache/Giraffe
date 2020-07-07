import useful_tools

print(useful_tools.roll_dice(10))


# ### Writing a file ###
# employee_file = open("C:\\Users\CatalinMihaiIordache\Documents\PycharmProjects\Giraffe\employees3.txt", "w")
# employee_file.write("Elena - IC Controller\n")
# employee_file.write("Balena - Happy" + "\n")
# employee_file.close()



# ### Reading a file ###
# employee_file = open("C:\\Users\CatalinMihaiIordache\Documents\PycharmProjects\Giraffe\employees3.txt", "r")
# for employee in employee_file.readlines():
#     print(employee)
# employee_file.close()



# ### Appending to an existing file ###
# employee_file = open("C:\\Users\CatalinMihaiIordache\Documents\PycharmProjects\employees.txt", "a")
# employee_file.write("\nKelly - Customer Service\n")
# employee_file.write("Toby - Human Resources" + "\n")
# employee_file.close()



# ### Reading a file ###
# employee_file = open("D:\Python\sample1.csv", "r")
# print(employee_file.readline())
# print(employee_file.readlines()[1])
#
# for employee in employee_file.readlines():
#     print(employee)
#
# employee_file.close()



# try:
#     number = int(input("Enter a number: "))
#     print(number)
#     value = 10/0
# except ZeroDivisionError:
#     print("Divided by zero.")
# except ValueError:
#     print("Invalid input.")



# def translate(phrase):
#     translation = ""
#     for letter in phrase:
#         if letter.lower() in "aeiou":
#             if letter.isupper():
#                 translation = translation + "G"
#             else:
#                 translation = translation + "g"
#         else:
#             translation = translation + letter
#     return translation
#
# print(translate(input("Enter a phrase:")))



# number_grid = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [0]
# ]
#
# for row in number_grid:
#     for col in row:
#         print(col)
#
# print(number_grid[0][0])



# def raise_to_power(base_num, pow_num):
#     result = 1
#     for index in range(pow_num):
#         result = result * base_num
#     return result
#
# print(raise_to_power(3,4))



# friends = ["Kevin", "Karen", "Jim","Toto","July"]
#
# for friend in friends:
#     print(friend)
# print("#########################")
#
# for index in range(10):
#     print(index)
# print("#########################")
#
# for index in range(3, 10):
#     print(index)
# print("#########################")
#
# for index in range(len(friends)):
#     print(friends[index])
# print("#########################")
#
# for index in range(len(friends)):
#     print(friends[3])
# print("#########################")
#
# for index in range(5):
#     if index == 0:
#         print("First Iteration")
#     else:
#         print("Not First Iteration")
# print("#########################")




# secret_word = "Giraffe"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False
#
# while guess != secret_word and not(out_of_guesses):
#     if  guess_count < guess_limit:
#         guess = input("Enter guess: ")
#         guess_count += 1
#     else:
#         out_of_guesses = True
#
# if out_of_guesses:
#     print("Out of Guesses, YOU LOSE!")
# else:
#     print("You win!")



# i = 1
# while i <= 10:
#     print(i)
#     i = i + 1  # or i += 1
#
# print("Done with loop!")



# monthConversions = {           # this is a dictionary!
#     "Jan" : "January",
#     "Feb" : "February",
#     "Mar" : "March",
#     "Apr" : "April",
#     "May" : "May",
#     "Jun" : "June",
# }
#
# print(monthConversions["May"])
# print(monthConversions.get("Dec", "Not a valid key!"))



# num1 = float(input("Enter first number: "))
# op = input("Enter operator: ")
# num2 = float(input("Enter second number: "))
#
# if op == "+":
#     print(num1 + num2)
# elif op == "-":
#     print(num1 - num2)
# elif op == "/":
#     print(num1 / num2)
# elif op == "*":
#     print(num1 * num2)
# else:
#     print ("Invalid operator entered!")



# def max_num(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2>= num3:
#         return num2
#     else:
#         return num3
#
# print(max_num(300, 4, 5))



# is_male = False
# is_tall = False
#
# if is_male or is_tall:
#     print("You are a male or tall or both.")
# else:
#     print("You are neither male not tall.")
#
# if is_male and is_tall:
#     print("You are a tall male.")
# elif is_male and not(is_tall):
#     print("You are a short male.")
# elif not(is_male) and is_tall:
#     print("You are not a male, but are tall.")
# else:
#     print("You are not a male and not tall.")


# def cube(num):
#     return num*num*num
#
# result = cube(4)
# print(result)


# def say_hi(name, age):     # This is a function declaration
#     print("Hello " + name + "! You are " + str(age) + ".")
#
# print("Top")
# say_hi("Mike", "23")
# print("Bottom")
# say_hi("Steve", "44")


# lucky_numbers = [4, 8, 15, 16, 23, 42]
# friends = ["Kevin", "Karen", "Jim","Toto","July"]
# friends.extend(lucky_numbers)
# friends.append("Creed")
# friends.insert(1, "Kelly")
# friends.remove("Toto")
# #friends.clear()
# friends.pop() # removes last list element
# print(friends)
#
# coordinates = (4, 5)  # this is how a tuple is defined
# coordinates_two = [(4, 5), (6, 7), (80, 34)]  # this is a list of tuples
# coordinates[0] = 10
# print(coordinates[0])


# from datetime import *
#
# year = timedelta(days=365)
# ten_years = 10 * year
# print(ten_years)
# print(ten_years.days // 365)
# nine_years = ten_years - year
# print(nine_years)

# friends = ["Kevin", "Karen", "Jim","Toto","July"]
# friends[1] = "Mike"
# print(friends)
# print(friends[-3])
# print(friends[-1])
# print(friends[0])
# print(friends[1:3])


# color = input("Enter a color: ")
# plural_noun = input("Enter a plural noun: ")
# celebrity = input("Enter a celebrity: ")
# print("Roses are " + color)
# print(plural_noun + " are blue")
# print("I love " + celebrity)


# from math import *
# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")
# result = float(num1) + int(floor(float(num2)))
# print(result)


# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print("Hello " + name + "! You are " + str(age) +"!")


# print(3 * (2 + 4))
# print(10 % 3) # restul impartirii lui 10 la 3 (modulus)
# my_num = -5
# print(str(my_num) + " my favorite number")
# print(abs(my_num))
# print(pow(3,2))
# print(max(3,2))
# print(min(3,2))
# print(round(3.7))
#
# from math import *
# print(floor(3.7),"is the floor of 3.7")
# print(ceil(3.7),"is the ceil of 3.7")
# print(sqrt(36),"is the sqrt of 36")
#

# phrase = "Giraffe Academy"
# print(phrase + " is cool")
# print(phrase.lower())
# print(phrase.upper())
# print(phrase.isupper())
# print(phrase.upper().isupper())
# print(len(phrase))
# print(phrase[0])
# print(phrase.index("a"))
# print(phrase.replace("Giraffe","Elephant"))


# character_name = "John"
# character_age = 35
# is_Male = True
# print("There once was a man named " + character_name + ", ")
# print("he was 35 years old. ")
# character_name = "Mike"
# print("He really liked the name " + character_name + ", ")
# print("but didn't like being " + character_age + ".")