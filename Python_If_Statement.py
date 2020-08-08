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