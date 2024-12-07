class App():
    def __init__(self):
        self.result_matrix = []
        self.input_data = []


    def read_from_file(self, filename="input.txt"):
        with open(filename, "r") as f:
            data = [line.strip() for line in f.readlines()]
        self.input_data = data

    def check_horizontal(self, input_data, x, y):
        if input_data:
            ...



    def solve(self):
        self.read_from_file("input_small.txt")
        #self.read_from_file()
        print(f"{self.input_data=}")    
        
        result_matrix = [False for line in self.input_data for character in line]

        print(result_matrix)

        for i, line in enumerate(self.input_data):
            for j, character in enumerate(line):
                ...
                



if __name__ == "__main__":
    App().solve()

