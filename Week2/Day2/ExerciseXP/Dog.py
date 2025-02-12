# Create a class called Dog with the following attributes name, age, weight
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

# Implement the following methods in the Dog class:
# bark: returns a string which states: “<dog_name> is barking”    
    def bark(self):
        print(f"{self.name} is barking")

# run_speed: returns the dogs running speed (weight/age*10)
    def run_speed(self):
        return round(self.weight / self.age * 10, 2)

# fight : takes a parameter which value is another Dog instance, 
# called other_dog. This method returns a string stating which dog won the fight. 
# The winner should be the dog with the higher run_speed x weight.

    def fight(self, other_dog):
        self_score = self.run_speed() * self.weight
        other_score = other_dog.run_speed() * other_dog.weight
        
        if self_score > other_score:
            return f'{self.name} won the fight!'
        elif self_score < other_score:
            return f"{other_dog.name} won the fight!"
        else:
            return "It's a tie!"
        
# Create 3 dogs and run them through your class
dog1 = Dog('Max', 2, 50)
dog2 = Dog('Nip', 5, 19)
dog3 = Dog('Jack', 18, 70)

all_dogs = [dog1, dog2, dog3]
for dog in all_dogs:
    dog.bark()
    print(f"{dog.name}'s speed: {dog.run_speed()} km/h")

print(dog1.fight(dog2))
print(dog2.fight(dog3))
print(dog3.fight(dog1))