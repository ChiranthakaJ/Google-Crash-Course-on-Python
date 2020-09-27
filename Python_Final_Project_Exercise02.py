#You're about to start the final project of the course. Amazing job making it all the way here. I hope you've been having as much fun as I have on this journey. 

#We're going to be working on our final project using Jupyter notebooks. You might be starting to feel pretty confident using them. But remember if you have any issues you can always ask for help in the discussion forums. 

#Okay, before we dive in, we're going to chat a little bit about what you'll be doing for the project, it's going to be really fun. The goal of the project is to create a word cloud. A word cloud is an image that's made up of different sized words. 

#Usually the sizes of the words are determined by how many times each word appears in a specific text. To create the image itself, we're going to use an external Python module called creatively Word cloud. [LAUGH] Your job is to create a script that would go through the text and count how many times each word appears. 

#We've done this a few times already, any ideas how we should tackle this one? If you're thinking of using a dictionary to count how many times each word appears, then. Ding ding ding, good answer! You're going to prepare a dictionary and use that as a parameter for the word cloud module, not too tricky, right? I think you can handle a little more, so two things you have to watch out for. 

#One, punctuation marks, before counting the frequency of the words, you need to make sure that there are no punctuation marks in the text. If you don't, a string example with a comma at the end would be different from a string example with a dot at the end. So before you put words into the dictionary, you have to clean up the text to remove any punctuation marks. 

#And the second thing we want to keep our word cloud interesting. Certain words in our language crop up a lot and if we include all of these we're going to get a pretty dull word cloud. Think about words like, the, two or if. They usually appear a whole lot in text but aren't too relevant to the text's overall message. 

#We want our Cloud to show words that are relevant to the text we're using for the input. So you need to find a way to exclude irrelevant or uninteresting words when processing the text. For the input, you're going to upload a text file. You can choose any text file you like for your input. 

#It could be the contents of a website, a full novel or even everything that one author has ever written. You just need to make sure that it's one text file, so that it can be processed by the code. Okay, before jumping into the project, remember you can re-watch this video If something isn't clear. 

#Yep, I'm starting to sound like a broken record, but this time it's extra extra important. This final project is the real test of how much you've gotten your head around and can highlight areas you need to brush up on. So we want you to be super clear on what you need to do on that point. 

#You'll find an overview of what you have to do in the next reading. Can you guess the best way of tackling this problem? Yep, you got it, our step-by-step approach that we outlined earlier. 

#Understand the problem statement, research available options, plan your approach, write your code and finally execute. Okay, feeling good? Ready to go? Remember, you know this stuff and you've totally got it.

#scenario
#------------------------------------------

#Create a dictionary with words and word frequencies that can be passed to the generate_from_frequencies function of the WordCloud class.

#Once you have the dictionary, use this code to generate the word cloud image:

'''
cloud = wordcloud.WordCloud()
cloud.generate_from_frequencies(frequencies)
cloud.to_file("myfile.jpg")
'''

#Things to remember 
#-------------------------------------

#Before processing any text, you need to remove all the punctuation marks. To do this, you can go through each line of text, character-by-character, using the isalpha() method. This will check whether or not the character is a letter.  

#To split a line of text into words, you can use the split() method.

#Before storing words in the frequency dictionary, check if they’re part of the "uninteresting" set of words (for example: "a", "the", "to", "if"). Make this set a parameter to your function so that you can change it if necessary.

#Input file
#---------------------------------

#For the input file, you need to provide a file that contains text only. For the text itself, you can copy and paste the contents of a website you like. Or you can use a site like Project Gutenberg to find books that are available online. You could see what word clouds you can get from famous books, like a Shakespeare play or a novel by Jane Austen.

#For this project, you'll create a "word cloud" from a text by writing a script. This script needs to process the text, remove punctuation, ignore case and words that do not contain all alphabets, count the frequencies, and ignore uninteresting or irrelevant words. A dictionary is the output of the calculate_frequencies function. The wordcloud module will then generate the image from your dictionary.

#For the input text of your script, you will need to provide a file that contains text only. For the text itself, you can copy and paste the contents of a website you like. Or you can use a site like Project Gutenberg to find books that are available online. You could see what word clouds you can get from famous books, like a Shakespeare play or a novel by Jane Austen. Save this as a .txt file somewhere on your computer.

#Now you will need to upload your input file here so that your script will be able to process it. To do the upload, you will need an uploader widget. Run the following cell to perform all the installs and imports for your word cloud script and uploader widget. It may take a minute for all of this to run and there will be a lot of output messages. But, be patient. Once you get the following final line of output, the code is done executing. Then you can continue on with the rest of the instructions for this notebook.

#Here are all the installs and imports you will need for your word cloud script and uploader widget

'''
!pip install wordcloud
!pip install fileupload
!pip install ipywidgets
!jupyter nbextension install --py --user fileupload
!jupyter nbextension enable --py fileupload
'''

'''
import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys
'''

#Whew! That was a lot. All of the installs and imports for your word cloud script and uploader widget have been completed.

#IMPORTANT! If this was your first time running the above cell containing the installs and imports, you will need save this notebook now. Then under the File menu above, select Close and Halt. When the notebook has completely shut down, reopen it. This is the only way the necessary changes will take affect.

#To upload your text file, run the following cell that contains all the code for a custom uploader widget. Once you run this cell, a "Browse" button should appear below it. Click this button and navigate the window to locate your saved text file.

#This is the uploader widget
'''
def _upload():

    _upload_widget = fileupload.FileUploadWidget()

    def _cb(change):
        global file_contents
        decoded = io.StringIO(change['owner'].data.decode('utf-8'))
        filename = change['owner'].filename
        print('Uploaded `{}` ({:.2f} kB)'.format(
            filename, len(decoded.read()) / 2 **10))
        file_contents = decoded.getvalue()

    _upload_widget.observe(_cb, names='data')
    display(_upload_widget)

_upload()
'''

#The uploader widget saved the contents of your uploaded file into a string object named file_contents that your word cloud script can process. This was a lot of preliminary work, but you are now ready to begin your script.

#Write a function in the cell below that iterates through the words in file_contents, removes punctuation, and counts the frequency of each word. Oh, and be sure to make it ignore word case, words that do not contain all alphabets and boring words like "and" or "the". Then use it in the generate_from_frequencies function to generate your very own word cloud!

#Hint: Try storing the results of your iteration in a dictionary before passing them into wordcloud via the generate_from_frequencies function.

#def calculate_frequencies(file_contents):
#Here is a list of punctuations and uninteresting words you can use to process your text

#punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
#"we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
#"their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
#"have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
#"all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]'''

#LEARNER CODE START HERE
#Each word is splitted below and formed a list named "words":
    
'''
words = file_contents.split(" ")
    
words_list = []
'''
    
#All the uninteresting words are ignored to form a new list of words below:
'''
for word in words:
    for uninteresting_word in uninteresting_words:
        if word is not uninteresting_word:
            words_list.append(word)
'''              
#Punctuation marks are removed below:
'''   
for word in words_list:
        if not word.isalpha():
            word = ''.join([letter for letter in word if word.isalpha()])
            
    words_dict = {}
'''
    
#The frequency of words of words are assigned as the values of the keys in the words dictionary named as "words_dict":
'''
for word in words_list:
        if word not in words_dict.keys():
            words_dict[word] = words_list.count(word)
'''           
#wordcloud
'''
cloud = wordcloud.WordCloud()
cloud.generate_from_frequencies(words_dict)
return cloud.to_array()
'''

#If you have done everything correctly, your word cloud image should appear after running the cell below. Fingers crossed!

'''
myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show() 
'''