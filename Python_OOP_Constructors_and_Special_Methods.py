#Up to now, we've been creating classes with empty or default values and their attributes and then setting the attribute values after we've created the object. 

#This works, but it's not ideal. Working this way means we need to write a separate line for each attribute we want to set, and that makes it really easy to forget to set an important value.

#So let's set those values as we create the instance. 

# This way, we know that our instance has all the important values in it from the moment is created and we don't have to worry about it. 

#To do this, we need to use a special method called constructor.

#Let's have look at the below example.

class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
        


#The constructor of the class is the method that's called when you call the name of the class. 

#It's always named init. This __init__() method is a very special method that is in the Python language.

#This method on top of the self variable that represents the instance receives two more parameters: color and flavor. 

#Then the method sets those values as the values of the current instance, jonagold. Let's have this in action.

jonagold = Apple("red", "sweet")

#Now, let's check that all the attributes are set correctly.

print(jonagold.color)   #=====>  'red'
print(jonagold.flavor)  #=====>  'sweet'

#Now by adding a constructor method that sets the attributes, we can create the class and have its values set right when it's created.

#Constructors aren't the only special methods we can write. When we use the STR or print functions to convert an object to a string, we are using a super-useful special method.

#Let's see what happens when we don't define it.

print(jonagold)     #=====> <__main__.Apple object at 0x000000896A5E54F0>

#When we don't specify a way to print an object, Python uses the default method that prints the position where the object is stored in the computer's memory. 

#If you ever try and print something and Python prints a random string of numbers and letters, you'll know that it's likely using the default representation, which is the position of the object in the computer's memory. 

#So how do we tell Python to print something that makes sense for us? We use the special STR method which returns the string that we want to print.

#By defining the special STR method, we're telling Python that we want it to display when the print function is called with an instance of our class.

class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
    def __str__(self): 
        return "This apple is {} and its flavor is {}".format(self.color, self.flavor)
    
jonagold = Apple("red", "sweet")
print(jonagold)     #=====> This apple is red and its flavor is sweet

#So the STR method lets us print a friendly message instead of a bunch of numbers.

#In general, it's a good idea to think ahead and define the STR method when creating objects that you want to print.  