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