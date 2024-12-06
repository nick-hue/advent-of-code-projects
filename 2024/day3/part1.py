class App():
    def read_from_file(self, filename="input.txt"):
        with open(filename, "r") as f:
            data = [line.strip() for line in f.readlines()]
        return data


    def solve(self):
        input_data = self.read_from_file()
        print(f"{input_data=}")       


if __name__ == "__main__":
    App().solve()
