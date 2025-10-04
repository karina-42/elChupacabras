from game_classes.room import Room
from rooms_config import rooms_config


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
