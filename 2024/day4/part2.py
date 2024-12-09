class App():
    def __init__(self):
        self.input_data = []
        self.result_matrix = []
        self.mas_list = ["MAS", "SAM"]
        
    def read_from_file(self, filename="input.txt"):
        with open(filename, "r") as f:
            data = [line.strip() for line in f.readlines()]
        self.input_data = data

    def draw_result_matrix(self):
        for i, line in enumerate(self.result_matrix):
            print(f"{i} : ", end = " ")
            for j, value in enumerate(line):
                # print(value)
                if value:
                    print_char = self.input_data[i][j]
                else:
                    print_char = "."

                print(f"{print_char}", end = '') 
            print() 

    def check_X_MAS(self, i, j):
        try:
            left_diag = self.input_data[i+1][j-1] + self.input_data[i][j] + self.input_data[i-1][j+1]
            right_diag = self.input_data[i-1][j-1] + self.input_data[i][j] + self.input_data[i+1][j+1]
        except IndexError:
            return 0

        if left_diag in self.mas_list and right_diag in self.mas_list:
            self.result_matrix[i+1][j-1] = True
            self.result_matrix[i-1][j-1] = True
            self.result_matrix[i][j] = True
            self.result_matrix[i-1][j+1] = True
            self.result_matrix[i+1][j+1] = True
            return 1
        
        return 0

    def solve(self):
        # self.read_from_file("input_small.txt")
        self.read_from_file("input.txt")
        print(f"{self.input_data=}")    

        self.result_matrix = [
            [False for _ in range(len(self.input_data[0]))]
            for _ in range(len(self.input_data))
        ]

        total = 0 
        for i, line in enumerate(self.input_data):
            for j, char in enumerate(line):
                if char == "A":
                    # print(char)
                    total += self.check_X_MAS(i, j)
            print()

        self.draw_result_matrix()
        print(f"{total=}")


if __name__ == "__main__":
    App().solve()

