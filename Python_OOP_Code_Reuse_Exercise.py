#Exercise 01
#--------------------------------------------

#First, let’s look back at inheritance. Run the following cell that defines a generic Animal class.

class Animal: 
    name =""
    category = ""
    
    def __init__(self, name): 
        self.name = name
    
    def set_Category(self, category): 
        self.category = category
        
#In the next cell, define a Turtle class that inherits from the Animal class. Then go ahead and set its category.
    
class Turtle(Animal): 
    category="reptile"
        
print(Turtle.category)  #=====> reptile
    
#Next, let’s practice composition a little bit. This one will require a second type of Animal that is in the same category as the first. For example, since you already created a Turtle class, go ahead and create a Snake class. Don’t forget that it also inherits from the Animal class and that its category should be set to reptile.
    
class Snake(Animal): 
    category = "reptile"
        
#Now, let’s say we have a large variety of Animals (such as turtles and snakes) in a Zoo. Below we have the Zoo class. We’re going to use it to organize our various Animals. Remember, inheritance says a Turtle is an Animal, but a Zoo is not an Animal and an Animal is not a Zoo -- though they are related to one another.
    
#Fill in the blanks of the Zoo class below so that you can use zoo.add_animal( ) to add instances of the Animal subclasses you created above. Once you’ve added them all, you should be able to use zoo.total_of_category( ) to tell you exactly how many individual Animal types the Zoo has for each category! Be sure to run the cell once you've finished your edits.
    
class Zoo: 
    def __init__(self): 
        self.current_animals = {} 
        
    def add_animal(self, animal): 
        self.current_animals[animal.name] = animal.category
        
    def total_of_category(self, category): 
        result = 0
        for animal in self.current_animals.values(): 
            if animal == category: 
                result += 1
            
        return result
    
zoo = Zoo()
    
#Run the following cell to check whether you properly filled in the blanks of your Zoo class.
    
turtle = Turtle("Turtle") #create an instance of the Turtle class
snake = Snake("Snake") #create an instance of the Snake class

zoo.add_animal(turtle)
zoo.add_animal(snake)

print(zoo.total_of_category("reptile")) #how many zoo animal types in the reptile category

'''
2
'''


#Exercise 02
#--------------------------------------------

#In this exercise, we'll create a few classes to simulate a server that's taking connections from the outside and then a load balancer that ensures that there are enough servers to serve those connections.

#To represent the servers that are taking care of the connections, we'll use a Server class. Each connection is represented by an id, that could, for example, be the IP address of the computer connecting to the server. For our simulation, each connection creates a random amount of load in the server, between 1 and 10.

#Begin Portion 1#
import random

class Server:
    def __init__(self):
        """Creates a new server instance, with no active connections."""
        self.connections = {}

    def add_connection(self, connection_id):
        """Adds a new connection to this server."""
        connection_load = random.random()*10+1
        # Add the connection to the dictionary with the calculated load
        self.connections[connection_id] = connection_load
    def close_connection(self, connection_id):
        """Closes a connection on this server."""
        # Remove the connection from the dictionary
        if connection_id in self.connections:
            del self.connections[connection_id]
    def load(self):
        """Calculates the current load for all connections."""
        total = 0
        for load in self.connections.values():
            total += load
        # Add up the load for each of the connections
        return total

    def __str__(self):
        """Returns a string with the current load of the server"""
        return "{:.2f}%".format(self.load())
    
#End Portion 1#

#Now run the following cell to create a Server instance and add a connection to it, then check the load:

server = Server()
server.add_connection("192.168.1.1")

print(server.load())

'''
0
'''

#After running the above code cell, if you get a NameError message, be sure to run the Server class definition code block first.

#The output should be 0. This is because some things are missing from the Server class. So, you'll need to go back and fill in the blanks to make it behave properly.

#Go back to the Server class definition and fill in the missing parts for the add_connection and load methods to make the cell above print a number different than zero. As the load is calculated randomly, this number should be different each time the code is executed.

#Hint: Recall that you can iterate through the values of your connections dictionary just as you would any sequence.