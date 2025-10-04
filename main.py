from game_classes.game import Game
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
# This is a text based adventure game_classes called A Visit from El Chupacabras.
# Users must type commands to progress the story. Their commands must start
# with 'go' or 'get'. The goal is to move from room to room collecting items
# before reaching the Chupacabras. If the player collected all the items,
# they win the game_classes. Whether they win or lose, they can choose to start
# a new game_classes.
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


def main():
    """
    The entry point for the game_classes. Creates a Game object and starts the game_classes
    loop. Restarts the game_classes if the player ended the previous game_classes and presses
    "y", or ends the game_classes and prints a goodbye message.

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
