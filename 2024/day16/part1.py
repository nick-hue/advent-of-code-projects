from typing import Tuple
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

@dataclass
class Path:
    score: int
    steps: list[Point]

class App():
    def __init__(self):
        self.map = []
        self.directions = {
            'up': ("^", (-1,0)),
            'down': ("v", (1,0)),
            'left': ("<", (0,-1)),
            'right': (">", (0,1)),
        }

    def read_from_file(self, filename="input.txt"):
        with open(filename, "r") as f:
            data = [line.strip() for line in f.readlines()]
        self.map = [list(line) for line in data]

    def get_start_end_points(self) -> tuple[Point,Point]:
        '''
        returns the i,j of the start and end points in the grid
        '''
        start: Point = None, None
        end: Point = None, None

        for i, line in enumerate(self.map):
            for j, char in enumerate(line):
                if char == "S":
                    start = Point(i,j)
                elif char == "E":
                    end = Point(i,j)

        if not start or not end:
            print("Error")
            return None, None
    
        return start, end
        
    
    def get_possible_points(self, point, path, direction):
        result = []
        for (symbol, (i,j)) in self.directions.values():
            new_point = self.map[point.x+i][point.y+j]
            # new point not a wall
            if new_point == "#": continue
            # dont go back to the previous point
            if new_point in path.steps: continue
            # allows for only clockwise and coutner clockwise turning
            if direction[0]+i == 0 or direction[1]+j == 0: continue 
            result.append((new_point, (i,j)))
        return result

    def step(self, point: Point, path: Path, direction: tuple[int,int]):
        
        new_points = self.get_possible_points(point, path, direction)
        print(new_points)
        if not new_points:
            return None        

        for p, current_dir in new_points:
            if p == self.end_point:
                return path
            
            path.steps.append(p)
            result_path = self.step(p, path, current_dir)
            if result_path:
                return result_path
            path.steps.pop(-1)


    def traverse(self):
        x = 0 
        while x < 5:
            path = self.step(point=self.start_point, path=Path(0, []), direction=(-1,0))  
            print(path)
            x+=1
        


    def solve(self):
        self.read_from_file("input_small.txt")
        #self.read_from_file()
        # print(f"{self.input_data=}")       

        for line in self.map:
            print("".join(line))

        self.start_point, self.end_point = self.get_start_end_points()

        print(f"{self.start_point=}")
        print(f"{self.end_point=}")

        score = self.traverse()

if __name__ == "__main__":
    App().solve()

