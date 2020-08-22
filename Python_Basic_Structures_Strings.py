#Exercise 01 - Modify the double_word function so that it returns the same word repeated twice, followed by the length of the new doubled word. For example, double_word("hello") should return hellohello10.

def double_word(word):
    return (word+word+str(len(word+word)))

print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0


#Exercise 02 - Modify the first_and_last function so that it returns True if the first letter of the string is the same as the last letter of the string, False if they’re different. Remember that you can access characters using message[0] or message[-1]. Be careful how you handle the empty string, which should return True since nothing is equal to nothing.

def first_and_last(message):
    if not message or message[0] == message[len(message)-1]:
     return True
    else:
     return False 

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))


#Exercise 03 - Checking of the user answered yes to a question. We will use lower() to convert the given answer, so that if the user has given the answer as YES or Yes or yES or in any other formality, it won't affect the final result.

answer = input("Please input the answer...")

if answer.lower() == "yes": 
    print("The answer is yes")
else: 
    print("The answer is not yes")
    

#Exercise 04 - To remove the whitespaces surrounding a given string or a substring, we can use the strip() method. This method also removes tab spaces, new line characters and any similar characters to a space or spaces.

answer = input("Please input the answer...")

newAnswer = answer.strip()

if answer.lower() == "yes": 
    print("The answer is yes")
else: 
    print("The answer is not yes")
    
    #There are 2 other versions of this strip() method. The lstrip() method will strip the whitespaces left to the substring and rstrip() will strip the whitespaces right to the substring.
    
#Exercise 05 - The count() method will count the no of occurances of a substring in a given string.

answer = input("Pleas insert the text....")

print(answer.count("a"))

    #This count() method will count the no of occurances that matches the exact substring. Not the same substring with any dirrerent formalities.
    
    
#Exercise 06 - The endswith() will check whether a certain string contains a substring. The answer is a boolean value.

print("Forest".endswith("rest"))  #===> Result is 'True'.


#Exercise 06 - The isnumeric() method will check whether a certain string or substring is made up with numbers. The answer is a boolean value.

print("Forest".isnumeric())

print("123456".isnumeric())
    

