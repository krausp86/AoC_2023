# Advent of Code 2023 - Day 3 - Part 1
# Patrick Kraus-Füreder
# 19.11.2024

import pytest
import re

def run_puzzle(test=False):
    if test:
        dataset = 'test_input_1.txt'
    else:
        dataset = 'quiz_input_1.txt'

    with open(dataset, 'r') as file:
        lines = file.readlines()
        sum = 0
        pattern = r'\d+'
        for linenum, line in enumerate(lines):
            # Finde Zahlen
            zahlen = re.finditer(pattern, line) 
            for zahl in zahlen:
                if is_adjacent_to_symbol(zahl, lines, linenum):
                    sum += int(zahl.group())
    return sum

def is_adjacent_to_symbol(number, matrix, line):
    # Funktion um zu prüfen, ob eine Zahl in der Matrix vertikal, horizontal oder diagonal
    # an ein symbol grenzt das nicht . oder eine andere Zahl ist
    is_adjacent = False
    pattern = r"[^0-9.]"
    if line > 0: 
        is_adjacent = is_adjacent or bool(re.search(pattern, matrix[line-1][max(number.start()-1,0):min(number.end()+1,len(matrix[line-1])-1)]))
    if line < len(matrix)-1:
        is_adjacent = is_adjacent or bool(re.search(pattern, matrix[line+1][max(number.start()-1,0):min(number.end()+1,len(matrix[line+1])-1)]))
    if number.start() > 0:
        is_adjacent = is_adjacent or bool(re.search(pattern, matrix[line][number.start()-1:number.start()]))
    if number.end() < len(matrix[line])-1:
        is_adjacent = is_adjacent or bool(re.search(pattern, matrix[line][number.end():number.end()+1]))
    return is_adjacent

def test_is_adjacent_to_symbol():
    pattern = r"\d+"
    ARR01 = ['..........\n',
             '.5........\n',
             '..........\n',
             '..........\n']
    NUM01 = re.search(pattern, ARR01[1])

    ARR02 = ['.#........\n',
             '.5........\n',
             '..........\n',
             '..........\n']
    NUM02 = re.search(pattern, ARR02[1])

    ARR03 = ['..$.......\n',
             '.5........\n',
             '..........\n',
             '..........\n']
    NUM03 = re.search(pattern, ARR03[1])

    ARR04 = ['..........\n',
             '.5*.......\n',
             '..........\n',
             '..........\n']
    NUM04 = re.search(pattern, ARR04[1])

    ARR05 = ['..........\n',
             '.5........\n',
             '..#.......\n',
             '..........\n']
    NUM05 = re.search(pattern, ARR05[1])

    ARR06 = ['..........\n',
             '.5........\n',
             '.*........\n',
             '..........\n']
    NUM06 = re.search(pattern, ARR06[1])

    ARR07 = ['..........\n',
             '.5........\n',
             '#.........\n',
             '..........\n']
    NUM07 = re.search(pattern, ARR07[1])

    ARR08 = ['..........\n',
             '#5........\n',
             '..........\n',
             '..........\n']
    NUM08 = re.search(pattern, ARR08[1])

    ARR09 = ['$.........\n',
             '.5........\n',
             '..........\n',
             '..........\n']
    NUM09 = re.search(pattern, ARR09[1])

    ARR10 = ['$.........\n',
             '.523......\n',
             '..........\n',
             '..........\n']
    NUM10 = re.search(pattern, ARR10[1])

    ARR11 = ['$523......\n',
             '..........\n',
             '..........\n',
             '..........\n']
    NUM11 = re.search(pattern, ARR11[0])

    ARR12 = ['..........\n',
             '..........\n',
             '..........\n',
             '$523......\n']
    NUM12 = re.search(pattern, ARR12[3])

    ARR13 = ['$.........\n',
             '523.......\n',
             '..........\n',
             '..........\n']
    NUM13 = re.search(pattern, ARR13[1])

    ARR14 = ['.........$\n',
             '.......523\n',
             '..........\n',
             '..........\n']
    NUM14 = re.search(pattern, ARR14[1])

    ARR15 = ['.523......\n',
             '..........\n',
             '..........\n',
             '..........\n']
    NUM15 = re.search(pattern, ARR15[0])

    ARR16 = ['..........\n',
             '..........\n',
             '..........\n',
             '.523......\n']
    NUM16 = re.search(pattern, ARR16[3])

    ARR17 = ['..........\n',
             '523.......\n',
             '..........\n',
             '..........\n']
    NUM17 = re.search(pattern, ARR17[1])

    ARR18 = ['..........\n',
             '.......523\n',
             '..........\n',
             '..........\n']
    NUM18 = re.search(pattern, ARR18[1])

    ARR19 = ['......3...\n',
             '.......523\n',
             '..........\n',
             '..........\n']
    NUM19 = re.search(pattern, ARR19[1])

    ARR20 = ['.....+....\n',
             '.523......\n',
             '..........\n',
             '..........\n']
    NUM20 = re.search(pattern, ARR20[1])

    ARR21 = ['..........\n',
             '.523.+....\n',
             '..........\n',
             '..........\n']
    NUM21 = re.search(pattern, ARR21[1])

    ARR22 = ['..........\n',
             '.523......\n',
             '.....+....\n',
             '..........\n']
    NUM22 = re.search(pattern, ARR22[1])

    ARR23 = ['+.........\n',
             '..523.....\n',
             '..........\n',
             '..........\n']
    NUM23 = re.search(pattern, ARR23[1])

    ARR24 = ['..........\n',
             '+.523.....\n',
             '..........\n',
             '..........\n']
    NUM24 = re.search(pattern, ARR24[1])

    ARR25 = ['..........\n',
             '..523.....\n',
             '+.........\n',
             '..........\n']
    NUM25 = re.search(pattern, ARR25[1])



    assert not is_adjacent_to_symbol(NUM01, ARR01, 1)
    assert is_adjacent_to_symbol(NUM02, ARR02, 1)
    assert is_adjacent_to_symbol(NUM03, ARR03, 1)
    assert is_adjacent_to_symbol(NUM04, ARR04, 1)
    assert is_adjacent_to_symbol(NUM05, ARR05, 1)
    assert is_adjacent_to_symbol(NUM06, ARR06, 1)
    assert is_adjacent_to_symbol(NUM07, ARR07, 1)
    assert is_adjacent_to_symbol(NUM08, ARR08, 1)
    assert is_adjacent_to_symbol(NUM09, ARR09, 1)
    assert is_adjacent_to_symbol(NUM10, ARR10, 1)
    assert is_adjacent_to_symbol(NUM11, ARR11, 0)
    assert is_adjacent_to_symbol(NUM12, ARR12, 3)
    assert is_adjacent_to_symbol(NUM13, ARR13, 1)
    assert is_adjacent_to_symbol(NUM14, ARR14, 1)
    assert not is_adjacent_to_symbol(NUM15, ARR15, 0)
    assert not is_adjacent_to_symbol(NUM16, ARR16, 3)
    assert not is_adjacent_to_symbol(NUM17, ARR17, 1)
    assert not is_adjacent_to_symbol(NUM18, ARR18, 1)
    assert not is_adjacent_to_symbol(NUM19, ARR19, 1)
    assert not is_adjacent_to_symbol(NUM20, ARR20, 1)
    assert not is_adjacent_to_symbol(NUM21, ARR21, 1)
    assert not is_adjacent_to_symbol(NUM22, ARR22, 1)
    assert not is_adjacent_to_symbol(NUM23, ARR23, 1)
    assert not is_adjacent_to_symbol(NUM24, ARR24, 1)
    assert not is_adjacent_to_symbol(NUM25, ARR25, 1)


def test_run_puzzle():
    assert run_puzzle(True) == 4361

if __name__ == '__main__':
    print(run_puzzle())
