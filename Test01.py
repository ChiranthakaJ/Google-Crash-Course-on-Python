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