#We can still use the Python function help to find documentation about classes and methods.

#We can also do this on our own classes, methods, and functions.

#Let's look at the below example.

class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
    def __str__(self): 
        return "This apple is {} and its flavor is {}".format(self.color, self.flavor)
    

print(help(Apple))

#This will get the below result.

'''
class Apple(builtins.object)
 |  Apple(color, flavor)
 |
 |  Methods defined here:
 |
 |  __init__(self, color, flavor)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
-- More  --
'''

#See how when we asked for help on our class we got a list of the methods that are defined in the class? In this example, the defined methods are the constructor and the conversion to string. But this documentation is super short and to be honest, it doesn't explain a whole lot. 

#We want our methods, classes, and functions to give us more information when we or someone else use the help function. We can do that by adding a docstring. 

#A docstring is a brief text that explains what something does. Let's have look at the below example.

def to_seconds(hours, minutes, seconds): 
    """Returns the amount of seconds in the given hours, minutes and seconds."""
    return hours*3600+minutes*60+seconds

#So there we have it, we have a function with a docstring in its body. Let's see how we can use the help function to see it.

print(help(to_seconds))


'''
Help on function to_seconds in module __main__:

to_seconds(hours, minutes, seconds)
    Returns the amount of seconds in the given hours, minutes and seconds.
'''

#The help function shows us the string we wrote.

#We can add docstrings to classes and methods too. Let's see it is in an example.

class Piglet: 
    """Represents a piglet that can say their name."""
    years = 0
    name = ""
    def speak(self): 
        """Outputs a message including the name of the piglet."""
        print("Oink! I'm {}! Oink!".format(self.name))
    
    def pig_years(self): 
        """Converts the current age to equivalent pig years."""
        return self.years*18
    
print(help(Piglet))

#When we get the help for a particular class, we will have all the Docstrings that was declared within the class. At this moment we will get the Docstrings that are in functions(), methods() and constructors.