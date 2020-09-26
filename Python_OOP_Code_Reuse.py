# Just like people have parents, grandparents, and so on, objects have an ancestry. The principle of inheritance let's a programmer build relationships between concepts and group them together.

#In particular, this allows us to reduce code duplication by generalizing our code. 

#For example, how could we develop our apple representation to include other types of fruit, too? Well, one thing we know about an apple is that it's a fruit. So we could define a separate fruit class. 

#Example 01 

class Fruit: 
    
# We also know that all fruits have a color and taste. So what if we moved our color and flavor attributes into the fruit class? Here, we have a fruit class with a constructor for the color and flavor attributes. 
    
    def __init__(self, color, flavor): 
        self.color = color
        self.flavor = flavor

#Now, we can rewrite our apple class and easily add another fruit into the mix, too.

#In Python, we use parentheses in the class declaration to show an inheritance.

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

#Let's see this in action.

#Example 02

#First, we create an instance of the apple class.

granny_smith = Apple("green", "tart")

#Now, an instance of the grape class.

carnelian = Grape("purple", "sweet")

#Then, to check that this actually worked, let's print the attributes values.

print(granny_smith.flavor) #=====> tart
print(carnelian.color)     #=====> sweet

#With the inheritance technique, we can use the fruit class to store information that applies to all kinds of fruit, and keep apple or grape specific attributes in their own classes. 

#For example, we could have an attribute to track how much of an apple is left after it's partially eaten. Of course, this applies to both attributes and methods. 

#If a class has an attribute or a method defined in it, inheriting classes will have the same attributes and methods defined in them. But we can also get them to behave differently depending on what we change. 

#Let's go back to our piglet example and change it so that there's a base animal class.

#Example 03 

class Animal: 
    sound = ""
    def __init__(self, name): 
        self.name = name
    def speak(self):
        print("{sound} I'm {name}! {sound}".format(name=self.name, sound=self.sound))
        
class Piglet(Animal): 
    sound = "Oink!"

hamlet = Piglet("Hamlet")
hamlet.speak()

#In this code, we've defined a general class called animal, which has an attribute to store the sound that the animal makes. The constructor of the class takes the name that will be assigned to the instance when it's created.

#There's also a speak method that prints the name of the animal together with the sound the animal makes. Then, we have a piglet class that inherits from the animal class. We set the value of the sound attribute to oink in the piglet class, and that's the only thing we've modified from the original. Everything else is inherited. Let's see this in action.

#Let's define a new class that also inherits from animal. How about a cow class? To finish, let's create an instance of this class to make it speak.

class Cow(Animal): 
    sound = "Moooo"
    
Milky = Cow("Milky white")
Milky.speak()

#So you can see that we can easily define new classes that inherit from the base animal class and use both the attributes and methods that the animal class provides.

#Example 04 - Let’s create a new class together and inherit from it. Below we have a base class called Clothing. Together, let’s create a second class, called Shirt, that inherits methods from the Clothing class. Fill in the blanks to make it work properly.

class Clothing:
      material = ""
      def __init__(self,name):
        self.name = material
      def checkmaterial(self):
	    print("This {} is made of {}".format(self.___,self.___))
			
class Shirt(___):
  material="Cotton"

polo = Shirt("Polo")
polo.checkmaterial()

#Inheritance lets you reuse code written for one class in other classes. 