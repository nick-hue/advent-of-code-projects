import operator as op

with open("input.txt", "r") as f:
    data = [item.strip("\n") for item in f.readlines()]

numbers_dic = {
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

number_list = []
for line in data:
    # make string numbers into digits "one" -> 1
    change_string = line 

    for key in list(numbers_dic.keys()):
        if op.contains(change_string, key):
            index = change_string.index(key)
            change_string = change_string[:index] + key[0] + str(numbers_dic[key]) + change_string[index:]
            print(change_string)

    print(f"Change : {change_string}")
    first = None
    last = None 
    for character in change_string: 
        if character.isdigit():
            if first is None:
                first = character
            else:
                last = character
    if last is None:
        last = first
    number_list.append(int(f"{first}{last}"))

total = sum(number_list)
print(number_list)
print(f"Total is: {total}")