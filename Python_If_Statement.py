#Exercise 01 - The is_positive function should return True if the number received is positive, otherwise it returns None.

def is_positive(number):
    if number>0:
        return True
    
print(is_positive(15))


#Exercise 02
def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long.")
    else:
        print("Valid username.")

hint_username("ChiranthakaJ")


#Exercise 03 - The is_positive function should return True if the number received is positive and False if it isn't.

def is_positive_v2(number):
    if number > 0:
        return True
    else:
        return False
    
print(is_positive_v2(15))


#Exercise 04 - Else is not always required and you can return the value for else without the else part.

def is_even(number):
    if number % 2 == 0: 
        return True
    return False

print(is_even(10))


#Exercise 05 - First example If--Elif--Else statement

def number_group(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

print(number_group(10)) #Should be Positive
print(number_group(0)) #Should be Zero
print(number_group(-5)) #Should be Negative


#Exercise 06 - Second example If--Elif--Else with 

def hint_username(username):
    if len(username) < 3: 
        return("Invalid username. Must be at least 3 characters long.")
    elif len(username) > 15: 
        return("Invalid username. Must be at most 15 characters long.")
    else: 
        return("Valid username.")
        
print(hint_username("ChiranthakaJ"))


#Exercise 07 - 
print("A dog" < "A mouse")
print(9999+8888 > 100*100)


#Exercise 08 - The function receives a name, then returns a greeting based on whether or not that name is "Taylor".

def greeting(name):
    if name == "Taylor":
        return "Welcome back Taylor!"
    else:
        return "Hello there, " + name

print(greeting("Taylor"))
print(greeting("John"))

#Result ==> Welcome back Taylor!
#           Hello there, John


#Exercise 09 - If a filesystem has a block size of 4096 bytes, this means that a file comprised of only one byte will still use 4096 bytes of storage. A file made up of 4097 bytes will use 4096*2=8192 bytes of storage. Knowing this, can you fill in the gaps in the calculate_storage function below, which calculates the total number of bytes needed to store a file of a given size?

def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize//4096
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = filesize % 4096
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
         return 4096*(full_blocks+1)
    return full_blocks*4096

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192


#Exercise 10 - The color_translator function receives the name of a color, then prints its hexadecimal value. Currently, it only supports the three additive primary colors (red, green, blue), so it returns "unknown" for all other colors.

def color_translator(color):
    if color == "red":
	    hex_color = "#ff0000"
    elif color == "green":
	    hex_color = "#00ff00"
    elif color == "blue":
	    hex_color = "#0000ff"
    else:
	    hex_color = "unknown"
    return hex_color

print(color_translator("blue")) # Should be #0000ff
print(color_translator("yellow")) # Should be unknown
print(color_translator("red")) # Should be #ff0000
print(color_translator("black")) # Should be unknown
print(color_translator("green")) # Should be #00ff00
print(color_translator("")) # Should be unknown


#Exercise 11 - Students in a class receive their grades as Pass/Fail. Scores of 60 or more (out of 100) mean that the grade is "Pass". For lower scores, the grade is "Fail". In addition, scores above 95 (not included) are graded as "Top Score". Fill in this function so that it returns the proper grade.

def exam_grade(score):
    if score>95:
	    grade = "Top Score"
    elif score>=60:
	    grade = "Pass"
    else:
	    grade = "Fail"
    return grade

print(exam_grade(65)) # Should be Pass
print(exam_grade(55)) # Should be Fail
print(exam_grade(60)) # Should be Pass
print(exam_grade(95)) # Should be Pass
print(exam_grade(100)) # Should be Top Score
print(exam_grade(0)) # Should be Fail


#Exercise 12 - This function receives the first_name and last_name parameters and then returns a properly formatted string.

def format_name(first_name, last_name):
    	# code goes here
	if first_name !="" and last_name !="":
	  string = ("Name: "+ last_name +", "+ first_name)
	elif first_name !=" " or last_name !=" ":
	  string = ("Name: "+ last_name + first_name)
	return string 

print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string


#Exercise 13 - The longest_word function is used to compare 3 words. It should return the word with the most number of characters (and the first in the list when they have the same length). Fill in the blank to make this happen

def longest_word(word1, word2, word3):
    if len(word1) >= len(word2) and len(word1) >= len(word3):
        word = word1
    elif len(word2) >= len(word3):
        word = word2
    else:
        word = word3
    return(word)

print(longest_word("chair", "couch", "table"))
print(longest_word("bed", "bath", "beyond"))
print(longest_word("laptop", "notebook", "desktop"))


#Exercise 14 - The fractional_part function divides the numerator by the denominator, and returns just the fractional part (a number between 0 and 1). Complete the body of the function so that it returns the right number. Note: Since division by 0 produces an error, if the denominator is 0, the function should return 0 instead of attempting the division.

def fractional_part(numerator, denominator):
    	# Operate with numerator and denominator to 
    if denominator >0:
        return (numerator%denominator)/denominator
# keep just the fractional part of the quotient
    return 0

print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0