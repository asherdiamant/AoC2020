import re
import numpy as np

program = []
with open('data/day8.txt') as f:
    for line in f.readlines():
        mp = re.match(r'(?P<opcode>\w+) (?P<operand>\S+)', line)
        program.append([mp['opcode'], int(mp['operand']), 0])
    program.append(['end', 0, 0])  # flag for eof


def run_program(code):
    ip = 0
    acc = 0
    seq = 1
    status = 0
    trace = []

    while 1:
        curr_line = code[ip]
        trace.append((ip, curr_line))
        # print(seq, ':', ip, ':', curr_line)
        opcode = curr_line[0]
        operand = curr_line[1]
        has_run = curr_line[2]
        if has_run:
            print(f"Infinite Loop detected. ip={ip}, acc={acc}")
            status = 2
            break
        else:
            curr_line[2] = seq  # it has now run
            seq += 1
            if opcode == 'acc':
                acc += operand
                ip += 1
            elif opcode == 'jmp':
                ip += operand
            elif opcode == 'nop':
                ip += 1
            elif opcode == 'end':
                print(f"code terminated successfully. acc={acc}")
                status = 0
                break
            else:
                print("Erroneous opcode:", opcode)
                status = 1
                break
    return status, trace


run_status, base_trace = run_program(program)

for pointer, code_line in reversed(base_trace):
    test_program = program.copy()
    for line in test_program:
        line[2] = 0
    if code_line[0] == 'jmp':
        replacement = ['nop', code_line[1], 0]
    elif code_line[0] == 'nop':
        replacement = ['jmp', code_line[1], 0]
    else:
        continue
    test_program[pointer] = replacement
    result, _ = run_program(test_program)
    if result == 0:
        print(f"Replace line {pointer}: {program[pointer][:2]} with {replacement[:2]}")
        break


# reset the has_run marks
for line in program:
    line[2] = 0

program[273] = ['nop', -55, 0]

run_program(program)
