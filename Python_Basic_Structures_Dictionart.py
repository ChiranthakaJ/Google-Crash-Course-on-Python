
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