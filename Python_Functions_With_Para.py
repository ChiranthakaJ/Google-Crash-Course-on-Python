#Example 01 - Function with Multiple Parameters Type 01. 

def get_seconds(hours, minutes, seconds):
    return 3600*hours + 60*minutes + seconds

amount_a = get_seconds(2,30,0)
amount_b = get_seconds(0, 45, 15)
result = amount_a+ amount_b

print(result)

#Example 02 - Function with Multiple Parameters Type 02. 

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

hours, minutes, remaining_seconds = convert_seconds(5000) #In here we assign the results of the function to 3 different variables at once

print(hours, minutes, remaining_seconds) 

#Similar to the above assign statement, you can use the standard assign method like the below.

hours = convert_seconds(5000)
minutes = convert_seconds(5000)
remaining_seconds = convert_seconds(5000)

print(hours, minutes, remaining_seconds)

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


