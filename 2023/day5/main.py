import operator as op

def get_maps(input_data):
    list_of_maps = [[],[],[],[],[],[],[]]

    list_index = 0
    i = 0
    while (list_index < 7) and (i != len(input_data)+1):
        if op.contains(input_data[i], '-'):
            while True:
                list_of_maps[list_index].append(input_data[i])
                i+=1
                try: 
                    if op.contains(input_data[i], '-'):
                        list_index+=1
                        i-=1
                        break
                except IndexError:
                    break
        i+=1
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