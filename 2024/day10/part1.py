from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int
    value: int    

class App():
    def __init__(self):
        self.input_data = []
        self.directions = {
            'up': (-1, 0),
            'down': (1, 0),
            'right': (0, 1),
            'left': (0, -1),
        }
        
    def read_from_file(self, filename="input.txt"):
        with open(filename, "r") as f:
            data = [line.strip() for line in f.readlines()]
        self.input_data = [[Point(i, j, int(item)) for j, item in enumerate(list(line)) if item != '.'] \
                                                for i, line in enumerate(data)]

    def display_map(self):
        print("   "+" ".join(list(map(str, range(len(self.input_data))))))
        print("-"*3*len(self.input_data))
        for i, line in enumerate(self.input_data):
            print(f"{i:<}", end = "| ")
            for point in line:
                print(point.value, end = " ")
            print("| ")
        print("-"*3*len(self.input_data))

    def is_point_inbounds(self, point):
        '''
        returns combination of x and y are inside the bounds of the map
        '''
        return 0 <= point.x < len(self.input_data) and 0 <= point.y < len(self.input_data[0])

    def trail_stop(self, point, visited) -> list[str]:
        '''
        returns a list of valid new points that the trail can continue
        if there are none returns an empty list
        '''
        possible_paths = []
        # print(f"Current {point}")
        for key, value in self.directions.items():
            # print(f"{key} -> {value}")
            new_point_x, new_point_y = point.x + value[0], point.y + value[1]
            # print(f"{new_point_x},{new_point_y}")
            try:
                new_point_value = self.input_data[new_point_x][new_point_y].value
            except IndexError: # this can replace the check if the point is inbounds
                continue

            new_point = Point(new_point_x, new_point_y, new_point_value)

            if new_point in visited:
                continue

            if (new_point.value - point.value) != 1 or not self.is_point_inbounds(point):
                continue
            else:                
                possible_paths.append(new_point)

        return possible_paths
            
    def simulate_trail(self, point, visited):
        # trail loop
        if point in visited: return 0
        visited.append(point)
        
        # trail path end, valid path !
        if point.value == 9: return 1

        # trail cant continue, invalid path !
        new_points = self.trail_stop(point, visited)
        if len(new_points) < 1: return 0 
        
        total = 0
        for p in new_points:
            # print(f"New point {p=}")
            total += self.simulate_trail(p, visited)
        
        # print(f"From {point} we got {total} paths")
        visited.remove(point)
        return total


    def calculate_valid_trails(self, trailhead) -> int:
        '''
        returns the number of trails for the specified trailhead
        '''
        return self.simulate_trail(trailhead, [])

        

    def solve(self):
        # self.read_from_file("input_small.txt")
        # self.read_from_file("2024/day10/input_small.txt")
        self.read_from_file()
        # print(f"{self.input_data=}")   
        self.display_map()


        trailhead_indeces = [point for line in self.input_data for point in line if point.value == 0]
        # print(f"{trailhead_indeces=}")
        total = 0 
        for trailhead in trailhead_indeces:
            tmp_total = self.calculate_valid_trails(trailhead)
            print(f"For {trailhead=} we got {tmp_total=}")

            total += tmp_total
        print(f"{total=}")



if __name__ == "__main__":
    App().solve()
