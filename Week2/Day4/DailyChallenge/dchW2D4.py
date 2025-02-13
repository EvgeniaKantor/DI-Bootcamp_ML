import string
from collections import Counter
import os
import requests
# First, we will analyze a simple string, like “A good book would sometimes cost as much as a good house.”

# Create a class called Text that takes a string as an argument and store the text in a attribute.
# Hint: You need to manually copy-paste the text, straight into the code

class Text:
    def __init__(self, string_text):
        self.string_text = string_text.translate(str.maketrans('', '', string.punctuation))
        self.words = self.string_text.lower().split()

# Implement the following methods:
# a method to return the frequency of a word in the text 
# (assume words are separated by whitespace) return None or a meaningful message.

    def frequency_word(self, word):
        word_count = self.words.count(word)
        if word_count == 0:
            return None
        return word_count
        
# a method that returns the most common word in the text.
    def most_common_word(self):
        word_counts = Counter(self.words)
        if word_counts:
            return word_counts.most_common(1)[0]
        return None

# a method that returns a list of all the unique words in the text.
    def unique_words(self):
        return list(set(self.words))
    
# text = Text("A good book would sometimes cost as much as a good house.")
# print(f"Frequency of {'good'}:", text.frequency_word("good"))
# print("Most common word:", text.most_common_word())
# print("Unique words:", text.unique_words())

# Then, we will analyze a text coming from an external text file. Download the_stranger.txt file.

# Implement a classmethod that returns a Text instance but with a text file:

#     >>> Text.from_file('the_stranger.txt')
# Hint: You need to open and read the text from the text file.
    @classmethod
    def from_file(cls, filename):
        with open(filename, 'r') as file:
            text = file.read()
        return cls(text)


save_path = 'd:/DI-Bootcamp_ML/Week2/Day4/DailyChallenge/the_stranger.txt'

# Now, use the provided the_stranger.txt file and try using the class you created above.
# Read the file using the from_file class method
text_instance = Text.from_file(save_path)

print("Frequency of 'good':", text_instance.frequency_word("good"))
print("Most common word:", text_instance.most_common_word())
print("Unique words:", text_instance.unique_words())