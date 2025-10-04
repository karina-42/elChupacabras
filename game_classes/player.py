class Player:
    """
    A class to represent a player.

    Attributes:
        current_room (Room object): The room the player is currently in.
        inventory (list): Holds the items the player picks up.
        hints_left (int): Counts how many hints the player has left. It is
            decremented by one each time they use a hint.

    Methods:
        get_player_status(): Describes the status of the player: the room they
            are in, their inventory, and how many hints they have left.
        get_item(item): Checks if the item the player wants to pick up is in
            the room. If it is, puts it in their inventory, removes it from the
            room, and returns a string confirming this. If it isn't, returns a
            string to inform the player.
    """

    def __init__(self, first_room, name="TestPlayer"):
        """
        Constructs the player object.

        :param first_room: The room the player is in when the game_classes starts.
        :type first_room: Room
        """
        self.current_room = first_room
        self.inventory = []
        self.hints_left = 3
        self.name = name

    def greet(self):
        return f"{self.name} is working!"

    def get_player_status(self):
        """
        Describes the status of the player: the room they are in, how many
        hints they have left, and their inventory.

        :return: A string with the room the player is currently in, the items
            in their inventory, and how many hints they have left.
        :rtype: str
        """
        room = self.current_room.name
        if len(self.inventory) > 0:
            inventory = ", ".join(self.inventory)
        else:
            inventory = "not picked up any items yet"

        return f"You are in the {room}. You have {inventory}.\nYou have " \
               f"{self.hints_left} hints left."

    def get_item(self, item):
        """
        Checks if the item the player wants to pick up is in the
        room. If it is, puts it in their inventory, removes it from the room,
        and returns a string confirming this. If it isn't, returns a string to
        inform the player.

        :param item: The name of the item the player wants to pick up.
        :type item: str
        :return: A string telling the player they picked up the item or that
            the item is not in the room.
        :rtype: str
        """
        if self.current_room.has_item() and \
                self.current_room.item["item_name"] == item:
            self.inventory.append(item)
            self.current_room.remove_item()
            return f"You picked up a {item}."
        else:
            return "Can't get that item."
