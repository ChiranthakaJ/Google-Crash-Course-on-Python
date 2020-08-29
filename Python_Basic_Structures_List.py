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

#The enumerate() function returns a tuple for each element in the list. The first value of the tuple is the index of the element in the sequence. The second value in the tuple is the element in the sequence.


#Example 11 - You have a list of tuples containing two strings each. The first string is an email and the second is the full name of the person with that email address. You need to write a function that creates a new list containing one string per person including their name abd the email address between abgled brackets.The format usually used in emails like this.

#We'll start by defining a function that receives a list of people, def full_emails, takes the argument people.
def full_emails(people):
     
    #Remember, people is a list of tuples where the first element is the email address and the second one is the full name.  So in our function, we'll first create the variable that we'll use as a return value which will be a list and we'll call it result. Result equals empty list.
    result = []
    
    #We'll then iterate over the list of people. We know this list contains tuples of two strings each. So we'll unpack the values directly when iterating in variables that we'll call email and name for email and name in people.
    for email, name in people: 
        
        #Now, our result variable is a list and it should contain strings. So we'll append to the resulting string to the results list, result.append. 
        result.append("{} <{}>".format(name, email))
        #The string that will append will be formatted in the way we want. To do that, we'll use the format method with the two variables of our iteration. So curly brackets, curly brackets.format, name, and email.
    
    #Once we're done with the iteration, we'll return the list which should now contain all the necessary emails, return result.
    return result 

print(full_emails([("alex@example.com", "Alex Diego"), ("shay@example.com", "Shay Brandt")]))


#You can create lists from sequences using a for loop, but there’s a more streamlined way to do this: list comprehension. List comprehensions allow you to create a new list from a sequence or a range in a single line.

#For example, [ x*2 for x in range(1,11) ] is a simple list comprehension. This would iterate over the range 1 to 10, and multiply each element in the range by 2. This would result in a list of the multiples of 2, from 2 to 20.

#Example 12 - List comprehensions vs generic list iterating

#------ Generic List Iteration ------

multiples = []
for x in range(1,11):
    multiples.append(x*7)

print(multiples) #=====> [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]

#------ List comprehensions used list iteration ------

multiples = [ x * 7 for x in range(1,11)]

print(multiples)


#Example 13 -  List comprehensions also let us use a conditional clause. Say we wanted all the numbers that are divisible by 3 between 0 and a 100, we could create a list like the below.

z = [x for x in range(1, 101) if x%3 ==0]
print(z)        #===== [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, ........ 90, 93, 96, 99]


#Example 14 - The odd_numbers function returns a list of odd numbers between 1 and n, inclusively. Fill in the blanks in the function, using list comprehension. Hint: remember that list and range counters start at 0 and end at the limit minus 1.

def odd_numbers(n):
    	return [x for x in range(1, n+1) if x % 2 != 0]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []
