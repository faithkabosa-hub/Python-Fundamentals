
class Dog:

    def __init__(self, breed, age, color):
         self.breed = breed
         self.age = age
         self.color = color

    def speak(self):
        print("Dog is barking")

dog1 = Dog("German Shepherd", 3, "White")
print(dog1.breed)
print(dog1.age)
print(dog1.color)

print()

dog2 = Dog("Chihuahua", 5, "Brown")
print(dog2.breed)
print(dog2.age)
print(dog2.color)

print()

dog3 = Dog("Siberian Husky", 7, "Black")
print(dog3.breed)
print(dog3.age)
print(dog3.color)

