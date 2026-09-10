class Animal:
    zoo_name = "My Zoo"
    
    def __init__(self, name, species, age, sound):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound
        
    def make_sound(self):
        print(self.sound)
        
    def info(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        print(f"Age: {self.age}")
        print(f"Zoo: {Animal.zoo_name}")
        
    def __str__(self):
        return f"Name: {self.name} | Species: {self.species} | Age: {self.age}"
        
class Bird(Animal):
    def __init__(self, name, species, age, sound, wing_span):
        super().__init__(name, species, age, sound)
        self.wing_span = wing_span
        
    def make_sound(self):
        print(f"Bird sound: {self.sound}")
        
lion = Animal("Leo", "Lion", 5, "Roar")
print(lion)
lion.info()
lion.make_sound()

print()

parrot = Bird("Willie", "Parrot", 2, "Squawk", 45)

print(parrot)
parrot.info()
parrot.make_sound()
print(f"Wing span: {parrot.wing_span}")