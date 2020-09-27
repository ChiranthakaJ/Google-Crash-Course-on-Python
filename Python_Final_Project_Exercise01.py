#Scenario 01
#---------------------------------------------------------------------------------

#Imagine that you're an IT specialist working in a medium-sized company, your manager wants to create a daily report that tracks the use of machines. Specifically, she wants to know which users are currently connected to which machines, it's your job to create the report. 

#In your company, there's a system that collects every event that happens on the machines on the network. Among the many events collected it records each time a user logs in or out of a computer. With this information, we want to write a script that generates a report of which users are logged in to which machines at that time. 

#We need to know what information we'll use as input and what information we'll have as output. 

#We can work this out by looking at the rest of the system where our script will live. 

#n our report scenario, the input is a list of events, each event is an instance of the event class. An event class contains the date when the event happened, the name of the machine where it happened, the user involved, and the event type. In this scenario, we care about the login and logout event type & we need to know exact names of the attributes, otherwise, we won't be able to access them.

#The attributes are called date, user, machine, and type. The event types are strings and the ones we care about are login and logout. With that we should have enough information about the input of our script. 

#The event types are strings and the ones we care about are login and logout.

#With that we should have enough information about the input of our script. Our script will receive a list of event objects and we'll access the events attributes.

#We'll then use that information to know if a user is currently logged into a machine or not. Let's talk about the output. We want to generate a report that lists all the machine names and for each machine, lists of the users that are currently logged in. 

#We then want this information printed on the screen. We've been tasked with generating a report and we can decide exactly how we want that report to look.

#One option would be to print the name of the machine at the beginning of the line and then list the current users on separate lines and indent it to the right, or we could print the machine name followed by a colon and then the usernames separated by commas all in the same line, and we can probably come up with something even more fancy. 

#When formatting a report, it's easy to get caught up in the making it look good part. I've fallen into that trap but what really matters is how well the script solves the problem. So it's better to first focus on making the program work. 

#You can always spend time making the report look nice later. Let's keep it simple for now and we'll go with the approach of printing the machine name followed by all the current users separated by commas. 

#Okay, we now have a pretty good idea of what we need to do. We've identified our problem statement which is we need to process a list of event objects using their date, type, machine, and user attributes to generate a report that lists all users currently logged into the machines. 
 
#We're off to a great start. The next step we're going to do is some research to work out how to best actually do this.

#Okay. So we have our problem statement which helps us understand the problem and focus our approach. We know we have to input a list of event objects and evaluate these objects attributes to output a report of all the users currently logged into a machine. 

#Now it's time for step 2, the research. We're going to consider all the tools we have available to help us solve the problem. To find out which users are currently logged into machines, we need to check when they logged in and when they logged out. 

#If a user logged into a machine and then logged out, they're no longer logged into it. But if they didn't logout out yet, they're still logged in. I know we're stating the obvious here, but in programming, it is super important to be clear on the parameters. 
 
#Also, knowing this tells us that to solve this correctly, it's vital that we process the events in chronological order. If they're not, we can get the logout event before the corresponding login event and our code may do unpredictable things, and no one likes unpredictable code. 

# So how do we sort lists in Python? We'll need to do some research. Type sort lists in Python into your favorite search engine and you'll get a bunch of results that mentioned the list sort method and the sorted function. 

# The difference between these two options is that the sort method modifies the list it's executed on, while the sorted function returns a new list that's been sorted. 

# Apart from that, they work the exact same way. Let's check out this difference in action. First, will create a list of numbers and call the sort method to sort the list.

#You can see here that the elements of the list have been sorted. Let's try a different example now using the sorted function. We'll create a list of names.

#Then we'll print the output of the sorted function.

#Let's print the original list again to check that it didn't change.

#So you can see that the original list wasn't modified. The sorted function returned a new sorted list, but the original was left untouched. Nice, we now know how to sort things in Python. For this problem, it's fine to modify the original list. So we'll use the sort method. 

#But wait, see how both these options sorted the list alphabetically? That's the default approach Python takes. But what if we wanted to organize our lists by different criteria? Again, if we take a look at the documentation we found online, we'll see that the sort method can take a couple of parameters. 

#One of these parameters is called key, and it lets us use a function as the sorting key. Let's try this out on our list of names. Instead of sorting alphabetically, we could sort by the length of each string.
 
# Do you remember which function we can use to do that? Yes, we can pass the len function as the key.

#All right. We now know how to order elements of a list based on the return value of a function. In our report scenario, we know that our elements will be instances of the event class and we want to order by date, which is an attribute of the event class. 

#One way we could do this is to write a function called get_event_date which returns the date stored in the event object. We could also create this as a method in the event class if we had access to modifying the class. 

#But since we're working with a bigger system that generates these events, we will assume that we can't just add a method to the class. So we'll create our own function instead. How does that sound? Isn't all making sense? 

#Remember that there are various paths we could take to solve this problem. But some are better than others. So it's important to understand why we chose the options we did. 

#Feel free to take some time on your own to explore the possibilities and understand what we're doing. In the next video, we will dive into our plan to build our script.

#Okay. You're doing great with this so far. We've already defined our problem statement and then we researched options to figure out what tools we have available and which are best for the job. Now it's time to plan our approach. 

#So we know that our input will be a list of events and we'll sort them by time. Each event in that list will include a machine name, a username, and tell us whether the event is a login or a logout. We want our script to keep track of users as they log in and out of machines. So how can we do this? Let's think about what we'll do for each event and see if we can figure out the best strategy. 

#When we process an event, we'll see that someone interacted with a machine. If it's a login, we want to add it to the group of users logged into that machine. If it's a logout, we want to remove it from the group of users logged into the machine. 

#In this scenario, it makes sense to use a set to store the current users. Adding new users at login time and removing them at logout time. Great. But if the current users of a given machine are stored in a set, how do we know which set corresponds to the machine we're looking for? The easiest way to know this is to store this information in a dictionary. 

#We'll use the name of the machine as the key and the current users of that machine as the value. So for each event we process, we'll first check in the dictionary to see if the machine is already there. We need to check this because it could be the first time we're processing an event for that machine. If it's not there, we'll create a new entry. 

#If it is, we'll update the existing entry with the action corresponding to the event. Which means we either add the user if the event is a login or remove the user if it's a logout. Once we're done processing the events, we'll want to print a report of the information we generated. This is a completely separate task. 

#So it should be a separate function. This function will receive the dictionary regenerated and print the report. It's important to have separate functions; to process the data and to print the data to the screen. This is because if we want to modify how the report is printed, we know we only need to change the function in charge of printing. 

#Or, if we find a bug in our processing the data, we only need to change the processing function. It would also allow us to use the same data processing function to generate a different kind of report, like generating a PDF file, for example. 

#Yay, we know what we need to do, how we need to do it, and how we'll structure our code. Now we can get into the meaty stuff, actually writing the code.

#We're almost done solving our problem. We've written the code that solves our problem statement after following our research and plan. We're now going to put all of our code in a jupyter notebook, execute it and see what happens.

#This is what our code currently looks like as we wrote in the previous video.

'''
def get_event_date(event):
      return event.date

def current_users(events):
  events.sort(key=get_event_date)
  machines = {}
  for event in events:
    if event.machine not in machines:
      machines[event.machine] = set()
    if event.type == "login":
      machines[event.machine].add(event.user)
    elif event.type == "logout":
      machines[event.machine].remove(event.user)
  return machines

def generate_report(machines):
  for machine, users in machines.items():
    if len(users) > 0:
      user_list = ", ".join(users)
      print("{}: {}".format(machine, user_list))
'''

#To check that our code is doing everything it's supposed to do, we need an event class. For this scenario, we'll use the very simple event class.

#No output should be generated from running the custom function definitions above. To check that our code is doing everything it's supposed to do, we need an Event class. The code in the next cell below initializes our Event class. Go ahead and run this cell next.

'''class Event:
    def __init__(self, event_date, event_type, machine_name, user):
     self.date = event_date
     self.type = event_type
     self.machine = machine_name
     self.user = user
'''

#Okay, we have an event class that has a Constructor and sets the necessary attributes. Using this Constructor, we'll create some events and add them to a list, like in the below.

'''
events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'login', 'mailserver.local', 'chris'),
]
'''

#Now we've got a bunch of events. Let's feed these events into our custom_users function and see what happens.

'''
users = current_users(events)
print(users)
'''

'''
{'webserver.local': {'lane'}, 'myworkstation.local': set(), 'mailserver.local': {'chris'}}
'''

#Now try generating the report by running the next cell.
'''
generate_report(users)
'''

'''
webserver.local: lane
mailserver.local: chris
'''

#Okay, we've got a bunch of events. They're currently unsorted, they affect a few machines and include some users. We'll feed these events into our function and see what happens.

#Everything is now ready to go. Drum roll, please. [SOUND] Great, our code correctly created a dictionary with the machine names as Keys. There's one empty set and two sets with one value. Let's now try generating the report.

#Success, our report correctly skipped to the one machine that had an empty set. That's great. In the world of IT, there's a bunch of other things that could happen. What happens if we come across an event for a user logging out that had never logged in?

#Complete Solution. 
#------------------------------------

#Hello, coders! Below we have code similar to what we wrote in the last video. Go ahead and run the following cell that defines our get_event_date, current_users and generate_report methods.

def get_event_date(event):
  return event.date

def current_users(events):
  events.sort(key=get_event_date)
  machines = {}
  for event in events:
    if event.machine not in machines:
      machines[event.machine] = set()
    if event.type == "login":
      machines[event.machine].add(event.user)
    elif event.type == "logout":
      machines[event.machine].remove(event.user)
  return machines

def generate_report(machines):
  for machine, users in machines.items():
    if len(users) > 0:
      user_list = ", ".join(users)
      print("{}: {}".format(machine, user_list))

#No output should be generated from running the custom function definitions above. To check that our code is doing everything it's supposed to do, we need an Event class. The code in the next cell below initializes our Event class. Go ahead and run this cell next.

class Event:
  def __init__(self, event_date, event_type, machine_name, user):
    self.date = event_date
    self.type = event_type
    self.machine = machine_name
    self.user = user
class Event:
  def __init__(self, event_date, event_type, machine_name, user):
    self.date = event_date
    self.type = event_type
    self.machine = machine_name
    self.user = user

#Ok, we have an Event class that has a constructor and sets the necessary attributes. Next let's create some events and add them to a list by running the following cell.

events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'login', 'mailserver.local', 'chris'),
]

#Now we've got a bunch of events. Let's feed these events into our custom_users function and see what happens.

users = current_users(events)
print(users)
users = current_users(events)
print(users)

'''

{'webserver.local': {'lane'}, 'myworkstation.local': set(), 'mailserver.local': {'chris'}}

'''

#Uh oh. The code in the previous cell produces an error message. This is because we have a user in our events list that was logged out of a machine he was not logged into. Do you see which user this is? Make edits to the first cell containing our custom function definitions to see if you can fix this error message. There may be more than one way to do so.

#Remember when you have finished making your edits, rerun that cell as well as the cell that feeds the events list into our custom_users function to see whether the error message has been fixed. Once the error message has been cleared and you have correctly outputted a dictionary with machine names as keys, your custom functions are properly finished. Great!

#Now try generating the report by running the next cell.

generate_report(users)

'''
webserver.local: lane
mailserver.local: chris
'''

#Whoop whoop! Success! The error message has been cleared and the desired output is produced. You are all done with this practice notebook. Way to go!