import sys

program_file = "examples/Cat.txt"
verbose = False

if len(sys.argv)>1:
    program_file = sys.argv[1]
    if len(sys.argv)>2:
        verbose = True if (str(sys.argv[2]).lower() in ["t", "true", "1"]) else False
else:
    #program_file = input("Enter path to file: ")
    pass

pointer = 0
ASM_stack = []
ASM_labels = {}

max_iterations = 1000
iteration_count = 0

def ASM_push(x: int) -> None:
    ASM_stack.append(int(x))

def ASM_pop() -> int:
    x: int = ASM_stack[-1]
    ASM_stack.pop(-1)
    return int(x)

def ASM_add() -> None:
    if len(ASM_stack) > 1:
        x = ASM_pop()
        y = ASM_pop()
        ASM_push(x+y)
    else:
        print("Not enough items in stack to add")
        quit()

def ASM_sub() -> None:
    if len(ASM_stack) > 1:
        x: int = ASM_pop()
        y: int = ASM_pop()
        ASM_push(y-x)
    else:
        print("Not enough items in stack to subtract")
        quit()

def ASM_print(string_literal: str) -> None:
    print(string_literal[:-1][1:])

def ASM_read() -> None:
    IO_input: int = int(input("IO In: "))
    ASM_push(IO_input)

def ASM_JUMP_EQ_0(label: str) -> None:
    global pointer
    if ASM_stack[-1] == 0:
        pointer = ASM_labels[str(label)]

def ASM_JUMP_GT_0(label: str) -> None:
    global pointer
    if ASM_stack[-1] > 0:
        pointer = ASM_labels[str(label)]

def ASM_JUMP_LT_0(label: str) -> None:
    global pointer
    if ASM_stack[-1] < 0:
        pointer = ASM_labels[str(label)]

def ASM_size() -> None:
    ASM_push(len(ASM_stack))

def ASM_is_empty() -> None:
    if len(ASM_stack) > 0:
        ASM_push(0)
    else:
        ASM_push(1)

def ASM_peek() -> None:
    ASM_push(ASM_stack[-1])

def ASM_out() -> None:
    print("IO Out:", ASM_pop())

def ASM_swap() -> None:
    x = ASM_pop()
    y = ASM_pop()
    ASM_stack[x], ASM_stack[y] = ASM_stack[y], ASM_stack[x]

def ASM_rot() -> None:
    ASM_stack.reverse()

def ASM_pick(x: int) -> None:
    ASM_stack.append(ASM_stack[int(x)])

def ASM_mul() -> None:
    if len(ASM_stack) > 1:
        x = ASM_pop()
        y = ASM_pop()
        ASM_push(x*y)
    else:
        print("Not enough items in stack to multiply")
        quit()

def ASM_div() -> None:
    if len(ASM_stack) > 1:
        x = ASM_pop()
        y = ASM_pop()
        ASM_push(y/x)
    else:
        print("Not enough items in stack to divide")
        quit()

commands = {
    "PUSH": ASM_push,
    "POP": ASM_pop,
    "ADD": ASM_add,
    "SUB": ASM_sub,
    "PRINT": ASM_print,
    "READ": ASM_read,
    "JUMP.EQ.0": ASM_JUMP_EQ_0,
    "JUMP.GT.0": ASM_JUMP_GT_0,
    "JUMP.LT.0": ASM_JUMP_LT_0,
    "SIZE": ASM_size,
    "IS.EMPTY": ASM_is_empty,
    "PEEK": ASM_peek,
    "OUT": ASM_out,
    "SWAP": ASM_swap,
    "ROT": ASM_rot,
    "PICK": ASM_pick,
    "MUL": ASM_mul,
    "DIV": ASM_div,
}


with open(program_file) as file:
    file_contents = file.read()
    lines = file_contents.split("\n")
    if "HALT" not in file_contents:
        print("No HALT found")
        quit()

for index, line in enumerate(lines):
    if "#" in line:
        comment_index = (line.index("#")+2)-2
        line = lines[index][:comment_index]
        if verbose: print("Found comment on line", index+1)
    
    line = line.strip()
    line_contents = line.split(" ")
    lines[index] = line
    
    if line_contents[0]:
        if (len(line_contents) == 1):
            if (line_contents[0] not in commands) and (line_contents[0] != "HALT"):
                if (line_contents[0][-1] == ":"):
                    if verbose: print("Added label:", index, line_contents[0][:-1])
                    ASM_labels[line_contents[0][:-1]] = index
                    if verbose: print("Current labels:", ASM_labels)
                else:
                    print(f"Error: Command '{line_contents[0]}' not recognized, line {index+1}")
                    quit()
    else:
        if (line_contents[0] not in commands) and (line_contents[0] != "HALT") and (line_contents[0] != ""):
            print(f"Error: Command '{line_contents[0]}' not recognized, line {index+1}")
            quit()

while iteration_count < max_iterations:
    line_contents = lines[pointer].split(" ")
    opcode = line_contents[0]
    
    if (opcode == "HALT"):
        if verbose: print("Halted")
        break
    
    if opcode:
        if (len(line_contents) == 1):
            if opcode[:-1] not in ASM_labels:
                if verbose: print("Executed command:", opcode)
                commands[line_contents[0]]()
                if verbose: print("Current stack:", ASM_stack)
        else:
            if verbose: print("Executed command:", opcode, " ".join(str(contents) for contents in line_contents[1:]))
            commands[opcode](" ".join(str(contents) for contents in line_contents[1:]))
            if verbose: print("Current stack:", ASM_stack)
    
    iteration_count += 1
    pointer += 1

if iteration_count >= max_iterations:
    print("Max iterations reached")

if verbose:
    print("Final stack:", ASM_stack)
    print("Labels:", ASM_labels)
    print(f"Iterations: {iteration_count}/{max_iterations}")
