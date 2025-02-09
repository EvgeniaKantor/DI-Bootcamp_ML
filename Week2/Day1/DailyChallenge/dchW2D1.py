# Take a look at the following code and output:
# File: market.py

# macdonald = Farm("McDonald")
# macdonald.add_animal('cow',5)
# macdonald.add_animal('sheep')
# macdonald.add_animal('sheep')
# macdonald.add_animal('goat', 12)
# print(macdonald.get_info())

# Output

# McDonald's farm

# cow : 5
# sheep : 2
# goat : 12

#     E-I-E-I-0!


# Create the code that is needed to receive the result provided above. Below are a few questions to assist you with your code:

# Create a class called Farm. How should it be implemented?
# Does the Farm class need an __init__ method? If so, what parameters should it take?
# How many methods does the Farm class need?
# Do you notice anything interesting about the way we are calling the add_animal method? What parameters should this function have? How many…?
# Test your code and make sure you get the same results as the example above.
# Bonus: nicely line the text in columns as seen in the example above. Use string formatting.

class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = {}
    
    def add_animal(self, animal, quantaty=1):
        if animal in self.animals:
            self.animals[animal] += quantaty
        else:
            self.animals[animal] = quantaty

    def get_info(self):
        info = f"{self.name}'s farm\n"
        for k, v in self.animals.items():
            info += f"{k} : {v}\n"
        return info + "\n  E-I-E-I-O"

# Add a method called get_animal_types to the Farm class. 
# This method should return a sorted list of all the animal types (names) in the farm. 
# With the example above, the list should be: ['cow', 'goat', 'sheep']
    def get_animal_types(self):
        return sorted(self.animals.keys())
    
# Add another method to the Farm class called get_short_info. 
# This method should return the following string: “McDonald’s farm has cows, goats and sheeps.”. 
# The method should call the get_animal_types function to get a list of the animals
    def get_short_info(self):
        animal_types = self.get_animal_types()  
        formatted_animals = []
        for animal in animal_types:
            if self.animals[animal] > 1:
                formatted_animals.append(animal + "s")
            else:
                formatted_animals.append(animal)

        if len(formatted_animals) == 1:
            animal_str = formatted_animals[0]
        else:
            animal_str = ", ".join(formatted_animals[:-1]) + f" and {formatted_animals[-1]}"

        return f"{self.name}'s farm has {animal_str}."

macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print(macdonald.get_animal_types())
print(macdonald.get_short_info())