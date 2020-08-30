
#Example 01 - You can create an empty dictionary in a similar way to creating an empty list, except instead of square brackets dictionaries use curly brackets to define their content. Once again, we can use the type function to check that the variable we've just created is a dictionary x = {} type(x). 

x ={}

print(type(x))  #=======> <class 'dict'>


#Example 02 - Declaring a dictionary and displaying it in the terminal.

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}

print(file_counts)

#For a detailed description about Python dictionaries, please refer the notebook drafted by me. 


#Example 03 - The "toc" dictionary represents the table of contents for a book. Fill in the blanks to do the following: 1) Add an entry for Epilogue on page 39. 2) Change the page number for Chapter 3 to 24. 3) Display the new dictionary contents. 4) Display True if there is Chapter 5, False if there isn't.

toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
toc["Epilogue"] = 39 # Epilogue starts on page 39
toc["Chapter 3"] = 24 # Chapter 3 now starts on page 24
print(toc) # What are the current contents of the dictionary?
print("Chapter 5" in toc) # Is there a Chapter 5?


#Example 04 - Iterating over the contents of a dictionary. We will use the for loop like in the previous data structures to iterate through a dictionary in python. Below example will print the extensions(keys) of the dictionary.

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}

for extension in file_counts: 
    print(extension)

''' 
     jpg
     txt
     csv
     py
        '''
        
#So if you use a dictionary in a for loop, the iteration variable will go through the keys in the dictionary. If you want to access the associated values, you can either use the keys as indexes of the dictionary or you can use the items method which returns a tuple for each element in the dictionary.

#The tuple's first element is the key. Its second element is the value. Let's try that with our example dictionary.


#Example 05 - This is the example to the previous explanation.

for ext, amount in file_counts.items(): 
    print("There are {} files with the .{} extension".format(amount, ext))
    
'''
    There are 10 files with the .jpg extension
    There are 14 files with the .txt extension
    There are 2 files with the .csv extension
    There are 23 files with the .py extension
'''

#Sometimes you might just be interested in the keys of a dictionary. Other times you might just want the values. You can access both with their corresponding dictionary methods like this. file_counts.keys() file counts.values().  

print(file_counts.keys())       #======> dict_keys(['jpg', 'txt', 'csv', 'py'])

print(file_counts.values())     #======> dict_values([10, 14, 2, 23])

#These methods return special data types related to the dictionary, but you don't need to worry about what they are exactly. You just need to iterate them as you would with any sequence.

for value in file_counts.values(): 
    print(value)
    
'''
    10
    14
    2
    23
'''

#So we can use items to get key value pairs, keys to get the keys, and values to get just the values.


#Example 06 - Complete the code to iterate through the keys and values of the cool_beasts dictionary. Remember that the items method returns a tuple of key, value for each element in the dictionary.

cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for beast, limb in cool_beasts.items():
    print("{} have {}".format(beast, limb))
    
'''
    octopuses have tentacles
    dolphins have fins
    rhinos have horns
'''


#Example 07 - Because we know that each key can be present only once, dictionaries are a great tool for counting elements and analyzing frequency. Let's check out a simple example of counting how many times each letter appears in a piece of text.

def count_letters(text): 
    result = {}         #We're first initializing an empty dictionary,
    for letter in text:     #Then going through each letter in the given string. 
        if letter not in result: #For each letter, we check if it's not already in the dictionary.
            result[letter]=0    #And in that case, we initialize an entry in the dictionary with a value of zero.
        result[letter] += 1     #Finally, we increment the count for that letter in the dictionary. 
    return result

#To sum up, we've created a dictionary where the keys are each of the letters present in the string and the values are how many times each letter is present.

print(count_letters("aaaaaa"))      #======> dict_keys{'a': 6}

print(count_letters("tenant"))      #======> {'t': 2, 'e': 1, 'n': 2, 'a': 1}

print(count_letters("My name is Chiranthaka Sampath Jayakody"))   #======> {'M': 1, 'y': 3, ' ': 5, 'n': 2, 'a': 8, 'm': 2, 'e': 1, 'i': 2, 's': 1, 'C': 1, 'h': 3, 'r': 1, 't': 2, 'k': 2, 'S': 1, 'p': 1, 'J': 1, 'o': 1, 'd': 1}

#Here you can see how the dictionary can have any number of entries and the pairs of key values always count how many of each letter there are in the string. 

#Also, do you see how our simple code doesn't distinguish between actual letters and special characters like a space?

#To only count the letters, we'd need to specify which characters we're taking into account. This technique might seem simple at first, but it can be really useful in a lot of cases.

#Let's say for example that you're analyzing logs in your server and you want to count how many times each type of error appears in the log file. You could easily do this with a dictionary by using the type of error as the key and then incrementing the associated value each time you come across that error type.

