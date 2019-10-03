# Implement a class to hold room information. This should have name and
# description attributes.
# Create a Room class with a name and a contains[] and a method add_item
# Create an Item class with a name and a contains[] that can print contents and pick up item
# from player import Player

class Room:
    # constructor
    def __init__(self, name, description, directions, items):
        self.name = name
        self.description = description
        self.directions = directions
        self.items = items
    # methods
    def add_item(self, item):
        self.items.append(item)

    def __str__(self):
        return f"room {self.name}.\n{self.description} is located in the {self.directions} theres a {self.items} inside"

    def __repr__(self):
        return f"{self.name}, {self.description}, {self.directions}"

location = Room('Eko', 'the cafeteria', 'n', 'guitar')
print(location)
