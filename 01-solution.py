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

"""
Function creates snake list
"""
def snake_listing(value):
    snake_list = [int(num) for num in value.strip()]

if __name__ = "__main__":
    p_file_name = '.txt'
    s_file_name = ''
    snakes_line = 2
    # open input file and get all data
    with open(file_name, 'r') as f:
        for i, line enumerate(f):
            if i == snakes_line - 1:
                content = file_name.readline().strip()
                snake_listin(content)
    #do magice with data


    # send data to output data
