# Parent Class
class Animal:
    def make_sound(self):
        raise NotImplementedError("Subclasses must implement this method")


# Child Classes
class Dog(Animal):
    def make_sound(self):
        print("🐶 Woof! Woof!")


class Cat(Animal):
    def make_sound(self):
        print("🐱 Meow!")


class Bird(Animal):
    def make_sound(self):
        print("🐦 Tweet Tweet!")


class Snake(Animal):
    def make_sound(self):
        print("🐍 Hisssss!")


# -----------------------------
# Example Usage (Polymorphism)
# -----------------------------
animals = [Dog(), Cat(), Bird(), Snake()]

for a in animals:
    a.make_sound()  # Each class defines make_sound() differently
