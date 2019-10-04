# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item


class Player():
    name = ""
    current_room = ""

    def __init__(self, name, current_room, items=None):
        self.name = name
        self.current_room = current_room
        if items:
            self.items = []
            for item in items:
                self.items.append(Item(item[0], item[1]))
        else:
            self.items = []

    def __repr__(self):
        r = f"(Player({repr(self.name)}, {repr(self.current_room)}))"
        return r

    def add_item(self, item):
        self.items.append(Item(item[0], item[1]))

    def remove_item(self, item):
        for s_item in self.items:
            if s_item.description == item:
                self.items.remove(s_item)
