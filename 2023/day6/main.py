
with open("input.txt") as f:
    data = [item.strip("\n") for item in f.readlines()]


# part 1

times = [int(x) for x in data[0].split(" ")[1:] if x]
distances = [int(x) for x in data[1].split(" ")[1:] if x]

print(times)
print(distances)


# A time and a distance is a race
total = 1
for time, distance in zip(times, distances):
    winning_times = 0
    #print(f"Time: {time} | Distance {distance}")
    for seconds_pressed in range(time+1):
        speed = seconds_pressed
        distance_travelled = (time-seconds_pressed)*speed
        if distance_travelled > distance:
            winning_times+=1
        #print(f"For {seconds_pressed} seconds pressed, travelled : {distance_travelled}")
    #print(f"Winning times: {winning_times}")
    total *= winning_times

print(f"Part1 : {total}")

# part 2

race_time = int("".join([x for x in data[0].split(" ")[1:] if x]))
race_distance = int("".join([x for x in data[1].split(" ")[1:] if x]))

print(race_time)
print(race_distance)

# 14 to 71516
winning_times = 0
for seconds_pressed in range(14, race_time-13):
    speed = seconds_pressed
    distance_travelled = (race_time-seconds_pressed)*speed
    if distance_travelled > race_distance:
        winning_times+=1
print(f"Part2 : {winning_times}")