#!/usr/bin/python3

""" Snake : defines snake object
"""

class Snake:
    def __init__(self, lenght):
        self.lenght = lenght


""" Cell : defines a cell in tye matrix object
"""

class Cell:
    def __init__(self, rels_value, visited):
        self.rels_value = rels_value
        self.visited = false
