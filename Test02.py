def initials(phrase):
    words = phrase.split()      #In this step the string will split to individual words and added to a list named words.
    result = ""                 #Initializing the variable.
    for word in words:
        result += word[0]       #Concatinating the result variablevalue with each element in words list.     
    return result.upper()

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS
