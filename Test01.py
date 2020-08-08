# REPLACE THIS STARTER CODE WITH YOUR FUNCTION
june_days = 30
print("June has " + str(june_days) + " days.")
july_days = 31
print("July has " + str(july_days) + " days.")

#Similar results using functions with parameters.

#Type 01
def month_days(month, days):
    result = f"{month} has {days} days."
    return (result)
print (month_days("June", 30))
print (month_days("July", 31))

#Type 02
def month_days(month, days):
    result = (month + " has " + str(days) + " days.")
    return(result)

print (month_days("June", 30))
print (month_days("July", 31))

#THIS FUCNTION CONVERTS MILES TO KILOMETERS(KM) & DOUBLES IT CALCULATE THE RETURN TRIP DISTANCE AS WELL.
def convert_distance(miles):
    km = miles * 1.6  # approximately 1.6 km in 1 mile
    return(km)

my_trip_km = convert_distance(55)
print("The distance in kilometers is " + str(my_trip_km))

print("The round-trip in kilometers is " + str(my_trip_km*2))


#THIS FUNCTION COMPARES TWO NUMBERS AND RETURNS THEM
def order_numbers(number1, number2):
    if number2 > number1:
        return number1, number2
    else:
        return number2, number1

smaller, bigger = order_numbers(100, 99)
print(smaller, bigger)


#THIS FUNCTION CALCULATE THE LUCKY NUMBER BY USING THE NAME
def lucky_number(name):
    number = len(name) * 9
    return ("Hello " + name + ". Your lucky number is " + str(number))
	    
print(lucky_number("Chiranthaka"))
print(lucky_number("Gayathri"))


#THIS FUNCTION concatinate 2 string variables depending their availability.

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
