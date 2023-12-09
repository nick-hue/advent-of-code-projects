import re

with open("input.txt") as f:
    data = [item.strip("\n") for item in f.readlines()]
    #print(data)

def isPart(character):
    #print(f"Character: {character}")
    if character == "." or character.isdigit():
        #print("Not a part.")
        return False
    #print("Is part")
    return True

def is_adjacent_to_part(data, line_number, index):
    
    for i in range(line_number-1, line_number+2):
        for j in range(index-1, index+2):
            try:
                if isPart(data[i][j]):
                    return True
            except IndexError:
                pass
    return False

numbers = []
for line_number, line in enumerate(data):
    tmp = re.findall(r'\d+', line)
    mapping = list(map(int, tmp))
    if mapping:
        for number in mapping:
            numbers.append(number)
print(numbers)

part_numbers = []
for number in numbers:
    for line_number, line in enumerate(data):
        if str(number) in line:
            #print(f"{number} exists in line : {line_number}") 
            for digit in str(number):
                index = line.find(digit)
                if is_adjacent_to_part(data, line_number, index):
                    part_numbers.append(number)
                    break
    
print(part_numbers)
# mporei na metrisei 2 fores to idio noumero

total = sum(part_numbers)
print(total)