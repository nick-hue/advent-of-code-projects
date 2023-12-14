import re

with open("input.txt") as f:
    data = [item.strip("\n") for item in f.readlines()]

def isPart(character):
    if character == "." or character.isdigit():
        return False
    return True

def is_adjacent(data, line_number, span):
    for i in range(line_number-1, line_number+2):
        if i < 0 or i == len(data): continue
        for j in range(span[0]-1, span[1]+1):  
            if j < 0 or j == len(data[0]):
                continue
            if isPart(data[i][j]):
                return True
            
    return False

def get_numbers(data):
    total = 0
    for line_number, line in enumerate(data):
        matches = re.finditer(r'\d+', line)

        for match in matches:
            if is_adjacent(data, line_number, match.span()):
                total += int(match.group())
    
    return total

total = get_numbers(data)
print(f"Part1: {total}")
    
def get_gear_ratio(data, line_number, index):
    numbers = []
    for i in range(line_number-1, line_number+2):
        matches = re.finditer(r'\d+', data[i])
        # print(f"Current line: {data[i]}")
        
        for match in matches:       # get the numbers for the current line
            print(f"Number: {match.group()} | Start: {match.start()} | end : {match.end()}")
            for check_index in range(index-1, index+2):
                if match.start() <= check_index <= match.end()-1:
                    numbers.append(int(match.group()))
                    break
    
    print(f"Numbers : {numbers}")
    if len(numbers) == 2:
        return numbers[0]*numbers[1]
    else:
        return -1
    
total = 0
for line_number, line in enumerate(data):
    matches = re.finditer(re.escape("*"), line)

    for match in matches:
        print(f"Gear: {match.group()} | line_number: {line_number} | start: {match.start()}")
        gear_ratio = get_gear_ratio(data, line_number, match.start())
        if gear_ratio!=-1:
            total+=gear_ratio
        print()

print(f"Part2: {total}")        