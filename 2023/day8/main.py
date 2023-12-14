
with open("input.txt") as f:
    data = [item.strip("\n") for item in f.readlines() if item.strip("\n")!='']

sequence = data[0]
print(f"Sequence: {sequence}")

instructions_dict = [{'source': instruction.split(" = ")[0], 'L':instruction.split(" = ")[1][1:4], 'R':instruction.split(" = ")[1][6:9]} for instruction in data[1:]]
print(instructions_dict)

source = 'AAA'
steps_count = 0

while source != 'ZZZ':
    current_seq = sequence[steps_count%len(sequence)]
    
    print(f"Source: {source} | Order: {current_seq}")

    for instruction in instructions_dict:
        if source == instruction['source']:
            source = instruction[current_seq]
            steps_count += 1
            break

print(f"Steps: {steps_count}") 