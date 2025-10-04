from factories.room_factory import RoomFactory
from rooms_config import rooms_config


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
