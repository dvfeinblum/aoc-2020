from copy import deepcopy

def parse_instructions(inp):
    inp_list = []
    for line in inp:
        instruct, val = line.split(" ")
        # instruction, instr value, execution counter
        inp_list.append([instruct, int(val), 0])
    return inp_list

def find_acc_value(parsed_instr, current_step=0, acc=0, swapped_instr=False):

    while True:
        if current_step == len(parsed_instr):
            print(f"Program exited successfully!\nAccumulator:{acc}")
            break
        instr, instr_val, count = parsed_instr[current_step]
        if count > 0:
            break

        if instr == "acc":
            acc += instr_val
            delta = 1
        elif instr == "jmp":
            delta = instr_val
            if not swapped_instr:
                # Let's try flipping this instruction and see if that new input terminates
                modified_list = deepcopy(parsed_instr)
                modified_list[current_step] = ["nop", instr_val, 1]
                find_acc_value(modified_list, current_step + 1, acc, True)
            
                
        elif instr == "nop":
            delta = 1
            if not swapped_instr and instr_val != 0:
                # flip this instr to jmp IF val != 0
                modified_list = deepcopy(parsed_instr)
                modified_list[current_step] = ["jmp", instr_val, 1]
                find_acc_value(modified_list, current_step + instr_val, acc, True)
        parsed_instr[current_step][2] += 1
        current_step += delta

    # print(f"Program will loop infinitely.\nAccumulator: {acc}\n")

if __name__ == "__main__":
    with open("input8.txt","r") as f:
        instructions = parse_instructions(f.readlines())
    find_acc_value(instructions)
    
