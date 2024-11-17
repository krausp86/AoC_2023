# Advent oc Code 2023
# Day 01 - part 2
# Patrick Kraus-Füreder

import pytest

numbers = {
    '0':0,
    '1':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    'zero':0,
    'one':1,
    'two':2,
    'three':3,
    'four':4,
    'five':5,
    'six':6,
    'seven':7,
    'eight':8,
    'nine':9,
    }

def read_first_number(line, numbers, direction = 'forward'):
    for num, _ in enumerate(line):
        if direction == 'forward':
            elem = line[:num]
        elif direction == 'backward':
            elem = line[-(num+1):]
        else:
            raise Exception("direction must be 'forward' or 'backward'")
        for key in numbers:
            if key in elem:
                return numbers[key]

def run_puzzle(test=False):
    if test:
        input_file = "test_input2.txt"
    else:
        input_file = "quiz_input.txt"

    with open(input_file, 'r') as file:
        lines= file.readlines()
        sum = 0
        for line in lines:
            first_number = read_first_number(line, numbers, direction = 'forward')
            last_number = read_first_number(line, numbers, direction = 'backward')
            sum += 10*first_number + last_number
    return sum

def test_read_first_number():
    assert read_first_number("two1nine", numbers, direction = 'forward') == 2
    assert read_first_number("two1nine", numbers, direction = 'backward') == 9
    assert read_first_number("abcone2threexyz", numbers, direction = 'forward') == 1
    assert read_first_number("abcone2threexyz", numbers, direction = 'backward') == 3
    assert read_first_number("4nineeightseven2", numbers, direction = 'forward') == 4
    assert read_first_number("4nineeightseven2", numbers, direction = 'backward') == 2
    assert read_first_number("4nineeight2sevn", numbers, direction = 'backward') == 2


def test_run_puzzle():
    assert run_puzzle(test=True) == 281

if __name__ == "__main__":
    print(run_puzzle())
