import operator as op

def get_maps(input_data):
    list_of_maps = []
    current_map = []

    for line in input_data:
        if 'map:' in line:
            if current_map:
                list_of_maps.append(current_map)
                current_map = []
        else:
            current_map.append(line)
    
    if current_map: 
        list_of_maps.append(current_map)

    return list_of_maps

with open("input.txt") as f:
    data = [item.strip("\n") for item in f.readlines() if item.strip("\n")!='']

seeds = data[0].split(":")[1].strip().split(" ")

input_data = data[1:]

list_of_maps = get_maps(input_data)

range_map_list = []
for map in list_of_maps:
    map_name = map[0]
    map_info = map[1:]
    #print(f"Name: {map_name} | Info: {map_info}")
    
    range_maps = []
    for line in map_info:
        dest, source, length = line.split(" ")
        #print(f"Destination: {dest} | Source: {source} | Length: {length}")

        dest_range = list(range(int(dest), int(dest)+int(length), 1))
        source_range = list(range(int(source), int(source)+int(length), 1))

        range_map = (list(zip(dest_range, source_range)))
        range_maps.append(range_map)
    range_map_list.append(range_maps)

locations = []
for seed in seeds:
    coming_source = int(seed)
    for range_maps in range_map_list:
        for map in range_maps:
            for pair in map:
                dst, src = pair
                if src == coming_source:
                    coming_source = dst
                    break
            else:
                continue
            break
    locations.append(coming_source)

lowest_location = min(locations)
print(lowest_location)