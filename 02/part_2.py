# Advent of Code 2023 - Day 2 - part 2
# Patrick Kraus-Füreder
# 18.11.2024

import re
import math
import pytest

# Prepare indices for colors
colors = {'red': 0, 'green':1, 'blue':2}


def run_puzzle(test=False):
    if test:
        dataset = 'test_input_1.txt'
    else:
        dataset = 'quiz_input_1.txt'

    with open(dataset, 'r') as file:
        lines = file.readlines()
        sum = 0
        for line in lines:
            n, max_cubes = get_max_numbers(line)
            sum += math.prod(max_cubes)
    return sum


def get_max_numbers(line, colors=colors):
    # Pattern for initial split
    pattern = r"\b\w+\s\d+|\d+\s\w+"
    matches = re.findall(pattern, line)
    # Match 0 is the Game number
    g_num = int(matches[0].split()[1])
    # Set default number of max cubes
    max_cubes = [0, 0, 0]
    # Iterate over the matches
    for match in matches[1:]:
        # Split the match
        num, color = match.split()
        # Get the index of the color
        idx = colors[color]
        # Check if the number is greater than the current max
        if int(num) > max_cubes[idx]:
            max_cubes[idx] = int(num)
    return [g_num, max_cubes]


def test_get_max_numbers():
    assert get_max_numbers('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green') == [1, [4, 2, 6]]
    assert get_max_numbers('Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue') == [2, [1, 3, 4]]
    assert get_max_numbers('Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red') == [3, [20, 13, 6]]
    assert get_max_numbers('Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red') == [4, [14, 3, 15]]
    assert get_max_numbers('Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green') == [5, [6, 3, 2]]

def test_run_puzzle():
    assert run_puzzle(True) == 2286 

if __name__ == '__main__':
    print(run_puzzle())
