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


    def read_from_file(self, filename="input.txt"):
        with open(filename, "r") as f:
            data = [line.strip() for line in f.readlines()]
        all_data = [list(line) for line in data]
        split_index = all_data.index([])
        self.map, self.instructions = all_data[:split_index], [ins for line in all_data[split_index+1:] for ins in line]


    def update_map(self, entity: Entity):
        '''
        updates map: sets the new location for the entity supplied and deletes the old one
        '''
        self.map[entity.pos.x][entity.pos.y] = entity.character
        if entity.last_pos.x:
            self.map[entity.last_pos.x][entity.last_pos.y] = "."


    def draw_map(self):
        for line in self.map:
            print("".join(line))
        print()


    def get_boxes_indeces(self, new_point_x, new_point_y, direction) -> list[int]:
        '''
        returns a list of indeces where the boxes that should be moved are in the big boxes list
        '''
        current_char = "O"
        current_x = new_point_x
        current_y = new_point_y

        boxes: list[Point] = []
        while current_char == "O":
            boxes.append(Point(current_x, current_y))
            
            current_x += direction[0]
            current_y += direction[1]
            current_char = self.map[current_x][current_y]

        # if the boxes are next to a wall dont move them 
        if current_char == "#":
            return None
        
        box_indeces = [i for box in boxes for i, other_box in enumerate(self.boxes) if other_box.pos == box]
        
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
        self.update_map(entity)

    def handle_box(self, new_point_x, new_point_y, direction):
        # get boxes in front of robot
        boxes_ind = self.get_boxes_indeces(new_point_x, new_point_y, direction)
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
            self.move_entity(entity=box, direction=direction)
    
        # move robot
        self.move_entity(entity=self.robot, direction=direction)
    

    def move(self, direction) -> None:
        '''
        moves the robot in the supplied direction if possible
        '''
        print(direction)
    
        new_point_x, new_point_y = self.robot.pos.x + direction[0], self.robot.pos.y + direction[1]

        if self.map[new_point_x][new_point_y] == "#": # run into a wall
            print("wall")
            return
        elif self.map[new_point_x][new_point_y] == "O": # run into a box 
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
        self.draw_map()

        for i, ins in enumerate(self.instructions):
            # make movement
            current_direction = self.directions[ins]
            self.move(current_direction)

            # draw map
            print(f"Move {ins}:")
            self.draw_map()

    def get_original_robot_position(self) -> Entity:
        for i, line in enumerate(self.map):
            for j, char in enumerate(line):
                if char == "@":
                    return Entity(pos=Point(i, j), last_pos=Point(None, None), character="@")
        return None

    def get_original_box_positions(self) -> list[Entity]:
        return [Entity(pos=Point(i,j), last_pos=Point(None, None), character="O") for i, line in enumerate(self.map) for j, char in enumerate(line) if char == "O"]


    def solve(self):
        # self.read_from_file("input_small.txt")
        self.read_from_file()
        
        self.robot = self.get_original_robot_position()
        self.boxes = self.get_original_box_positions()
        print(f"{self.robot=}")
        print(f"{self.boxes=}")

        print(f"{self.instructions=}")       

        self.simulate_movement()

        total = 0
        for box in self.boxes:
            print(box)
            total += box.pos.x * 100 + box.pos.y

        print(f"total is {total}")


if __name__ == "__main__":
    App().solve()

