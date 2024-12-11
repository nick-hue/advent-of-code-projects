from itertools import permutations

class App():
    def __init__(self):
        self.input_data = []
        self.symbols = ["+", "*"]

    def read_from_file(self, filename="input.txt"):
        with open(filename, "r") as f:
            data = [line.strip() for line in f.readlines()]
        self.input_data = data

    def is_equation_true(self, numbers):
        
        combinations_amount = len(numbers)-1
        print(combinations_amount)

        print(list(permutations(self.symbols, combinations_amount)))


    def solve(self):
        self.read_from_file("input_small.txt")
        #self.read_from_file()
        print(f"{self.input_data=}")       

        total = 0
        for line in self.input_data:
            print(f"{line}")
            result, amounts = line.split(": ")
            numbers = amounts.split(" ")

            print(f"{result=}")
            print(f"{numbers=}")


            if self.is_equation_true(numbers):
                total += result  


        print(f"{total=}")


if __name__ == "__main__":
    App().solve()
