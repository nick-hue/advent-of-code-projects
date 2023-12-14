
with open("input.txt", "r") as f:
    data = [item.strip("\n") for item in f.readlines()]

total = 0
for game in data:
    game_data = game.split(": ")[1]
    print(game_data)

    pulls = game_data.split("; ")
    max_dict = {
        'red':-1,
        'green':-1,
        'blue':-1
    }
    for pull in pulls:
        items_from_pull = pull.split(", ") 
        print(items_from_pull)
        for item in items_from_pull:
            amount, color = item.split(" ")
            if int(amount) > max_dict[color]:
                max_dict[color] = int(amount)
    
    print(max_dict.values())
    power = max_dict['red']*max_dict['green']*max_dict['blue']
    total += power

print(f"Total: {total}")