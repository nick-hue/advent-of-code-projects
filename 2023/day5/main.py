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
print(seeds)

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

print("LEN", len(range_map_list))

seed = seeds[0]
range_map_index = 0
dest = coming_source = int(seed)
while (range_map_index < 7):
    print(f"Name: {list_of_maps[range_map_index][0]} | Info: {list_of_maps[range_map_index][1:]}")
    print(f"Coming: {coming_source}")
    
    for map in range_map_list[range_map_index]:
        found = False
        #print(f"Map: {map}")
        for dest, src in map:
            if coming_source == src:
                print(f"Source {src} -> dest {dest}")
                print("HERE\n")
                coming_source = dest
                range_map_index+=1
                found = True
                break
        if not found:
            range_map_index+=1
    
    
print(dest)