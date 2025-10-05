# Code by Angela Karina Vegega Ortiz
# Enhancement Three - October 5, 2025.
# This game was initially played in the console. Enhancement three included
# adding a database to hold user data, user validation with passwords,
# creating a graphical user interface to turn this game into a full stack
# application that can be hosted online, and adding a Scoreboards page to
# show the user's best completion times.
#
# This is a text based adventure game called A Visit from El Chupacabras.
# Users must type commands to progress the story. Their commands must start
# with 'go' or 'get'. The goal is to move from room to room collecting items
# before reaching the Chupacabras. If the player collected all the items,
# they win the game. Whether they win or lose, they can choose to start
# a new game.
# The game can be demoed logging in with username demo and password demo1234
#
# I used articles by Lavasani (2023) and Rodriguez (2019) to research and
# adapt the Factory pattern for creating rooms.
# I used articles on GeeksforGeeks (2025), w3schools (W3Schools.com, n.d.),
# Code Signal (“Finding the Shortest Path in Graphs With BFS Algorithm,” n.d.),
# and StackOverflow (Python - Create a Graph From a Dictionary, 2019), to
# guide me in creating the graph data structure and using BFS algorithm to
# find the shortest path for the hint functionality.
# I used and adapted Tech With Tim's (2021) tutorial to guide me in adding
# user validation and creating a full stack python application. I referenced
# the Flask (Welcome to Flask — Flask Documentation (3.1.x), n.d.), Bootstrap
# (Bootstrap team, n.d.), SQLAlchemy (SQLAlchemy 2.0 Documentation, 2025),
# and Jinja (Jinja Documentation (3.1.x), n.d.) documentation while creating
# the app to debug and build it out.
#
# References:
# Bootstrap team. (n.d.). Get started with Bootstrap.
#   https://getbootstrap.com/docs/5.3/getting-started/introduction/
# Finding the shortest path in graphs with BFS algorithm. (n.d.).
#   CodeSignal.
#   https://codesignal.com/learn/courses/mastering-graphs-in-python/lessons/finding-the-shortest-path-in-graphs-with-bfs-algorithm
# GeeksforGeeks. (2025, July 15). Building an undirected graph and finding
#   shortest path using dictionaries in Python. GeeksforGeeks.
#   https://www.geeksforgeeks.org/python/building-an-undirected-graph-and-finding-shortest-path-using-dictionaries-in-python/
# Jinja Documentation (3.1.x). (n.d.).
#   https://jinja.palletsprojects.com/en/stable/
# Lavasani, A. (2023, September 17). Design Patterns in Python: Factory Method.
#   Medium.
#   https://medium.com/@amirm.lavasani/design-patterns-in-python-factory-method-1882d9a06cb4
# Python - Create a graph from a dictionary. (2019, September 29).
#   Stack Overflow.
#   https://stackoverflow.com/questions/58157354/python-create-a-graph-from-a-dictionary
# Rodriguez, I. (2019, February 11). The Factory Method Pattern and its
#   implementation in Python. Real Python.
#   https://realpython.com/factory-method-python/
# SQLAlchemy 2.0 Documentation. (2025, August 11).
#   https://docs.sqlalchemy.org/en/20/
# Tech With Tim. (2021, February 1). Python website full tutorial - flask,
#   authentication, databases & more [Video]. YouTube.
#   https://www.youtube.com/watch?v=dam0GPOAvVI
# W3Schools.com. (n.d.). https://www.w3schools.com/python/python_dsa_graphs.asp
# Welcome to Flask — Flask Documentation (3.1.x). (n.d.).
#   https://flask.palletsprojects.com/en/stable/
"""
Main entry point for the Flask application
"""
from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
