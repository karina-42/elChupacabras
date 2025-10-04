class Room:
    """
    A class to represent a room of the player's house

    Attributes:
        name (str): The name of the room.
        item (dict or None): A dictionary in the Room object that holds the
            name of the item in the room and how it can be used or None if the
            room has no item.
        connected_rooms (dict): A dictionary of Room objects that are
            connected through cardinal directions. Provides the connections
            for the graph data structure

    Methods:
        has_item(): Checks if the room has an item.
        get_room_status(): Describes the status of the room: its name, whether
            it has an item, the item's name, and how the player can use it.
        remove_item(): Sets an item in the room to None, to represent it being
            removed from the room after the player picks it up.
        add_connection(direction, connecting_room): Adds the connecting rooms
            by the direction they are connected in to the connected_rooms
            dictionary to create the edges of the graph data structure.
    """

    def __init__(self, name, item_dict):
        """
        Constructs the Room object

        :param name: The name of the room.
        :type name: str
        :param item_dict: A dictionary in the Room object that holds the
            name of the item in the room and how it can be used or None if the
            room has no item.
        :type item_dict: dict or None
        """
        self.name = name
        self.item = item_dict
        self.connected_rooms = {}

    def has_item(self):
        """
        Checks if the room has an item.

        :return: True or false
        :rtype: bool
        """
        if self.item is None:
            return False
        else:
            return True

    def get_room_status(self):
        """
        Describes the status of the room: its name, whether it has an item,
        the item's name, and how the player can use it.

        :return: A string telling the player the room doesn't have an item,
        or the item's name and use.
        :rtype: str
        """

        if self.has_item():
            item_message = f"There is a {self.item['item_name']}. You can " \
                           f"use it to {self.item['item_use']}."
        else:
            item_message = f"There are no items in this room."
        return f"{item_message}"

    def remove_item(self):
        """
        Sets an item in the room to None, to represent it being removed from
        the room after the player picks it up.
        """
        self.item = None

    def add_connection(self, direction, connecting_room):
        """
        Adds the connecting rooms by the direction they are connected in to
        the connected_rooms dictionary to create the edges of the graph data
        structure.

        :param direction: The direction the player would move in to get to the
            connecting room
        :type direction: str
        :param connecting_room: The room connected to the current room
        :type connecting_room: Room object
        :return: Nothing
        :rtype: None
        """
        self.connected_rooms[direction] = connecting_room
