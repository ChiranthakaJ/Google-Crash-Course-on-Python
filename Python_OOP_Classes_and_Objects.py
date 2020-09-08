#Defining a class.

'''Syntax

class class_name: 
    class body

'''

#Example 01
class Apple: 
    color=""
    flavor=""

#creating an instance(object) of the class. The instance name is jonagold.

'''Syntax

instance_name = Class_name()

'''

jonagold = Apple() 

#Assigning a value to attributes of the instance.

'''Syntax

instance_name.attribute = value

'''

#Instance 01
#----------------------------
jonagold.color = "red"
jonagold.flavor = "sweet"

print(jonagold.color)   #=====> red
print(jonagold.flavor)  #=====> sweet

#The attributes and methods of some objects can be other objects and can have attributes and methods of their own. For example, we could use the upper method to turn the string of the color attribute to uppercase. So print (jonagold.color.upper()).

print(jonagold.color.upper())   #=====> RED


#Instance 02
#----------------------------

golden =Apple() 
golden.color = "yellow"
golden.flavor = "soft"

print(golden.color)   #=====> yellow
print(golden.flavor)  #=====> soft


#Example 02 - Instance methods - Basic

class Piglet: 
    def speak(self):
        print("oink oink")

hamlet = Piglet() 
hamlet.speak()  #=====> oink oink


#Example 03 - Instance methods - Intermediate

class Piglet(): 
    name = "piglet"
    def speak(self): 
        print("Oink! I'm {}! Oink!".format(self.name))
        
hamlet = Piglet() 
hamlet.name = "Hamlet"
hamlet.speak()

barnabas = Piglet() 
barnabas.name = "Barnabas" 
barnabas.speak()


#Example 04 - Since methods are just functions that belong to a specific class, they can work as any other function. So they can receive more parameters and return values if needed. Let's check out what a method returning a value looks like. In this case, we've created a method that converts the age of our piglet to pig years. So the value that the method returns to change when we change the years attribute of our instance. Let's create an instance and check how this method works. Piggy is two-years-old and human years, how old is he and pig years?

class Piglet(): 
    years = 0
    def pig_years(self): 
        return self.years * 18 
    
piggy = Piglet() 
print(piggy.pig_years())    #======> 0

piggy.years = 2 
print(piggy.pig_years())    #======> 36


#Example 05 - OK, now it’s your turn! Have a go at writing methods for a class. Create a Dog class with dog_years based on the Piglet class shown before (one human year is about 7 dog years).

class Dog:
  years = 0
  def dog_years(self):
    return self.years * 7
    
fido=Dog()
fido.years=3
print(fido.dog_years())     #======> 21
