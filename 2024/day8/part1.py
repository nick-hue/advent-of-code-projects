from itertools import product, combinations

class App():
    def __init__(self):
        self.input_data = []
        
    def read_from_file(self, filename="input.txt"):
        with open(filename, "r") as f:
            data = [line.strip() for line in f.readlines()]
        self.input_data = [list(chars) for chars in data]

    def is_node_inbounds(self, x, y):
        return 0 <= x < len(self.input_data[0]) and 0 <= y < len(self.input_data)

    def solve(self):
        # self.read_from_file("input_small.txt")
        self.read_from_file()
        # print(f"{self.input_data=}")       

        distinct = set([num for line in self.input_data for num in line if num != "."])
        print(f"{distinct=}")

        locations_dic = {}

        print("     "+" ".join([str(num) for num in list(range(len(self.input_data[0])))]))
        for i, line in enumerate(self.input_data):
            print(f"{i:<4}", end=" ")
            for j, char in enumerate(line):
                print(f"{char}", end=" ")
                if char in distinct:
                    try:
                        if locations_dic[char]:
                            locations_dic[char].append((i,j))
                    except KeyError:
                        locations_dic[char] = []
                        locations_dic[char].append((i,j))
            print()

        print(f"{locations_dic=}")

        antinode_locations = []
        total = 0
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
                else:
                    antinode_y_1 = first[1] + abs(col_dist)
                    antinode_y_2 = second[1] - abs(col_dist)

                if self.is_node_inbounds(antinode_x_1, antinode_y_1):
                    print(f"Putting at : {antinode_x_1},{antinode_y_1}")
                    # if self.input_data[antinode_x_1][antinode_y_1] not in distinct:
                    self.input_data[antinode_x_1][antinode_y_1] = "#"
                    antinode_locations.append((antinode_x_1, antinode_y_1))
                    # total += 1 
                # else:
                #     print(f"{antinode_x_1}-{antinode_y_1} not in bounds")
                if self.is_node_inbounds(antinode_x_2, antinode_y_2):
                    print(f"Putting at : {antinode_x_2},{antinode_y_2}")
                    # if self.input_data[antinode_x_2][antinode_y_2] not in distinct:
                    self.input_data[antinode_x_2][antinode_y_2] = "#"
                    antinode_locations.append((antinode_x_2, antinode_y_2))
                    # total += 1
                # else:
                #     print(f"{antinode_x_2}-{antinode_y_2} not in bounds")
        print(f"{antinode_locations=}")
        print(f"{len(set(antinode_locations))=}")


                #  check antinode location is inbounds 
                # chec knot overlapping
        print("After")
        print("     "+" ".join([str(num) for num in list(range(len(self.input_data[0])))]))
        for i, line in enumerate(self.input_data):
                print(f"{i:<4}", end=" ")
                for j, char in enumerate(line):
                    print(f"{char}", end=" ")
                print()
        print(f"{total=}")

if __name__ == "__main__":
    App().solve()
