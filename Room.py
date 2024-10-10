###########################################################################################
# Name: Dr. Jean Gourd
# Date: 2023-11-13
# Description: A basic Room class.
###########################################################################################

# the blueprint for a room
class Room:
    # the constructor
    def __init__(self, name):
        # rooms have a name, description, exits (e.g., south), exit locations (e.g., to the south is
        # room n), items (e.g., table), item descriptions (for each item), and grabbables (things that
        # can be taken into inventory)
        self._name = name
        self._description = ""
        self._exits = []
        self._exitLocations = []
        self._items = []
        self._itemDescriptions = []
        self._grabbables = []

    # getters and setters for the instance variables
    def get_name(self):
        return self._name
    def set_name(self, value):
        self._name = value

    def get_description(self):
        return self._description
    def set_description(self, value):
        self._description = value

    def get_exits(self):
        return self._exits
    def set_exits(self, value):
        self._exits = value

    def get_exitLocations(self):
        return self._exitLocations
    def set_exitLocations(self, value):
        self._exitLocations = value

    def get_items(self):
        return self._items
    def set_items(self, value):
        self._items = value

    def get_itemDescriptions(self):
        return self._itemDescriptions
    def set_itemDescriptions(self, value):
        self._itemDescriptions = value

    def get_grabbables(self):
        return self._grabbables
    def set_grabbables(self, value):
        self._grabbables = value


    name = property(get_name, set_name)
    description = property(get_description, set_description)
    exits = property(get_exits, set_exits)
    exitLocations = property(get_exitLocations, set_exitLocations)
    items = property(get_items, set_items)
    itemDescriptions = property(get_itemDescriptions, set_itemDescriptions)
    grabbables = property(get_grabbables, set_grabbables)


    # adds an exit to the room
    # the exit is a string (e.g., north)
    # the room is an instance of a room
    def addExit(self, exit, room):
        # append the exit and room to the appropriate lists
        self._exits.append(exit)
        self._exitLocations.append(room)

    # adds an item to the room
    # the item is a string (e.g., table)
    # the desc is a string that describes the item (e.g., it is made of wood)
    def addItem(self, item, desc):
        # append the item and description to the appropriate lists
        self._items.append(item)
        self._itemDescriptions.append(desc)

    # adds a grabbable item to the room
    # the item is a string (e.g., key)
    def addGrabbable(self, item):
        # append the item to the list
        self._grabbables.append(item)



    # returns a string description of the room as follows:
    #  <name>
    #  <description>
    #  <items>
    #  <exits>
    # e.g.:
    #  Room 1
    #  You look around the room.
    #  You see: chair table 
    #  Exits: east south 
    def __str__(self):
        # first, the room name and description
        s = "{}\n".format(self._name)
        s += "{}\n".format(self._description)


        # next, the items in the room
        s += "You see: "
        for item in self._items:
            s += item + " "
        s += "\n"

        # next, the exits from the room
        s += "Exits: "
        for exit in self._exits:
            s += exit + " "

        return s


