import re

with open("input.txt") as f:
    data = [item.strip("\n") for item in f.readlines()]
    #print(data)

def isPart(character):
    if character == "." or character.isdigit():
        return False
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

number_set = [(num, False) for num in numbers]
print(number_set)
results = []
for number, counted in number_set:
    for line_number, line in enumerate(data):
        if str(number) in line:
            for digit in str(number):
                index = line.find(digit)
                if is_adjacent_to_part(data, line_number, index) and not counted:
                    counted = True
                    results.append(number)
                    break
    
print(results)
# mporei na metrisei 2 fores to idio noumero
total = sum(results)
print(total)