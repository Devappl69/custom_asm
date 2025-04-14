# Custom ASM Interpreter
My own custom assembly-like language, that is mostly stack-based



# Usage
### Using Arguments
`python main.py PATH_TO_FILE`
### Using Python Inputs
`python main.py` and enter file path in the prompt



# Commands
## Default
- PUSH (`ASM_push(item)`): Pushes an item to the stack
- POP (`ASM_pop()`): Removes the top-most item from the stack and returns it
- PRINT (`ASM_print(string_literal)`): Prints out the given string
- READ (`ASM_read()`): Reads the input and pushes it to the stack

## Arithmetic
- ADD (`ASM_add()`): Adds the 2 top-most items from the stack, pops them, and then pushes the output
- SUB (`ASM_sub()`): Subtracts the top-most from the second top-most items from the stack, pops them, and then pushes the output
- MUL (`ASM_mul()`): Multiplies the 2 top-most items from the stack, pops them, and then pushes the output
- DIV (`ASM_div()`): Divides the top-most by the second top-most items from the stack, pops them, and then pushes the output

## Jumps
- JUMP.EQ.0 (`ASM_JUMP_EQ_0(label)`): Jumps to the given label if the top-most item in the stack is equal to 0
- JUMP.GT.0 (`ASM_JUMP_GT_0(label)`): Jumps to the given label if the top-most item in the stack is greater than to 0
- JUMP.LT.0 (`ASM_JUMP_LT_0(label)`): Jumps to the given label if the top-most item in the stack is lower than to 0

## Other
- SIZE (`ASM_size()`): Pushes the stack size to the stack
- IS.EMPTY (`ASM_is_empty()`): Pushes 1 if the stack is empty, pushes 0 if the stack is full to the stack
- PEEK (`ASM_peek()`): Pushes the top-most item to the stack, effectivley duplicating it
- OUT (`ASM_out()`): Pops the top-most item in the stack and prints it

## Array-based
- SWAP (`ASM_swap()`): Swaps the 2 items in the stack, who's index corresponds to the 2 top-most items in the stack
- ROT (`ASM_rot()`): Reverses the stack
- PICK (`ASM_pick(index)`): Pushes the items to the stack, who's index corresponds to the top-most item of the stack

## Special
- LABEL (`label:`): Defines a label by using the ':' sign after its name
- HALT (`halt`): Halts the program, every program must have at least one of these



# Roadmap
- Logging
- Verbose sys arguments
- Better error handling
- Comments
- Goto line #
- Compiling
