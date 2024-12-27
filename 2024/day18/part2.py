from dataclasses import dataclass
from collections import deque

# point :x is distance from the top
# point :y is distance from the left edge
@dataclass(frozen=True)
class Point:
    x: int
    y: int

class App():
    def __init__(self):
        self.input_data = []
        self.directions = {
            'up':(-1,0),
            'down':(1,0),
            'right':(0,1),
            'left':(0,-1),
        }

    def read_from_file(self, filename="input.txt"):
        with open(filename, "r") as f:
            data = [line.strip() for line in f.readlines()]
        self.input_data = [Point(int(pos.split(",")[1]), int(pos.split(",")[0])) for pos in data]

    def make_maze(self, rows, columns, bytes_num):
        '''
        makes map after specified number of bytes
        '''
        maze = []
        for i in range(rows):
            row = []
            for j in range(columns):
                point = Point(i,j)
                if point in self.input_data[:bytes_num]:
                    print_char = "#"
                else:
                    print_char = "."
                row.append(print_char)
            maze.append(row) 
        return maze      


    def draw_grid(self, grid):
        for line in grid:
            print("".join(line))


    def is_point_inbounds(self, maze, point: Point):
        return 0 <= point.x < len(maze) and 0 <= point.y < len(maze)

    def bfs(self, maze, start):
        queue = deque()
        queue.append(start)
        seen = set([start])
        predecessors = {start: None}  

        while queue:
            point = queue.popleft()

            if point == self.end:
                path = []
                while point is not None:
                    path.append(point)
                    point = predecessors[point]
                return path[::-1]  

            for (i, j) in self.directions.values():
                new_point = Point(point.x + i, point.y + j)
                if self.is_point_inbounds(maze, new_point) and maze[new_point.x][new_point.y] != "#" and new_point not in seen:
                    queue.append(new_point)
                    seen.add(new_point)
                    predecessors[new_point] = point 

        return None  

    def solve(self):
        
        # self.read_from_file("input_small.txt")
        # ROWS = 7
        # COLUMNS = 7
        # bytes_num = 12

        self.read_from_file()
        ROWS = 71
        COLUMNS = 71
        bytes_num  = 1024

        self.start = Point(0,0)
        self.end = Point(ROWS-1,COLUMNS-1)

        # print(f"{self.input_data=}")       

        start_num = 1024
        for i, byte in enumerate(self.input_data[start_num:], start=start_num):
            print(i, byte)
            self.maze = self.make_maze(ROWS, COLUMNS, i+1)
            
            # draw grid after bytes_num bytes
            # self.draw_grid(self.maze)
            
            path = self.bfs(self.maze, self.start)
            if not path:
                break
            # print(path)

        print(f"byte that stopped {byte.y},{byte.x}")
        # print(f"Need steps {len(path)-1}")

if __name__ == "__main__":
    App().solve()

