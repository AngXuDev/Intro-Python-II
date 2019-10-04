# Implement a class to hold room information. This should have name and
# description attributes.

from item import Item


class Room():
    name = ""
    description = ""

    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        if items:
            self.items = []
            for item in items:
                self.items.append(Item(item[0], item[1]))
        else:
            self.items = []

    def __repr__(self):
        r = f"(Room({repr(self.name)}, {repr(self.description)}))"
        return r

    def add_item(self, item):
        self.items.append(Item(item[0], item[1]))

    def remove_item(self, item):
        for s_item in self.items:
            if s_item.description == item:
                self.items.remove(s_item)
