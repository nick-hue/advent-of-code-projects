import re

with open("input.txt", "r") as f:
    data = [item.strip("\n") for item in f.readlines()]

numbers_dict = {
    'one':1,
    'two':2,
    'three':3,
    'four':4,
    'five':5,
    'six':6,
    'seven':7,
    'eight':8,
    'nine':9,
}


def transfrom_line(line):
    number_list = []
    for key, value in list(numbers_dict.items()):
        matches = re.finditer(key, line)
        
        for match in matches:
            span_median = (match.span()[0]+match.span()[1])/2
            number_list.append((match.group(), span_median))

        matches_value = re.finditer(str(value), line)

        for match in matches_value:
            number_list.append((match.group(), match.start()))

    sorted_number_list = sorted(number_list, key = lambda x : x[1])
    final_numbers = []
    for number,_ in sorted_number_list:
        if number in numbers_dict.keys():
            final_numbers.append(numbers_dict[number])
        else:
            final_numbers.append(int(number))

    print(final_numbers)
    result = int(str(final_numbers[0])+str(final_numbers[-1]))
    return result

total = 0
for line in data:
    total += transfrom_line(line)
print(f"Total: {total}")

