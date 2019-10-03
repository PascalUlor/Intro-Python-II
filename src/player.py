# Write a class to hold player information, e.g. what room they are in
# currently.
# create a player item and some items to pick up
# then create a room and add the player to the room

# import rooms for composition fields
from room import Room


class Player:
    def __init__(self, name, age, current_room):
        self.name = name
        self.age = age
        self.current_room = current_room

        # methods

        # getters
    def get_name(self):
        return self.name

        # setters
    def set_name(self, name):
        self.name = name

    def __str__(self):
        output = ""
        output += self.name + "\n" + "age" + self.age
        i = 1
        for c in self.current_room:
            output += "  " + str(i) + ". " + c.name + "\n"
            i += 1

        # add an exit message
        output += "  " + str(i) + ". Exit"
        return output


s = Player('Player 1', 'Eko', [Room('Big Apple', 'NYC', 'n'), Room(
    'Gold Coast', 'Ghana', 's'), Room('Safari', 'SA', 'e'), Room('Naija', 'Nigeria', 'w')])
