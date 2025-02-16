# It should do the following:
# Show a menu, offering the user to input a word or exit. Keep showing the menu until the user chooses to exit.

# If the user chooses to input a word, it must be accepted from the user’s keyboard input, and then be validated:
# Only a single word is allowed. If the user typed more than one word, show an error message. (Hint: how do we know how many words were typed?)
# Only alphabetic characters are allowed. No numbers or special characters.
# Whitespace should be removed from the start and end of the user’s input.

# Once your code has decided that the user’s input is valid, it should find out the following:
# All possible anagrams to the user’s word.
# Create an AnagramChecker instance and apply it to the steps created above.
# Display the information about the word in a user-friendly, nicely-formatted message such as:


# YOUR WORD :”MEAT”
# this is a valid English word.
# Anagrams for your word: mate, tame, team.

from anagram_checker import AnagramChecker

class Anagrams(AnagramChecker):
    def __init__(self, file_path):
        super().__init__(file_path)

    def show_menu(self):
         while True:
            print("\n--- Anagram Checker ---")
            print("1. Input a word")
            print("2. Exit")
            
            choice = input("Enter your choice (1 or 2): ").strip()
            if choice not in ['1', '2']:
                print("Invalid choice. Please enter 1 to input a word or 2 to exit.")
                continue  # Prompt again
            
            if choice == '1':
                word = input('Enter a word: ').strip()
                
                if len(word.split()) > 1:
                    print("Error: Please enter only one word.")
                    continue  # Ask again
                
                if not word.isalpha():
                    print("Error: The word should only contain alphabetic characters.")
                    continue  
                
                word = word.upper()  
            
                if not self.is_valid_word(word):
                    print(f"'{word}' is not a valid English word.")
                else:
                    print(f"'{word}' is a valid English word.")
                    
                    anagrams = self.get_anagrams(word)
                    if anagrams:
                        print(f"Anagrams for '{word}': {', '.join(anagrams)}")
                    else:
                        print(f"No anagrams found for '{word}'.")
            
            elif choice == '2':
                print("Exiting the program. Goodbye!")
                break  # Exit the loop and program


if __name__ == "__main__":
    anagram_ui = Anagrams('D:\DI-Bootcamp_ML\Week2\Day5\ExercisesXP\sowpods.txt')  
    anagram_ui.show_menu()


    
