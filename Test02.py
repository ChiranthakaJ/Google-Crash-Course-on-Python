def initials(phrase):
    words = phrase.split()      #In this step the string will split to individual words and added to a list named words.
    result = ""                 #Initializing the variable.
    for word in words:
        result += word[0]       #Concatinating the result variablevalue with each element in words list.     
    return result.upper()

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS


def student_grade(name, grade):
     return ("{name} received {grade}% on the exam".format(name=name, grade=grade))

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))


