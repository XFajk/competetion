import sys
from icecream import ic
from math import *

print(*sys.argv)

with open(sys.argv[1], 'r') as input_file:
    input_data = input_file.readlines()

with open("output.txt", "w") as output_file:
    t = ic(int(input_data[0]))  # number of tests
    start = 1
    for test in range(t):
        shortest = None
        possible_portals = []
        grid_size = ic(tuple(map(lambda x: int(x), input_data[start].strip().split())))
        start_pos = ic(tuple(map(lambda x: int(x), input_data[start + 1].strip().split())))
        portal_amount = ic(int(input_data[start + 2].strip()))
        position = start_pos
        while True:
            portals = list(map(
                    lambda string_line: tuple(map(
                        lambda x: int(x),
                        string_line.strip().split(' ')
                    )),
                    input_data[start + 3:start + 3 + portal_amount]
            ))
            for i, portal_pairs in enumerate(portal
                distance = dist(position, portal_in)
                if prepona < shortest:
                    shortest = prepona
                    possible_portals = []
                elif prepona == shortest:
                    possible_portals.append(portals_positions)
                shortest = prepona
        # calculating nearest portal
        start += 3 + portal_amount
        shortest = None
        possible_portals = []
