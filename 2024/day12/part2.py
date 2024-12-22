from dataclasses import dataclass
from typing import Tuple, List

@dataclass
class Region:
    letter: str
    area: int
    perimeter: int
    points: List[Tuple[int,int]]

class App():
    def __init__(self):
        self.input_data = []
        self.directions = {
            'up' : (-1,0),
            'down' : (1,0),
            'left' : (0,-1),
            'right' : (0,1),
        }

    def read_from_file(self, filename="input.txt"):
        with open(filename, "r") as f:
            data = [line.strip() for line in f.readlines()]
        self.input_data = [list(line) for line in data]

    def check_point_inbounds(self, x,y) -> bool:
        return 0 <= x < len(self.input_data) and 0 <= y < len(self.input_data[0])

    def has_big_diff(self, xi, xj, rest) -> bool:
        big_diff = False
        for (i,j) in rest:
            diffx = abs(xi-i)
            diffy = abs(xj-j)
            if diffx < 2 or diffy < 2:
                big_diff = True
                break

        return big_diff

    def get_perimeters(self, points, letter):

        perimeters = []
        for (i,j) in points:
            for key, (di, dj) in self.directions.items():
                ni, nj = i+di, j+dj
                if ni < 0 or ni >= len(self.input_data) or nj < 0 or nj >= len(self.input_data[0]) or self.input_data[ni][nj] != letter:
                    perimeters.append((ni,nj))

        return perimeters

    def calculate_side_number(self, points, letter):

        perimeters = self.get_perimeters(points, letter)
        print(perimeters)

        sides = 0
        checked = []
        for index, (xi,xj) in enumerate(perimeters):
            if not self.has_big_diff(xi,xj, perimeters[index:]) and (xi,xj) not in checked:
                sides += 1
                # print(xi,xj)
                checked.append((xi,xj))
                print(checked)
        
        print(sides)


        return 0        

    def make_region(self, i, j, letter) -> Region:
        
        points = [(i,j)]
        changed = True
        while True:
            if not changed:
                break 
            changed = False

            for point in points:
                for key, value in self.directions.items():
                    tmp_x, tmp_y = point[0]+value[0], point[1]+value[1]
                    if not self.check_point_inbounds(tmp_x, tmp_y):
                        continue
                    if (tmp_x, tmp_y) not in points and self.input_data[tmp_x][tmp_y] == letter:
                        points.append((point[0]+value[0], point[1]+value[1]))
                        changed = True

        sides = self.calculate_side_number(points, letter)

        return Region(letter=letter, area=len(points), perimeter=sides, points=points)

    
    def solve(self):
        self.read_from_file("input_small.txt")
        # self.read_from_file()
        # print(f"{self.input_data=}")       
        
        regions = []
        used_points = []
        for i, line in enumerate(self.input_data):
            # print("".join(line))
            for j, char in enumerate(line):
                if (i,j) not in used_points:
                    reg  = self.make_region(i, j, char)
                    regions.append(reg)
                    used_points.extend(reg.points)
            
        total = 0
        for reg in regions:
            # print(f"{reg=}")
            total += reg.area * reg.perimeter
        print(f"Total is {total}")



if __name__ == "__main__":
    App().solve()

