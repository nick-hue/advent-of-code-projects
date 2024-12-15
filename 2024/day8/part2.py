from itertools import combinations

class App():
    def __init__(self):
        self.input_data = []
        self.antinode_locations = []
        self.total=0

    def read_from_file(self, filename="input.txt"):
        with open(filename, "r") as f:
            data = [line.strip() for line in f.readlines()]
        self.input_data = [list(chars) for chars in data]

    def is_node_inbounds(self, x, y):
        return 0 <= x < len(self.input_data[0]) and 0 <= y < len(self.input_data)

    def put_antinodes(self, anti_x, anti_y, node_x, node_y):
        print(f"Putting anti nodes for {anti_x=}-{anti_y=}")
        value_x, value_y = anti_x, anti_y
        while True:
            print(f"{value_x}-{value_y}")
            if not self.is_node_inbounds(value_x, value_y):
                print("breaking")
                break

            if self.input_data[value_x][value_y] not in self.distinct:
                self.input_data[value_x][value_y] = "#"
            self.antinode_locations.append((value_x, value_y))
            
            self.result_matrix[value_x][value_y] = True
            self.total+=1

            value_x += node_x
            value_y += node_y

            
            


    def solve(self):
        # self.read_from_file("input_small.txt")
        self.read_from_file()
        # print(f"{self.input_data=}")       

        self.result_matrix = [[False for _ in line] for line in self.input_data]
        print(self.result_matrix) 

        self.distinct = set([num for line in self.input_data for num in line if num != "."])
        print(f"{self.distinct=}")

        locations_dic = {}

        print("     "+" ".join([str(num) for num in list(range(len(self.input_data[0])))]))
        for i, line in enumerate(self.input_data):
            print(f"{i:<4}", end=" ")
            for j, char in enumerate(line):
                print(f"{char}", end=" ")
                if char in self.distinct:
                    try:
                        if locations_dic[char]:
                            locations_dic[char].append((i,j))
                    except KeyError:
                        locations_dic[char] = []
                        locations_dic[char].append((i,j))
            print()

        print(f"{locations_dic=}")

        for key, value in locations_dic.items():
            combos = list(combinations(value, r=2))
            print(f"For {value=} there are : {combos=}")

            for com in combos:
                first, second = com
                # x_dist, y_dist = abs(first[0] - second[0]), abs(first[1] - second[1])
                row_dist, col_dist = first[0] - second[0], first[1] - second[1]
                print(f"{row_dist=}, {col_dist=} for {com}")

                antinode_x_1 = first[0] - abs(row_dist)
                antinode_x_2 = second[0] + abs(row_dist)
                
                if col_dist < 0 :
                    antinode_y_1 = first[1] - abs(col_dist)
                    antinode_y_2 = second[1] + abs(col_dist)
                    
                    self.put_antinodes(antinode_x_1, antinode_y_1, -abs(row_dist), -abs(col_dist))
                    self.put_antinodes(antinode_x_2, antinode_y_2, abs(row_dist), abs(col_dist))
                else:
                    antinode_y_1 = first[1] + abs(col_dist)
                    antinode_y_2 = second[1] - abs(col_dist)

                    self.put_antinodes(antinode_x_1, antinode_y_1, -abs(row_dist), abs(col_dist))
                    self.put_antinodes(antinode_x_2, antinode_y_2, abs(row_dist), -abs(col_dist))
                
        print(f"{self.antinode_locations=}")
        print(f"{len(list(self.antinode_locations))=}")

        print("After")
        print("     "+" ".join([str(num) for num in list(range(len(self.input_data[0])))]))
        for i, line in enumerate(self.input_data):
                # print(f"{i:<4}", end=" ")
                for j, char in enumerate(line):
                    print(f"{char}", end="")
                print()

        from collections import Counter

        print(f"{Counter([value for line in self.result_matrix for value in line])}")

        result_dict = dict(Counter([value for line in self.input_data for value in line]))

        print(result_dict)
        print(self.distinct)
        total = 0 
        for key, value in result_dict.items():
            if key in self.distinct or key == "#":
                total += value

        print(f"Total is {total}")

if __name__ == "__main__":
    App().solve()
