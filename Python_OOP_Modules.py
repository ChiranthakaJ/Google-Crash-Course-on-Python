#To organize the code we need to perform tasks, Python provides an abstraction called a module. Modules can be used to organize functions, classes, and other data together in a structured way. 

#Internally, modules are set up through separate files containing the necessary classes and functions. Python already comes with a bunch of ready-to-use modules. All these modules are contained in a group called the Python standard library.

#We'll use the import keyword to import the random module. This module is useful for generating random numbers or making random choices.

import random

#Now that we've imported the module, let's use a function provided by this module called randint.
print(random.randint(1, 10))

#This function receives two parameters and generates a random number between the two parameters that we pass. In this case, we're generating a random number between 1 and 10. As you can see, this function returns different numbers each time it's called.

#The syntax used for calling a function provided by a module is similar to calling a method provided by a class. It uses a dot to separate the name of the module and the function provided by that module. 

#Let's try using a different module, the datetime module. We use this for handling dates and times.

#Example 02 - Let's get the current date.

import datetime

now = datetime.datetime.now()

print(type(now)) #=====> <class 'datetime.datetime'>

#If you're wondering why we have a doubled datetime, it's because the datetime module provides a datetime class, and the datetime class gives us a method called now. This now method generates an instance of the datetime class for the current time. We can operate on this instance of datetime in a bunch of ways.

print(now) #=====> '2020-09-26 23:21:34.212403'