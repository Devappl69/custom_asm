# custom_language
My own custom stack-like language

# Usage
`python main.py PATH_TO_FILE`
or
`python main.py` and enter file path in the prompt


# Commands

- PUSH (`ASM_push(item)`): Pushes an item to the stack
- POP (`ASM_pop()`): Removes the top-most item from the stack and returns it
- ADD (`ASM_add()`): Adds the 2 top-most items from the stack, pops them, and then pushes the output
- SUB (`ASM_sub()`): Subtracts the top-most from the second top-most items from the stack, pops them, and then pushes the output
- PRINT (`ASM_print(string_literal)`): Prints out the given string
- READ (`ASM_read()`): Reads the input and pushes it to the stack
- JUMP.EQ.0 (`ASM_JUMP_EQ_0(label)`): Jumps to the given label if the top-most item in the stack is equal to 0
- JUMP.GT.0 (`ASM_JUMP_GT_0(label)`): Jumps to the given label if the top-most item in the stack is greater than to 0
- JUMP.LT.0 (`ASM_JUMP_LT_0(label)`): Jumps to the given label if the top-most item in the stack is lower than to 0
- SIZE (`ASM_size()`): Pushes the stack size to the stack
- IS.EMPTY (`ASM_is_empty()`): Pushes 1 if the stack is empty, pushes 0 if the stack is full to the stack
- PEEK (`ASM_peek()`): Pushes the top-most item to the stack, effectivley duplicating it
- OUT (`ASM_out()`): Pops the top-most item in the stack and prints it
- SWAP (`ASM_swap()`): Swaps the 2 items in the stack, who's index corresponds to the 2 top-most items in the stack
- ROT (`ASM_rot()`): Reverses the stack
- PICK (`ASM_pick(index)`): Pushes the items to the stack, who's index corresponds to the top-most item of the stack
