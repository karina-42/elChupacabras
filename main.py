from website import create_app

app = create_app()

# Code by Angela Karina Vegega Ortiz
# Enhancement Two - September 28, 2025.
# Refactored the Rooms dictionary into a graph data structure connected by
# rooms and the direction they are connected in. Used a breadth-first search
# (BFS) algorithm to create a hints function so players can get hints in the
# form of cardinal directions to the closest room with an item from their
# current room. Players can use hints up to three times.
#
# This is a text based adventure game called A Visit from El Chupacabras.
# Users must type commands to progress the story. Their commands must start
# with 'go' or 'get'. The goal is to move from room to room collecting items
# before reaching the Chupacabras. If the player collected all the items,
# they win the game. Whether they win or lose, they can choose to start
# a new game.
#
# I used articles by Lavasani (2023) and Rodriguez (2019) to research and
# adapt the Factory pattern for creating rooms.
# I used articles on GeeksforGeeks (2025), w3schools (W3Schools.com, n.d.),
# Code Signal (“Finding the Shortest Path in Graphs With BFS Algorithm,” n.d.),
# and StackOverflow (Python - Create a Graph From a Dictionary, 2019), to
# guide me in creating the graph data structure and using BFS algorithm to
# find the shortest path for the hint functionality.
#
# References:
# Finding the shortest path in graphs with BFS algorithm. (n.d.).
#   CodeSignal.
#   https://codesignal.com/learn/courses/mastering-graphs-in-python/lessons/finding-the-shortest-path-in-graphs-with-bfs-algorithm
# GeeksforGeeks. (2025, July 15). Building an undirected graph and finding
#   shortest path using dictionaries in Python. GeeksforGeeks.
#   https://www.geeksforgeeks.org/python/building-an-undirected-graph-and-finding-shortest-path-using-dictionaries-in-python/
# Lavasani, A. (2023, September 17). Design Patterns in Python: Factory Method.
#   Medium.
#   https://medium.com/@amirm.lavasani/design-patterns-in-python-factory-method-1882d9a06cb4
# Python - Create a graph from a dictionary. (2019, September 29).
#   Stack Overflow.
#   https://stackoverflow.com/questions/58157354/python-create-a-graph-from-a-dictionary
# Rodriguez, I. (2019, February 11). The Factory Method Pattern and its
#   implementation in Python. Real Python.
#   https://realpython.com/factory-method-python/
# W3Schools.com. (n.d.). https://www.w3schools.com/python/python_dsa_graphs.asp
#


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

    def __init__(self, first_room):
        """
        Constructs the player object.

        :param first_room: The room the player is in when the game starts.
        :type first_room: Room
        """
        self.current_room = first_room
        self.inventory = []
        self.hints_left = 3

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


class RoomFactory:
    """
    A class to implement the factory pattern to create rooms.

    Methods:
        create_room(room_name): Creates an instance of a Room object using
        data from the rooms_config dictionary
    """

    @staticmethod
    def create_room(room_name):
        """
        Creates an instance of a Room object using data from the rooms_config
        dictionary

        :param room_name: The name of the room to look up in the rooms_config
            dictionary
        :type room_name: str
        :return: A Room object
        :rtype: Room
        """
        config = rooms_config.get(room_name)
        return Room(config["name"], config["item"])


class GraphFactory:
    """
    A class to implement the Factory pattern to create a graph data structure
    to hold room data.

    Methods:
        create_game_world(): Creates an instance of a Room object, assigning
        it data from the rooms_config dictionary and adding it to the rooms
        dictionary, then adds the connections between rooms in the direction
        the player must move in.
    """

    @staticmethod
    def create_game_world():
        """
        Creates an instance of a Room object, assigning it data from the
        rooms_config dictionary and adding it to the rooms dictionary, then
        adds the connections between rooms in the direction the player must
        move in

        :return: A dictionary of Room objects and their connecting rooms
        :rtype: dict
        """
        rooms = {}
        # Create the Rooms
        for room in rooms_config:
            rooms[room] = RoomFactory.create_room(room)

        # Add connections (edges) to the rooms
        for room, room_data in rooms_config.items():
            for direction, connected_room in room_data['exits'].items():
                rooms[room].add_connection(direction, rooms[connected_room])
        return rooms


class Game:
    """
    A class to represent and handle the flow of the game.

    Attributes:
        rooms (dict): A dictionary of all Rooms
        player (Player): The player
        total_items (int): The total number of the items in the house. The
            player must pick up all items to win. This variable is used to
            compare against the number of items the player has in their
            inventory.

    Methods:
        get_hint(current_room): Use the breadth-first search (BFS) algorithm
            to search through the rooms to find the closest room that has an
            item. Players can use this function up to three times.
        display_opening_message(): Returns a list of messages to welcome the
            player to the game, give the story and context, and explain
            how to play.
        display_player_status(): Returns the string returned from the player's
            get_player_status method
        display_room_status(room_name): Uses room_name to look up the
            appropriate room object and get their status using the room's
            get_room_status method
        move_player(direction): Checks if the direction the player typed is
            valid, then checks if the room they are in has a room connecting
            to it in that direction. If it does, it updates the player's
            current_room to the room in that direction to represent the player
            moving to a different room.
        process_command(user_input): Takes the user input, sanitizes it, then
            calls the appropriate function to handle their command.
        player_outcome(): Checks if the player has reached the room that
            the Chupacabras is in and whether they have the right number of
            items needed to win the game.
        play(): This method controls the flow of the game by calling methods
            in a while loop until the game is finished. It prints the opening
            messages, player status and room status. It takes the user input,
            checking if it is "q" for quitting the game. It calls the
            process_command method, printing the results followed by a text
            divider for ease of reading. It prints the winning or losing
            message before ending the game.
    """
    TEXT_DIVIDER = "-" * 30
    WELCOME_MESSAGE = "A Visit from El Chupacabras!"
    GAME_INFO = (
        "El chupacabras has come to suck the blood of your livestock! Move "
        "throughout your house and collect 6 items before coming face to "
        "face with the beast!")
    MOVING_INSTRUCTIONS = "To move to a different room type 'go south, " \
                          "'go north', 'go east', or 'go west'."
    ITEM_INSTRUCTIONS = "To add an item to your inventory, type 'get " \
                        "item name'."
    HINT_INSTRUCTIONS = "If you are having trouble finding a room that has " \
                        "an item, you can type 'hint' to get cardinal" \
                        " directions to the closest room with an item. " \
                        "Please type each direction one by one."
    QUIT_AND_REPLAY_INSTRUCTIONS = "To quit the game at any time, please " \
                                   "type 'q'. To replay the game after " \
                                   "quitting or finishing it, please type " \
                                   "'y'. Type 'n' to stop the game completely."
    VALIDATION_MESSAGE = "Please enter a valid move."
    EXIT_MESSAGE = "Thanks for playing, hope you had fun!"
    WINNING_MESSAGE = "You see el Chupacabras!\nYou toss the goat plushie " \
                      "by its feet. While it's investigating it, you squirt" \
                      " shampoo into its eyes, knock it out with your " \
                      "frying pan, tie it up with your rope, \nand take " \
                      "pictures of it once it's subdued. Luckily, you " \
                      "didn't have to hurt it with your machete.\n" \
                      "You call Animal Control and become famous for " \
                      "capturing the first live specimen of el Chupacabras." \
                      " Your goats and chicken are happy.\nCongratulations!"
    LOSING_MESSAGE = "You see el Chupacabras!\nYou try to fight it, but " \
                     "don't have enough items to deal with it. You manage" \
                     " to keep it away from your livestock, but it's not " \
                     "leaving hungry.\nYou become the first human victim " \
                     "of el Chupacabras.\nGame over."

    def __init__(self):
        graph_factory = GraphFactory()
        self.rooms = graph_factory.create_game_world()
        first_room = self.rooms["bedroom"]
        self.player = Player(first_room)

        # Count how many items are in the house, the player must collect all
        # items before facing the Chupacabras to win
        self.total_items = 0
        for room in self.rooms.values():
            if room.has_item():
                self.total_items += 1

    def get_hint(self, current_room):
        """
        Use the breadth-first search (BFS) algorithm to search through the
        rooms to find the closest room that has an item. Players can use this
        function up to three times.

        :param current_room: The room the player is currently in. BFS will
            start from there.
        :type current_room: Room
        :return: A message with either directions to the closest room with an
            item, that the room the player is in has an item, or that the
            player has no more items to pick up.
        :rtype: str
        """
        self.player.hints_left -= 1
        visited = []

        # Store room and direction in a tuple
        queue = [[(current_room, None)]]

        if current_room.has_item():
            return f"The room you are in has an item."

        while queue:
            path = queue.pop(0)
            room = path[-1][0]

            if room not in visited:
                neighbours = room.connected_rooms.items()

                for direction, neighbour in neighbours:
                    new_path = list(path)
                    new_path.append((neighbour, direction))
                    queue.append(new_path)

                    if neighbour.has_item():
                        directions = []
                        for room, cardinal in new_path[1:]:
                            directions.append(cardinal)
                        return f"To get to the closest item " \
                               f"head {', then '.join(directions)}."

                visited.append(room)
        return f"There are no more items to pick up."

    def display_opening_message(self):
        """
        Returns a list of messages to welcome the player to the game, give
        the story and context, and explain how to play.

        :return: The list of messages joined into a string with newlines
        :rtype: str
        """
        messages = [
            self.WELCOME_MESSAGE,
            self.GAME_INFO,
            self.MOVING_INSTRUCTIONS,
            self.ITEM_INSTRUCTIONS,
            self.HINT_INSTRUCTIONS,
            self.QUIT_AND_REPLAY_INSTRUCTIONS,
            self.TEXT_DIVIDER
        ]
        return "\n".join(messages)

    def display_player_status(self):
        """
        Returns the string returned from the player's get_player_status method

        :return: A string with the player's current room and inventory
        :rtype: str
        """
        return self.player.get_player_status()

    def display_room_status(self, room_name):
        """
        Uses room_name to look up the appropriate room object and get their
        status using the room's get_room_status method

        :param room_name: The name of a room to look up its status.
        :type room_name: str
        :return: A string describing the room's name, item in the room,
            and use for the item.
        :rtype: str
        """
        room = self.rooms[room_name]
        return room.get_room_status()

    def move_player(self, direction):
        """
        Checks if the direction the player typed is valid, then checks if the
        room they are in has a room connecting to it in that direction.
        If it does, it updates the player's current_room to the room in that
        direction to represent the player moving to a different room.

        :param direction: The direction provided by the player.
        :type direction: str
        :return: A string confirming that they moved to a different room or
        that there are no rooms in the direction they want to move in.
        :rtype: str
        """
        valid_directions = ["north", "south", "east", "west"]
        if direction not in valid_directions:
            return self.VALIDATION_MESSAGE
        if direction in self.player.current_room.connected_rooms:
            room_name = self.player.current_room.connected_rooms \
                .get(direction).name
            self.player.current_room = self.rooms[room_name]
            return f"You moved to the {room_name}."
        else:
            return f"There is no room in that direction."

    def process_command(self, user_input):
        """
        Takes the user input, sanitizes it, then calls the appropriate function
        to handle their command.

        :param user_input: The user input of what they want to do next in the
            game. It should start with "go", "get", or hint.
        :type user_input: str
        :return: The confirmation message returned from the function called
            according to the input, or a validation message if the input was
            not valid.
        :rtype: str
        """
        command = user_input.lower().strip().split()
        if len(command) == 0:
            return self.VALIDATION_MESSAGE

        if command[0] == "go":
            if len(command) < 2:
                return self.VALIDATION_MESSAGE
            else:
                return self.move_player(command[1])
        elif command[0] == "get":
            if len(command) < 2:
                return self.VALIDATION_MESSAGE
            else:
                desired_item = " ".join(command[1:])
                return self.player.get_item(desired_item)
        elif command[0] == "hint":
            if self.player.hints_left == 0:
                return f"Sorry, you have no more hints left."
            else:
                return self.get_hint(self.player.current_room)
        else:
            return self.VALIDATION_MESSAGE

    def player_outcome(self):
        """
        Checks if the player has reached the room that the Chupacabras is in
        and whether they have the right number of items needed to win the game.

        :return: A string signaling if the player won or lost, or None to
            continue the game until the player reaches the Chupacabra's room.
        :rtype: str or None
        """
        if self.player.current_room.name == "backyard":
            if len(self.player.inventory) < self.total_items:
                return "lost"
            elif len(self.player.inventory) == self.total_items:
                return "won"
        else:
            return None

    def play(self):
        """
        This method controls the flow of the game by calling methods in a
        while loop until the game is finished. It prints the opening messages,
        player status and room status. It takes the user input, checking if it
        is "q" for quitting the game. It calls the process_command method,
        printing the results followed by a text divider for ease of reading.
        It prints the winning or losing message before ending the game.

        :return: Nothing
        :rtype: None
        """
        print(self.display_opening_message())
        game_is_finished = False

        while not game_is_finished:
            print(self.display_player_status())
            print(self.display_room_status(self.player.current_room.name))
            user_command = input("Enter your command:\n")
            if user_command.lower() == "q":
                game_is_finished = True
            else:
                print(self.process_command(user_command))
            print(self.TEXT_DIVIDER)
            player_outcome = self.player_outcome()
            if player_outcome == "lost":
                print(self.LOSING_MESSAGE)
                game_is_finished = True
            elif player_outcome == "won":
                print(self.WINNING_MESSAGE)
                game_is_finished = True
            else:
                continue


# rooms_config defines all the rooms in the game. Each key is a room name and
# each value is a dictionary with the name (str) of the room, item
# (dict or None) with the item name and use, and exits (dict) with the cardinal
# directions and name of the rooms they lead to
rooms_config = {
    "bedroom": {
        "name": "bedroom",
        "item": None,
        "exits": {"north": "living room", "east": "kids' room"}
    },
    "living room": {
        "name": "living room",
        "item": {"item_name": "pro camera",
                 "item_use": "document clear proof of the existence of el "
                             "Chupacabras"},
        "exits": {"north": "storage room", "east": "kitchen",
                  "south": "bedroom", "west": "bathroom"}
    },
    "kids' room": {
        "name": "kids' room",
        "item": {"item_name": "goat plushie",
                 "item_use": "distract el Chupacabras"},
        "exits": {"west": "bedroom"}
    },
    "storage room": {
        "name": "storage room",
        "item": {"item_name": "machete",
                 "item_use": "kill el Chupacabras if you have to"},
        "exits": {"east": "backyard", "south": "living room"}
    },
    "kitchen": {
        "name": "kitchen",
        "item": {"item_name": "frying pan",
                 "item_use": "knock out el Chupacabras"},
        "exits": {"north": "garage", "west": "living room"}
    },
    "bathroom": {
        "name": "bathroom",
        "item": {"item_name": "shampoo bottle",
                 "item_use": "blind el Chupacabras"},
        "exits": {"east": "living room"}
    },
    "garage": {
        "name": "garage",
        "item": {"item_name": "rope",
                 "item_use": "tie up el Chupacabras"},
        "exits": {"south": "kitchen"}
    },
    "backyard": {  # Villain room
        "name": "backyard",
        "item": None,
        "exits": {"west": "storage room"}
    }
}


def main():
    """
    The entry point for the game. Creates a Game object and starts the game
    loop. Restarts the game if the player ended the previous game and presses
    "y", or ends the game and prints a goodbye message.

    :return: Nothing
    :rtype: None
    """
    replay_game = True

    while replay_game:
        game = Game()
        game.play()

        start_over_input = input("\nDo you want to play again? y/n\n")
        if start_over_input.lower() != "y":
            print("Thank you for playing!")
            break


if __name__ == '__main__':
    app.run(debug=True)
    main()
