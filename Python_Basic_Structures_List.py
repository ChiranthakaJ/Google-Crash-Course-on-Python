#Example 01 - Using the "split" string method from the preceding lesson, complete the get_word function to return the {n}th word from a passed sentence. For example, get_word("This is a lesson about lists", 4) should return "lesson", which is the 4th word in this sentence. Hint: remember that list indexes start at 0, not 1.

def get_word(sentence, n):
    	# Only proceed if n is positive 
	if n > 0:
		words = sentence.split()
		# Only proceed if n is not more than the number of words 
		if n <= len(words):
			return(words[n-1])
	return("")

print(get_word("This is a lesson about lists", 4)) # Should print: lesson
print(get_word("This is a lesson about lists", -4)) # Nothing
print(get_word("Now we are cooking!", 1)) # Should print: Now
print(get_word("Now we are cooking!", 5)) # Nothing


#Example 06 - Let's use tuples to store information about a file: its name, its type and its size in bytes. Fill in the gaps in this code to return the size in kilobytes (a kilobyte is 1024 bytes) up to 2 decimal places.

def file_size(file_info):
    name, type, file_size= file_info
    return("{:.2f}".format(file_size / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21


#Example 07 - An example of tuples.

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours *3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

result = convert_seconds(5000)

print(convert_seconds(5000))   #====> (1, 23, 20)
print(type(result))   #The answer gives as a Tuple and we can get ot confirmed like below.


#Example 08 - Iterating over a List.

animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
chars = 0
for animal in animals: 		#In this function it will go through the list for counting the no of characters of each element.
    chars += len(animal)    #Calculate the no of characters of each element and calculate the total no of characters.

print("Total characters: {}, Average length: {}".format(chars, chars/len(animals)))		#Calculate the average no of characters and print with the total no of characters. In here len() used to calculate the total no of elements in the list.


#Example 09 -  Identifying the index of an element going through the list using the enumerate() function.

winners = ["Ashley", "Dylan", "Reese"]
for index, person in enumerate(winners): 
    print("{} - {}".format(index + 1, person))

'''
	1 - Ashley
	2 - Dylan
	3 - Reese
'''


#Example 10 - Try out the enumerate function for yourself in this quick exercise. Complete the skip_elements function to return every other element from the list, this time using the enumerate function to check if an element is on an even position or an odd position.

def skip_elements(elements):
    list=[]
    for index,element in enumerate(elements):
        if index%2==0:
            list.append('{}'.format(element))
    return list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']


