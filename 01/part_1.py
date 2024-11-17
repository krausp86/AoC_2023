# Advent oc Code 2023
# Day 01
# Patrick Kraus-Füreder

def run_puzzle(test=False):
    if test:
        input_file = "test_input.txt"
    else:
        input_file = "quiz_input.txt"

    with open(input_file, 'r') as file:
        lines= file.readlines()
        sum = 0
        for line in lines:
            line_num = [x for x in line if x in ['1','2','3','4','5','6','7','8','9','0']]
            sum += 10*int(line_num[0]) + int(line_num[-1])
        print(sum)


if __name__ == "__main__":
    run_puzzle()
