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
        """Adds an item to this Room items list"""
        self.items.append(Item(item[0], item[1]))

    def remove_item(self, item):
        print((ele for ele in self.items if ele.name == item))
        # self.items.remove(x)
