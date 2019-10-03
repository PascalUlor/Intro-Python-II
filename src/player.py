# Write a class to hold player information, e.g. what room they are in
# currently.
# create a player item and some items to pick up
# then create a room and add the player to the room

# import rooms for composition fields
# from room import Room


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
        return f"Player {self.name} aged {self.age} is in {self.current_room} room"

    def __repr__(self):
        return f"{self.name}, {self.current_room}"


s = Player('Tom', 23, 'Eko')
print(s)
