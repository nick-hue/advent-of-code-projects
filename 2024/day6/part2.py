import time 
import os
import sys
import copy

class App():
    def __init__(self):
        self.input_data = []
        self.step_matrix = []
        self.guard_row, self.guard_col = 0, 0
        self.guard_symbol = "^"
        self.guard_direction = "up"
        self.guard_symbol_dict = {
            'up' : '^',
            'right' : '>',
            'down' : 'v',
            'left' : '<'
        }
        self.path_symbol = {
            'up' : '|',
            'right' : '-',
            'down' : '|',
            'left' : '-'
        }
        self.guard_direction_seq = list(self.guard_symbol_dict.keys())

    def read_from_file(self, filename="input.txt"):
        with open(filename, "r") as f:
            data = [line.strip() for line in f.readlines()]
        self.input_data = [list(word) for word in data]

    def get_starting_guard_pos(self, map):
        for i, line in enumerate(map):
            # print(line)
            for j, char in enumerate(line):
                if char == self.guard_symbol:
                    # print("found")
                    return i, j

        print("Error position not found")
        return -1, -1

    def move_guard(self, map):
        try:
            self.step_matrix[self.guard_row][self.guard_col] = True

            if map[self.guard_row][self.guard_col] != "+":
                map[self.guard_row][self.guard_col] = self.path_symbol[self.guard_direction]

            match self.guard_direction:
                case "up":
                    self.guard_row -=1
                case "right":
                    self.guard_col +=1
                case "down":
                    self.guard_row +=1
                case "left":
                    self.guard_col -=1
                case _:
                    print("Error with guard direction")

            map[self.guard_row][self.guard_col] = self.guard_symbol
        except IndexError:
            return


    def check_obstacle(self, map) -> bool:
        obstacle_seen = False
        try:
            match self.guard_direction:
                case "up":
                    if map[self.guard_row-1][self.guard_col] == "#" or map[self.guard_row-1][self.guard_col] == "O":
                        obstacle_seen = True
                case "right":
                    if map[self.guard_row][self.guard_col+1] == "#" or map[self.guard_row][self.guard_col+1] == "O":
                        obstacle_seen = True
                case "down":
                    if map[self.guard_row+1][self.guard_col] == "#" or map[self.guard_row+1][self.guard_col] == "O":
                        obstacle_seen = True
                case "left":
                    if map[self.guard_row][self.guard_col-1] == "#" or map[self.guard_row][self.guard_col-1] == "O":
                        obstacle_seen = True
                case _:
                    print("No obstacle seen")
                    obstacle_seen = False
                    pass
        except IndexError:
            # print("Guard left the map")
            pass            

        return obstacle_seen

    def draw_map(self, map):
        # Clear the terminal screen
        os.system('cls' if os.name == 'nt' else 'clear')  # Use 'cls' for Windows, 'clear' for others
        
        map_string = ""
        for line in map:
            map_string += ''.join(line) + "\n"
        map_string += f"Current position: {self.guard_row},{self.guard_col}\n"
        
        print(map_string)

    def is_guard_inbounds(self, map):
        return 0 <= self.guard_row < len(map[0]) and 0 <= self.guard_col < len(map)
        
    def turn_guard(self, map):
        # Get's next symbol in the rotation (turns 90 degrees), if last direction was left it goes back to up 
        index = self.guard_direction_seq.index(self.guard_direction)        

        # Get next index
        next_symbol = self.guard_direction_seq[(index+1)%(len(self.guard_direction_seq))]

        # update guard's symbol and direction
        self.guard_symbol = self.guard_symbol_dict[next_symbol]
        self.guard_direction = next_symbol
        map[self.guard_row][self.guard_col] = "+"

    def draw_position_map(self, draw):        
        map_string = ""
        count = 0

        for i, line in enumerate(self.input_data):
            for j, char in enumerate(self.input_data):
                if (i, j) in self.obstacle_indexes:
                    output_char = "#"
                elif self.step_matrix[i][j]:
                    output_char = "X"
                    count += 1
                else:
                    output_char = "."
                map_string+=output_char
            map_string+="\n"
 
        if draw:
            print(map_string)
        return count

    def does_enter_loop(self, map):
        self.guard_row, self.guard_col = self.get_starting_guard_pos(map)
        
        iter = 0
        while True:
            # if iter is bigger than dimension space break
            if iter > 260*260:
                return True
            # self.draw_map(map)

            if self.check_obstacle(map):  
                self.turn_guard(map)
                continue

            # move guard
            self.move_guard(map)            
            iter += 1

            # time.sleep(0.05)
            if not self.is_guard_inbounds(map):
                return False



    def solve(self):
        # self.read_from_file("input_small.txt")
        self.read_from_file()
        # print(f"{self.input_data=}")    
        copied_input = copy.deepcopy(self.input_data)

        self.step_matrix = [
            [False for _ in range(len(self.input_data[0]))]
            for _ in range(len(self.input_data))
        ]

        self.path = [
            ["." for _ in range(len(self.input_data[0]))]
            for _ in range(len(self.input_data))
        ]

        self.obstacle_indexes = [(self.input_data.index(line), line.index(character)) for line in self.input_data for character in line if character == "#"]

        self.guard_row, self.guard_col = self.get_starting_guard_pos(self.input_data)

        original_guard_row, original_guard_col = self.guard_row, self.guard_col
        step_counter = 0

        while self.is_guard_inbounds(self.input_data):
            # self.draw_map(self.input_data)

            # check if facing object 
            if self.check_obstacle(self.input_data):    # if yes turn right
                self.turn_guard(self.input_data)

            # move guard
            self.move_guard(self.input_data)

            step_counter += 1
            # time.sleep(0.3)
    
        # coords that the guard goes through
        path_coords = [(i,j) for i, line in enumerate(self.step_matrix) for j, value in enumerate(line) if value]
        # remove from the path coords the one where the guard started 
        del path_coords[path_coords.index((original_guard_row, original_guard_col))]
        
        # print(path_coords)
        
        loop_count = 0
        for (x,y) in path_coords:
            # print(f"Map for coords {x},{y}")
            self.guard_symbol = "^"
            self.guard_direction = "up"
            tmp_map = copy.deepcopy(copied_input)
            tmp_map[x][y] = "O"

            # for line in tmp_map:
            #     print("".join(line))
            # print("")
            if self.does_enter_loop(tmp_map):
                loop_count += 1 


        print(f"{loop_count=}")

            

if __name__ == "__main__":
    App().solve()
