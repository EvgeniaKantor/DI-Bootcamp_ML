class AnagramChecker:
    def __init__(self, file_path = 'D:\DI-Bootcamp_ML\Week2\Day5\ExercisesXP\sowpods.txt'):
#load text file into a variable
        
        with open(file_path, encoding = 'utf-8') as f:
            self.word_list = set(word.strip().upper() for word in f)

# should check if the given word (ie. the word of the user) is a valid word.
    def is_valid_word(self, word):
        return word.upper() in self.word_list

# Checks if two given words are anagrams of each other
    def is_anagram(self, word1, word2):
        return sorted(word1.upper()) == sorted(word2.upper())
    
    def get_anagrams(self, word):
        word = word.upper()
        return [w for w in self.word_list if self.is_anagram(word, w) and w != word]

# Example usage
checker = AnagramChecker()

word = input('Enter a word: ').strip().upper()

while not checker.is_valid_word(word):
    word = input('Invalid word! Enter another word: ').strip().upper()

anagrams = checker.get_anagrams(word)
print("this is a valid English word.")
print(f"Anagrams of '{word}': {anagrams}")
            