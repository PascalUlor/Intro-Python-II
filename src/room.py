# Implement a class to hold room information. This should have name and
# description attributes.
# Create a Room class with a name and a contains[] and a method add_item
# Create an Item class with a name and a contains[] that can print contents and pick up item
# from player import Player
class Room:
    # constructor
    def __init__(self, name, description, directions):
        self.name = name
        self.description = description
        self.directions = directions
    # methods
    def __str__(self):
        return f"room {self.name}.\n{self.description} is located in the {self.directions}"

    def __repr__(self):
        return f"{self.name}, {self.description}, {self.directions}"

location = Room('Eko', 'the cafeteria', 'n')

print(location)