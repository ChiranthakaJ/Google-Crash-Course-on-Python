#This is a flexible, powerful paradigm where classes represent and define concepts, while objects are instances of classes. 

#In our apple example, we can have a class called apple that defines the characteristics of an apple. We could then have a bunch of instances of that apple class, which are the individual objects of that class.

# Almost everything in Python is an object, all of the numbers, strings, lists, and dictionaries we've seen so far, and have used in our exercises and quizzes, have been objects.

#The core, apple pun intended, concept of object-oriented programming comes down to attributes and methods associated with a type. The attributes are the characteristics associated to a type, and the methods are the functions associated to a type. In the apple example, the attributes are the color and flavor. What would the methods be? Well, it depends on what we're going to do with apple. We could maybe have a cut method that turns one whole apple into four slices, or we could have an eat method that reduces the amount of apple available with every bite. 

#Let's think about a more IT focused example, like a file in our computer. A file has lots of attributes, it has a name, a size, the date it was created, permissions to access it, its contents, and a whole lot more.

#You can get your computer to list all the attributes and methods in a class. To do that Just use the dir function. This gets the Interpreter to print to the screen a list of all the attributes and methods.

print(dir(""))

#The first bunch here are special methods that begin and end with double underscores. These methods aren't usually called by those weird names. Instead, they're called by some of the internal Python functions. For example, the __len__ method is called by the len function that we've used before to find out the length of a string. Or the __ge__ method is used to compare if one string is greater than or equal to another, when using the greater than or equal to operator.

#After the special methods, we see a lot of string methods that we've already come across. This list gives the names of all the methods, but it doesn't tell us how we can use them. There's a different function to tell us that, which is called help.

print(help(""))

#When we use the help function on any variable or value, we're showing all the documentation for the corresponding class.

#In this case, we're looking at the documentation for the str class, the class of the string object. As before, it starts with the special method. If we scroll down, we reach the ones we've already seen. 

#The help() function identify that has given within the parentheses is a string with the double quotes.

#If we give 'int' in the parentheses the result is different, because the help at that moment is for integers. 

#Likewise we can change the keyword in the parenthese and get the help for that class.

