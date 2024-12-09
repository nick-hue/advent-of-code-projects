class App():
    def __init__(self):
        self.input_data = []
        
    def read_from_file(self, filename="input.txt"):
        with open(filename, "r") as f:
            data = [line.strip() for line in f.readlines()]
        self.input_data = data

    def solve(self):
        self.read_from_file("input_small.txt")
        #self.read_from_file()
        print(f"{self.input_data=}")       

if __name__ == "__main__":
    App().solve()
