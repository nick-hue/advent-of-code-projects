
def get_correct_node(instruction, instructions_dict):
    for instr in instructions_dict:
        print(f"{instruction} | {instr}")
        if instr['source'] == instruction:
            print('HERE')
            print()
            return instr

    return None

with open("input2.txt") as f:
    data = [item.strip("\n") for item in f.readlines() if item.strip("\n")!='']

sequence = data[0]
print(f"Sequence: {sequence}")

instructions_dict = [{'source': instruction.split(" = ")[0], 'L':instruction.split(" = ")[1][1:4], 'R':instruction.split(" = ")[1][6:9]} for instruction in data[1:]]
print(instructions_dict)

traverse_nodes = [node for node in instructions_dict if node['source'].endswith('A')]
print(traverse_nodes)

steps_count = 0 

while 1:
    current_seq = sequence[steps_count%len(sequence)]
    print(current_seq)

    switch_nodes = []
    for node in traverse_nodes:

        #print(f"Source: {node['source']} | Order: {current_seq}")
        print(f"Step: {steps_count}| order : {current_seq} | {traverse_nodes}hh")

        for instruction in instructions_dict:
            if node['source'] == instruction['source']:
                correct_node = get_correct_node(instruction[current_seq], instructions_dict)
                switch_nodes.append(correct_node)
                print(correct_node)
                #print(f"Node: {node}")
                break
    steps_count += 1

    traverse_nodes = switch_nodes
    
    print(f"Step: {steps_count}| order : {current_seq} | {traverse_nodes}")
    if all(node['source'].endswith('Z') for node in traverse_nodes):
        break
    
