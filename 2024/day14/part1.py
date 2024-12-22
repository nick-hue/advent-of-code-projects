from dataclasses import dataclass
from typing import Tuple, List
import inspect

@dataclass
class RobotMovement:
    pos: List[int]
    vel: List[int]
    last_pos: List[int]


class App():
    def __init__(self):
        self.input_data = []
        self.robot_board = []

    def read_from_file(self, filename="input.txt"):
        with open(filename, "r") as f:
            data = [line.strip() for line in f.readlines()]
        self.input_data = data

    def print_var_name(self, var):
        for name, value in locals().items():  # Or use locals() if inside a function
            if value is var:
                print(f"I am now printing '{name}', its value is {value}")
                break

    def get_robot_movement(self):
        movements = []
        for line in self.input_data:
            pos, vel = line.split(" ")
            pos, vel = pos.replace("p=", "").split(","), vel.replace("v=", "").split(",")
            # pos = (int(pos[0]), int(pos[1]))
            # pos = (int(pos[1]), int(pos[0]))
            pos = [int(pos[1]), int(pos[0])]

            # vel = (int(vel[0]), int(vel[1]))
            # vel = (int(vel[1]), int(vel[0]))
            vel = [int(vel[1]), int(vel[0])]

            movements.append(RobotMovement(pos=pos, vel=vel, last_pos=[None, None]))
            
        return movements


    def draw_board(self):
        print("  "+"".join([str(num) for num in range(self.COLUMNS)]))
        for i, line in enumerate(self.robot_board):
            print(i, end = " ")
            for j, num in enumerate(line):    
                if num == 0:
                    print(".", end = "")
                else: 
                    print(num, end = "")
            print()
        print()


    def move_robot(self, data:RobotMovement):
        # print(f"{data.pos[0]},{data.pos[1]}")
        if data.last_pos[0] is not None and data.last_pos[1] is not None:
            self.robot_board[data.last_pos[0]][data.last_pos[1]] -= 1

        self.robot_board[data.pos[0]][data.pos[1]] += 1

        # self.robots[robot_index].pos[0] += data.vel[0] % self.ROWS
        # self.robots[robot_index].pos[1] += data.vel[1] % self.COLUMNS
        
        # robots[robot_index].pos[0] = (data.pos[0] + data.vel[0]) % self.ROWS
        # robots[robot_index].pos[1] = (data.pos[1] + data.vel[1]) % self.COLUMNS
        # robots[robot_index].last_pos[0] = data.pos[0] 
        # robots[robot_index].last_pos[1] = data.pos[1] 
        
        # self.robots[robot_index].pos[0] = (data.pos[0] + data.vel[0]) % self.ROWS
        # self.robots[robot_index].pos[1] = (data.pos[1] + data.vel[1]) % self.COLUMNS
        # self.robots[robot_index].last_pos[0] = data.pos[0] 
        # self.robots[robot_index].last_pos[1] = data.pos[1] 

        # update last position for next step
        data.last_pos[0] = data.pos[0]
        data.last_pos[1] = data.pos[1]

        # update position for next step
        data.pos[0] = (data.pos[0] + data.vel[0]) % self.ROWS
        data.pos[1] = (data.pos[1] + data.vel[1]) % self.COLUMNS    


    def simulate_movement_example(self, data: RobotMovement):
        seconds = 0
        last_pos_x = data.pos[0]
        last_pos_y = data.pos[1]

        print(data)
        while seconds <= 5:
            # print(f"{last_pos_x%self.COLUMNS} {last_pos_x=}")

            robot_x = last_pos_x 
            robot_y = last_pos_y 
            print(f"{robot_x},{robot_y}")

            # update robots location
            self.robot_board[robot_x][robot_y] += 1

            # draw board at current state
            if seconds == 0:
                print("Initial state:")
            else: 
                print(f"After {seconds} seconds")
            self.draw_board()

            # robot step
            last_pos_x = (last_pos_x + data.vel[0]) % self.ROWS
            last_pos_y = (last_pos_y + data.vel[1]) % self.COLUMNS
            
            # clear last location
            self.robot_board[robot_x][robot_y] -= 1

            seconds += 1

    def get_quadrant(self, vertical:str , horizontal:str) -> list:
        mid_row = self.ROWS // 2
        mid_col = self.COLUMNS // 2

        # print(f"{mid_row=} {mid_col=}")

        result = []
        for i, line in enumerate(self.robot_board):
            tmp_list = []
            for j, num in enumerate(line):
                if vertical == "top":
                    if horizontal == "left":
                        if i < mid_row and j < mid_col:
                            tmp_list.append(num)
                    elif horizontal == "right":
                        if i < mid_row and j > mid_col:
                            tmp_list.append(num)
                    else:
                        print("error")
                        return None
                elif vertical == "bottom":
                    if horizontal == "left":
                        if i > mid_row and j < mid_col:
                            tmp_list.append(num)
                    elif horizontal == "right":
                        if i > mid_row and j > mid_col:
                            tmp_list.append(num)
                    else:
                        print("error")
                        return None
                else:
                    print('ERROR')

            result.append(tmp_list)
        result = [lst for lst in result if lst]

        # print(f"{result=}")
        return result

    def draw_quadrant(self, quad):
        for line in quad:
            for char in line:
                if char == 0:
                    print('.', end = '')
                else:
                    print(char, end = '')
            print()
        print()
    
    def process_quadrants(self, quadrants):
        for quad_name, quad_value in quadrants.items():  # Using a dictionary to pass name-value pairs
            self.print_var_name(quad_name, quad_value)
            self.draw_quadrant(quad_value)

    def solve(self):
        # self.read_from_file("input_small.txt")
        # self.ROWS = 7
        # self.COLUMNS = 11
        self.read_from_file()
        self.ROWS = 103
        self.COLUMNS = 101

        # print(f"{self.input_data=}")      
        print(f"{self.ROWS=} {self.COLUMNS=}")

        # Simulation for robot movement for example part
        # data = RobotMovement(pos=[4,2], vel=[-3,2], last_pos=[None, None])
        # self.simulate_movement_example(data)
        
        # Get movement data of robots
        self.robots = self.get_robot_movement()
        self.robot_board = [[0 for _ in range(self.COLUMNS)]\
                                for _ in range(self.ROWS)]

        # print(self.robot_board)

        seconds = 0
        while seconds < 101:
            for robot in self.robots:
            # for robot in [self.robots[-2]]:
                print(robot)
                self.move_robot(robot)
            print()
            seconds += 1
        print(seconds)
        self.draw_board()


        # split the board into quadrants
        top_left_quad = self.get_quadrant(vertical="top", horizontal="left")
        top_right_quad = self.get_quadrant(vertical="top", horizontal="right")
        bottom_left_quad = self.get_quadrant(vertical="bottom", horizontal="left")
        bottom_right_quad = self.get_quadrant(vertical="bottom", horizontal="right")
        
        
        quadrants = [top_left_quad, top_right_quad, bottom_left_quad, bottom_right_quad]

        # display quadrants
        print("Displaying quadrants...")
        for quad in quadrants:
            self.draw_quadrant(quad=quad)
        
        total = 0
        robots_amonut_per_quad = []
        for quad in quadrants:
            tmp_nums = []
            for nums in quad:
                tmp_nums.append(sum(nums))
            robots_amonut_per_quad.append(sum(tmp_nums))
        print(f"{robots_amonut_per_quad=}")


        safety_factor = 1
        for robot_amount in robots_amonut_per_quad:
            safety_factor *= robot_amount
        
        print(f"total amount = {safety_factor}")



if __name__ == "__main__":
    App().solve()

