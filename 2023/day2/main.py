#  12 red cubes, 13 green cubes, and 14 blue cubes

with open("input.txt", "r") as f:
    data = [item.strip("\n") for item in f.readlines()]

def isPullPossible(dict):
    if int(dict['red']) <= 12 and int(dict['green']) <= 13 and int(dict['blue']) <= 14:
        return True
    return False

valid_games = []
for current_game in data:
    game_id = int(current_game.split(":")[0].split(" ")[1])
    sets = current_game.split(":")[1].split(";")

    current_data_dict = {
        'game_id': game_id,
        'red': 0,
        'green': 0,
        'blue': 0,
        'isPossible': False
    }

    for set in sets:
        set_info = set.split(",")
        for pull in set_info:
            number, color = pull.split(' ')[1:]
            current_data_dict[color]+=int(number)

    current_data_dict['isPossible'] = isPullPossible(current_data_dict)

    if (current_data_dict['isPossible']):
        print(current_data_dict)
        valid_games.append(current_data_dict['game_id'])

print(valid_games)
total = sum(valid_games)
print(total)
