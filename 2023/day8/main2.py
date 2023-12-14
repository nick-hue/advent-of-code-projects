
with open("input2.txt") as f:
    data = [item.strip("\n") for item in f.readlines() if item.strip("\n")!='']

sequence = data[0]
print(f"Sequence: {sequence}")

instructions_dict = [{'source': instruction.split(" = ")[0], 'L':instruction.split(" = ")[1][1:4], 'R':instruction.split(" = ")[1][6:9]} for instruction in data[1:]]
print(instructions_dict)