from datetime import datetime
from factories.graph_factory import GraphFactory
from game_classes.player import Player


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
        start_time (DateTime): The time the player started a game
        end_time (DateTime): The time the player ended a game by winning it

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
        start_timer(): Check if a starting time has been assigned to
        start_time, if not, then assign the current time to start_time.
        get_elapsed_time(): Get the player outcome, stop the timer if the
            player finished the game. Calculate and assign the elapsed time to
            elapsed_time. Return the elapsed seconds
    """

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
    VALIDATION_MESSAGE = "Please enter a valid move."
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
        self.start_time = None
        self.end_time = None

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
        Returns a list of messages to welcome the player to the game,
        give the story and context, and explain how to play.

        :return: The list of messages joined into a string with newlines
        :rtype: str
        """
        messages = [
            self.GAME_INFO,
            self.MOVING_INSTRUCTIONS,
            self.ITEM_INSTRUCTIONS,
            self.HINT_INSTRUCTIONS
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
            continue the game until the player reaches the
            Chupacabra's room.
        :rtype: str or None
        """
        if self.player.current_room.name == "backyard":
            if len(self.player.inventory) < self.total_items:
                return "lost"
            elif len(self.player.inventory) == self.total_items:
                return "won"
        else:
            return None

    def start_timer(self):
        """
        Check if a starting time has been assigned to start_time, if not, then
        assign the current time to start_time.

        :return: Nothing
        :rtype: None
        """
        now = datetime.now()
        if self.start_time is None:
            self.start_time = now

    def get_elapsed_time(self):
        """
        Get the player outcome, stop the timer if the player finished the game.
        Calculate and assign the elapsed time to elapsed_time. Return the
        elapsed seconds, else None

        :return: Elapsed time in total seconds or nothing
        :rtype: float, None
        """
        outcome = self.player_outcome()
        now = datetime.now()
        if outcome in ['won', 'lost']:
            self.end_time = now
            if self.start_time and outcome == 'won':
                elapsed_time = self.end_time - self.start_time
                return elapsed_time.total_seconds()
