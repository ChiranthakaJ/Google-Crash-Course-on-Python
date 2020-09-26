# Just like people have parents, grandparents, and so on, objects have an ancestry. The principle of inheritance let's a programmer build relationships between concepts and group them together.

#In particular, this allows us to reduce code duplication by generalizing our code. 

#For example, how could we develop our apple representation to include other types of fruit, too? Well, one thing we know about an apple is that it's a fruit. So we could define a separate fruit class. 

#Example 01 - 

class Fruit: 
    
# We also know that all fruits have a color and taste. So what if we moved our color and flavor attributes into the fruit class? Here, we have a fruit class with a constructor for the color and flavor attributes. 
    
    def __init__(self, color, flavor): 
        self.color = color
        self.flavor = flavor

#Now, we can rewrite our apple class and easily add another fruit into the mix, too.

#In Python, we use parentheses in the class declaration to show an inheritance

#Syntax
#-------------------------------------------------
'''
class ClassName(super class name)
    class body
'''

class Apple(Fruit):
    pass

class Grape(Fruit): 
    pass

#For our new fruit classes, we've used that syntax to tell our computer that both the apple and the grape classes inherit from the fruit class.

#Because of this, they automatically have the same constructor, which sets the color and flavor attributes. You can think of the fruit class as the parent class, and the apple and grape classes as siblings. 
