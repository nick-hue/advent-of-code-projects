from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

@dataclass
class Entity:
    pos: Point
    last_pos: Point
    character: str    

@dataclass
class BoxPoint:
    left: Point
    right: Point

@dataclass
class Box:
    pos: BoxPoint
    last_pos: BoxPoint
    left_char: str
    right_char: str

class App():
    def __init__(self):
        self.map = []
        self.instructions = []
        self.directions = {
            '^' : (-1,0),
            'v' : (1,0),
            '>' : (0,1),
            '<' : (0,-1)
        }
        self.vertical_dirs = [(-1,0), (1,0)]
        self.horizontal_dirs = [(0,1), (0,-1)]
        self.box_chars = ['[',']']


    def read_from_file(self, filename="input.txt"):
        with open(filename, "r") as f:
            data = [line.strip() for line in f.readlines()]
        all_data = [list(line) for line in data]
        split_index = all_data.index([])
        self.map, self.instructions = all_data[:split_index], [ins for line in all_data[split_index+1:] for ins in line]


    def update_map(self, mapp, entity: Entity):
        '''
        updates map: sets the new location for the entity supplied and deletes the old one
        '''
        mapp[entity.pos.x][entity.pos.y] = entity.character
        if entity.last_pos.x:
            mapp[entity.last_pos.x][entity.last_pos.y] = "."

    def update_map_box(self, mapp, box:Box, direction: tuple[int,int]):
        '''
        updates map: sets the new location for the entity supplied and deletes the old one
        '''
            
        mapp[box.pos.left.x][box.pos.left.y] = box.left_char
        mapp[box.pos.right.x][box.pos.right.y] = box.right_char

        if box.last_pos.left.x:
            if direction in self.horizontal_dirs: # coming from left >
                return
            else:
                mapp[box.last_pos.left.x][box.last_pos.left.y] = "."
                mapp[box.last_pos.right.x][box.last_pos.right.y] = "."





    def draw_map(self, mapp):
        for line in mapp:
            print("".join(line))
        print()


    def get_boxes_indeces(self, mapp, new_point_x, new_point_y, direction) -> list[int]:
        '''
        returns a list of indeces where the boxes that should be moved are in the big boxes list
        '''

        current_char = mapp[new_point_x][new_point_y]
        
        if current_char == "[":
            check_pos = [(new_point_x, new_point_y), (new_point_x, new_point_y+1)]
        elif current_char == "]":
            check_pos = [(new_point_x, new_point_y-1), (new_point_x, new_point_y)]
        else:
            check_pos = None
            print("error !!!")
        print(f"{check_pos=}")

        boxes: list[BoxPoint] = []

        while mapp[check_pos[0][0]][check_pos[0][1]] in self.box_chars or mapp[check_pos[1][0]][check_pos[1][1]] in self.box_chars:
            tmp_pos = []
            for check_x, check_y in check_pos:
                print(f"{check_x},{check_y}")
                if mapp[check_x][check_y] == '[':
                    boxes.append(BoxPoint(left=Point(check_x, check_y), right=Point(check_x,check_y+1)))
                else:
                    boxes.append(BoxPoint(left=Point(check_x, check_y-1), right=Point(check_x, check_y)))
            
                if direction in self.vertical_dirs: # if we are coming from a vertical direction -> normal increment
                    print('from the top or bottom')
                    updated_x = check_x + direction[0]
                    updated_y = check_y + direction[1]
                else:   # if we are coming from the side we want double direction to leave the object
                    print('from the side')
                    updated_x = check_x + direction[0]
                    updated_y = check_y + direction[1]

                tmp_pos.append((updated_x, updated_y))
                
            check_pos = tmp_pos

        # if the boxes are next to a wall dont move them 
        if  check_pos[0] == "#" or check_pos[1] == "#":
            print("cant move boxes")
            return None
        
        print(f"{boxes=}")
        box_indeces = list(set([i for box in boxes for i, other_box in enumerate(self.boxes) if other_box.pos == box]))
        
        return box_indeces

    def move_entity(self, entity: Entity, direction: tuple[int,int]) -> None:
        '''
        moves the supplied entity and '''
        # update last position to next position
        entity.last_pos.x = entity.pos.x
        entity.last_pos.y = entity.pos.y

        # update current pos to new position
        entity.pos.x += direction[0]
        entity.pos.y += direction[1]

        # update map for current box
        self.update_map(self.resized_map, entity)


    def move_box(self, box:Box, direction):
        print(box)

        box.last_pos.left.x = box.pos.left.x
        box.last_pos.left.y = box.pos.left.y
        box.last_pos.right.x = box.pos.right.x
        box.last_pos.right.y = box.pos.right.y

        box.pos.left.x += direction[0]
        box.pos.left.y += direction[1]
        box.pos.right.x += direction[0]
        box.pos.right.y += direction[1]
        self.update_map_box(self.resized_map, box, direction)


    def handle_box(self, new_point_x, new_point_y, direction):
        # get boxes in front of robot
        boxes_ind = self.get_boxes_indeces(self.resized_map, new_point_x, new_point_y, direction)
        print(f"{boxes_ind=}")
        # print(f"{self.boxes}")

        # if its empty it means the boxes hit a wall so dont move
        if not boxes_ind:
            return

        # move boxes 
        for i in reversed(boxes_ind):
            # get current box
            box = self.boxes[i]
            # move current box
            self.move_box(box=box, direction=direction)
    
        # move robot
        self.move_entity(entity=self.robot, direction=direction)
    

    def move(self, mapp, direction) -> None:
        '''
        moves the robot in the supplied direction if possible
        '''
        print(direction)
    
        new_point_x, new_point_y = self.robot.pos.x + direction[0], self.robot.pos.y + direction[1]

        if mapp[new_point_x][new_point_y] == "#": # run into a wall
            print("wall")
            return
        elif mapp[new_point_x][new_point_y] == "[" or mapp[new_point_x][new_point_y] == "]": # run into a box 
            print("box")
            self.handle_box(new_point_x, new_point_y, direction)
        else: # normal movement
            print("normal")
            # update last pos
            self.move_entity(entity=self.robot, direction=direction)
            
        

    def simulate_movement(self) -> None:
        '''
        function that simulates the movement of the robot
        '''
        print("Initial state:")
        self.draw_map(self.resized_map)

        for i, ins in enumerate(self.instructions):
            # make movement
            current_direction = self.directions[ins]
            self.move(self.resized_map, current_direction)

            # draw map
            print(f"Move {ins}:")
            self.draw_map(self.resized_map)

    def get_original_robot_position(self, mapp) -> Entity:
        for i, line in enumerate(mapp):
            for j, char in enumerate(line):
                if char == "@":
                    return Entity(pos=Point(i, j), last_pos=Point(None, None), character="@")
        return None

    def get_original_box_positions(self, mapp) -> list[Box]:
        return [Box(pos=BoxPoint(left=Point(i,j), right=Point(i,j+1)), \
                    last_pos=BoxPoint(left=Point(None, None), right=Point(None, None)),
                    left_char='[',
                    right_char=']') for i, line in enumerate(mapp) for j, char in enumerate(line) if char == "["]


    def get_new_map(self):
        
        resized_map = []
        
        for line in self.map:
            tmp_list = []
            for char in line:
                output_char = ''
                if char == "O":
                    output_char = ["[", "]"]
                elif char == "#" or char == ".":
                    output_char = [f"{char}",f"{char}"]
                else:
                    output_char = ["@","."]
                tmp_list.extend(output_char)
            resized_map.append(tmp_list)
        

        return resized_map



    def solve(self):
        self.read_from_file("input_small.txt")
        # self.read_from_file()
        self.resized_map = self.get_new_map()
        
        self.draw_map(self.resized_map)


        self.robot = self.get_original_robot_position(self.resized_map)
        self.boxes = self.get_original_box_positions(self.resized_map)

        print(f"{self.robot=}")
        # print(f"{self.boxes=}")

        for box in self.boxes:
            print(box)


        print(f"{self.instructions=}")       

        self.simulate_movement()

        # total = 0
        #     total += box.pos.x * 100 + box.pos.y

        # print(f"total is {total}")


if __name__ == "__main__":
    App().solve()

