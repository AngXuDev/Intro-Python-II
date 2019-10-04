from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons",
                     [("knife", "a knife"), ("soda", "a bottle of soda"), ("pigeon", "a pigeon")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east.""",
                     [("club", "a club"), ("water", "a bottle of water")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""",
                     [("bow", "a bow"), ("berries", "a handful of berries")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air.""",
                     [("gold coins", "a bag of gold coins"), ("meat", "a hunk of meat")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.""",
                     [("grail", "a grail"), ("note", "a handwritten note")]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# Create new player
player = Player("Jack", room["outside"])

# Define current room, initialize empty items list and room items string
current = player.current_room
items_list = []
room_items = ""

current.add_item(("ball", "a ball"))
current.remove_item("pigeon")

# Helper function to update items list for a room and the string to print room items in terminal


def updateItems(current):
    global room_items
    items_list = []
    room_items = ""
    for tup in current.items:
        items_list.append(tup.description)
    room_items = ", ".join(items_list[:-1]) + ' and ' + items_list[-1]
    room_items = room_items[0].upper() + room_items[1:]


# Initial update of items in the room
updateItems(current)

# Initial description of room
print(
    f"You are currently at {current.name}. {current.description}. {room_items} is laying around")

# Initial input prompt
command = input("Enter a command (n, e, s, w, or q): ")

# Start while loop, as long as q is not entered to quit, continue the loop
while command != 'q':
    # If a direction is entered use control flow to move player
    if (command in ['n', 'e', 's', 'w']):
        # If valid direction is entered, check for route existence
        dir_attr = f"{command}_to"
        if hasattr(current, dir_attr):
            # If route exists, update current room and room items and print
            current = getattr(current, dir_attr)
            updateItems(current)
            print(
                f"You are currently at {current.name}. {current.description}. {room_items} is laying around")
        # If route does not exist, print error message
        else:
            print(f"There is nothing in that direction.")
    # If a different command is entered let player know the command is not valid
    else:
        print(f"Please enter a valid command (n, e, s, w, or q).")
    # Re-prompt after each while loop
    command = input("Enter a command (n, e, s, w, or q): ")
# If q is entered, print farewell message
if (command == 'q'):
    print(f"Farewell traveler")

# while True:
#   try:
#     command = input("Enter a command (n, e, s, w, or q): ")
#   except
