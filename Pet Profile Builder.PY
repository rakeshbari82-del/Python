# 🐾==========================================🐾
#        🐶 PET PROFILE BUILDER 🐱
#    Object-Oriented Programming Project
# 🐾==========================================🐾

class Pet:

    kingdom = "Animal 🐾"

    def __init__(self, name, pet_type, breed, age, color, favourite_food):
        self.name = name
        self.pet_type = pet_type
        self.breed = breed
        self.age = age
        self.color = color
        self.favourite_food = favourite_food

    def show_profile(self):
        print("\n🌟==============================🌟")
        print("🐾 PET PROFILE")
        print("🌟==============================🌟")
        print("🐶 Name           :", self.name)
        print("🐾 Type           :", self.pet_type)
        print("❤️ Breed          :", self.breed)
        print("🎂 Age            :", self.age, "Years")
        print("🎨 Colour         :", self.color)
        print("🍖 Favourite Food :", self.favourite_food)
        print("🌍 Kingdom        :", Pet.kingdom)

    def speak(self):
        if self.pet_type.lower() == "dog":
            print("🐕 Woof Woof!! 🦴")
        elif self.pet_type.lower() == "cat":
            print("🐱 Meow Meow!! 🐟")
        elif self.pet_type.lower() == "parrot":
            print("🦜 Hello Friend!! 🌿")
        elif self.pet_type.lower() == "rabbit":
            print("🐰 Squeak Squeak!! 🥕")
        elif self.pet_type.lower() == "horse":
            print("🐴 Neigh Neigh!! 🌾")
        else:
            print("🐾 Cute Pet Sound!! ❤️")


# ----------------------------
# Creating Objects
# ----------------------------

pet1 = Pet("Bruno", "Dog", "German Shepherd", 4, "Black & Brown", "Chicken 🍗")
pet2 = Pet("Kitty", "Cat", "Persian", 2, "White", "Fish 🐟")
pet3 = Pet("Coco", "Parrot", "Macaw", 3, "Green", "Seeds 🌻")
pet4 = Pet("Snow", "Rabbit", "Dutch Rabbit", 1, "White", "Carrot 🥕")
pet5 = Pet("Thunder", "Horse", "Arabian Horse", 6, "Black", "Grass 🌿")


# ----------------------------
# Display Profiles
# ----------------------------

pet1.show_profile()
pet1.speak()

pet2.show_profile()
pet2.speak()

pet3.show_profile()
pet3.speak()

pet4.show_profile()
pet4.speak()

pet5.show_profile()
pet5.speak()

print("\n🎉 Thank You for Using Pet Profile Builder! 🐾❤️")