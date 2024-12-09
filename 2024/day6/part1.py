import time 
import os
import sys

class App():
    def __init__(self):
        self.input_data = []
        self.step_matrix = []
        self.guard_row, self.guard_col = 0, 0
        self.guard_symbol = "^"
        self.guard_direction = "up"
        self.guard_inbounds = True
        self.guard_symbol_dict = {
            'up' : '^',
            'right' : '>',
            'down' : 'v',
            'left' : '<'
        }
        self.guard_direction_seq = list(self.guard_symbol_dict.keys())

    def read_from_file(self, filename="input.txt"):
        with open(filename, "r") as f:
            data = [line.strip() for line in f.readlines()]
        self.input_data = [list(word) for word in data]

    def get_starting_guard_pos(self):
        for i, line in enumerate(self.input_data):
            # print(line)
            for j, char in enumerate(line):
                if char == self.guard_symbol:
                    # print("found")
                    return i, j

        print("Error position not found")
        return -1, -1

    def move_guard(self):
        try:

            self.step_matrix[self.guard_row][self.guard_col] = True

            self.input_data[self.guard_row][self.guard_col] = "."
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

            self.input_data[self.guard_row][self.guard_col] = self.guard_symbol
        except IndexError:
            return


    def check_obstacle(self) -> bool:
        obstacle_seen = False
        try:
            match self.guard_direction:
                case "up":
                    if self.input_data[self.guard_row-1][self.guard_col] == "#":
                        obstacle_seen = True
                case "right":
                    if self.input_data[self.guard_row][self.guard_col+1] == "#":
                        obstacle_seen = True
                case "down":
                    if self.input_data[self.guard_row+1][self.guard_col] == "#":
                        obstacle_seen = True
                case "left":
                    if self.input_data[self.guard_row][self.guard_col-1] == "#":
                        obstacle_seen = True
                case _:
                    print("No obstacle seen")
                    obstacle_seen = False
                    pass
        except IndexError:
            print("Guard left the map")
            self.guard_inbounds = False
            

        return obstacle_seen

    def draw_map(self):
        # Clear the terminal screen
        os.system('cls' if os.name == 'nt' else 'clear')  # Use 'cls' for Windows, 'clear' for others
        
        map_string = ""
        for line in self.input_data:
            map_string += ''.join(line) + "\n"
        map_string += f"Current position: {self.guard_row},{self.guard_col}\n"
        
        print(map_string)

    def is_guard_inbounds(self):
        return 0 <= self.guard_row < len(self.input_data[0]) and 0 <= self.guard_col < len(self.input_data)
        
    def turn_guard(self):
        # Get's next symbol in the rotation (turns 90 degrees), if last direction was left it goes back to up 
        index = self.guard_direction_seq.index(self.guard_direction)        

        # Get next index
        next_symbol = self.guard_direction_seq[(index+1)%(len(self.guard_direction_seq))]

        # update guard's symbol and direction
        self.guard_symbol = self.guard_symbol_dict[next_symbol]
        self.guard_direction = next_symbol

    def draw_position_map(self, draw):        
        map_string = ""
        count = 0

        obstacle_indexes = [(self.input_data.index(line), line.index(character)) for line in self.input_data for character in line if character == "#"]
        print(obstacle_indexes)

        for i, line in enumerate(self.input_data):
            for j, char in enumerate(self.input_data):
                if (i, j) in obstacle_indexes:
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


    def solve(self):
        # self.read_from_file("input_small.txt")
        self.read_from_file()
        # print(f"{self.input_data=}")    

        self.step_matrix = [
            [False for _ in range(len(self.input_data[0]))]
            for _ in range(len(self.input_data))
        ]

        self.guard_row, self.guard_col = self.get_starting_guard_pos()
        print(self.guard_row, self.guard_col)
        step_counter = 0

        while self.is_guard_inbounds():
            # self.draw_map()

            # check if facing object 
            if self.check_obstacle():    # if yes turn right
                self.turn_guard()

            # move guard
            self.move_guard()

            step_counter += 1
            # time.sleep(0.05)
        # self.draw_map()


        count = self.draw_position_map(True)
        from collections import Counter

        print(Counter([value for line in self.step_matrix for value in line]))
        print(f"{count=}")

            

if __name__ == "__main__":
    App().solve()
