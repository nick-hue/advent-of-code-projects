import numpy as np
from scipy.ndimage import rotate

class App():
    def __init__(self):
        self.result_matrix = []
        self.input_data = []


    def read_from_file(self, filename="input.txt"):
        with open(filename, "r") as f:
            data = [line.strip() for line in f.readlines()]
        self.input_data = data

    def check_horizontal(self):
        total = 0 
        
        # print(self.input_data)
        for i, line in enumerate(self.input_data):
            for j, char in enumerate(line):
                # print(i,j)
                string = ""
                try:
                    list_of_chars = self.input_data[i][j] + self.input_data[i][j+1] + self.input_data[i][j+2] + self.input_data[i][j+3] 
                except IndexError:
                    break

                string = "".join("".join(list_of_chars))
                # print(string)
                if string == "XMAS" or string == "SAMX":
                    total+=1
                    print(f"Found {i}-{j} : {string}")
                    self.result_matrix[i][j] = True
                    self.result_matrix[i][j+1] = True
                    self.result_matrix[i][j+2] = True
                    self.result_matrix[i][j+3] = True
            
                    
        return total 
    
    def check_vertical(self):
        total = 0 
        print(f"{len(self.input_data[0])=}")
        for i in range(len(self.input_data)):
            string = ""
            for j in range(len(self.input_data[0])):

                try:
                    list_of_chars = self.input_data[i][j] + self.input_data[i+1][j] + self.input_data[i+2][j] + self.input_data[i+3][j] 
                except IndexError:
                    break
                    
                string = "".join(list_of_chars)
                if string == "XMAS" or string == "SAMX":
                    total+=1
                    print(f"Found {i}-{j} : {string}")
                    self.result_matrix[i][j] = True
                    self.result_matrix[i+1][j] = True
                    self.result_matrix[i+2][j] = True
                    self.result_matrix[i+3][j] = True

        return total
    
    def check_diagonally(self):
        total = 0 

        for i in range(len(self.input_data)):
            for j in range(len(self.input_data[0])):
                
                try:
                    left_diag_char = self.input_data[i][j] + self.input_data[i-1][j-1] + self.input_data[i-2][j-2] + self.input_data[i-3][j-3] 
                    right_diag_char = self.input_data[i][j] + self.input_data[i+1][j+1] + self.input_data[i+2][j+2] + self.input_data[i+3][j+3] 
                    
                except IndexError:
                    break 

                string_left = "".join(left_diag_char)
                string_right = "".join(right_diag_char)
                
                if string_left == "XMAS" or string_left == "SAMX":
                    total+=1
                    print(f"Found {i}-{j} : {string_left}")
                    self.result_matrix[i][j] = True
                    self.result_matrix[i-1][j-1] = True
                    self.result_matrix[i-2][j-2] = True
                    self.result_matrix[i-3][j-3] = True

                if string_right == "XMAS" or string_right == "SAMX":
                    total+=1
                    print(f"Found {i}-{j} : {string_right}")
                    self.result_matrix[i][j] = True
                    self.result_matrix[i+1][j+1] = True
                    self.result_matrix[i+2][j+2] = True
                    self.result_matrix[i+3][j+3] = True
                    

        return total
                
    def draw_result_matrix(self):
        for i, line in enumerate(self.result_matrix):
            for j, value in enumerate(line):
                # print(value)
                if value:
                    print_char = self.input_data[i][j]
                else:
                    print_char = "."

                print(print_char, end = '') 
            print()   

    def solve(self):
        self.read_from_file("input_small.txt")
        #self.read_from_file()


        self.result_matrix = [
            [False for _ in range(len(self.input_data[0]))]
            for _ in range(len(self.input_data))
        ]
        # self.input_data = [list(line) for line in self.input_data]
        # self.input_data = np.array(self.input_data, dtype=str)

        result_total = 0
    
        print("Checking horizontally")
        result_total += self.check_horizontal()
        print("Checking vertically")
        result_total += self.check_vertical()
        print("Checking diagonally")
        result_total += self.check_diagonally()

        print(f"{result_total=}")
        # print(self.result_matrix)
        self.draw_result_matrix()


if __name__ == "__main__":
    App().solve()

