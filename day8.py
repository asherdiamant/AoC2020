import re
import numpy as np


input_file = []
with open('data/day8.txt') as f:
    for line in f.readlines():
        mp = re.match(r'(?P<opcode>\w+) (?P<operand>\S+)', line)
        input_file.append([mp['opcode'], int(mp['operand']), 0])

ip = 0
acc = 0

while 1:
    curr_line = input_file[ip]
    opcode = curr_line[0]
    operand = curr_line[1]
    has_run = curr_line[2]
    if has_run:
        print(f"Infinite Loop detected. ip={ip}, acc={acc}")
        exit(2)
    else:
        curr_line[2] = 1 # it has now run
        if opcode == 'acc':
            acc += operand
            ip += 1
        elif opcode == 'jmp':
            ip += operand
        elif opcode == 'nop':
            ip += 1
        else:
            print("Erroneous opcode:", opcode)
            exit(1)

