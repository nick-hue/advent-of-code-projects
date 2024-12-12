from itertools import product

class App():
    def __init__(self):
        self.input_data = []
        self.symbols = "+*"

    def read_from_file(self, filename="input.txt"):
        with open(filename, "r") as f:
            data = [line.strip() for line in f.readlines()]
        self.input_data = data

    def is_equation_true(self, result, numbers):
        combinations_amount = len(numbers)-1
        possible_combinations = list(product(self.symbols, repeat=combinations_amount))

        # print(f"For {len(numbers)} numbers there are : {possible_combinations}")

        for comb in possible_combinations:
            check_result = int(numbers[0])
            
            for num, op in zip(numbers[1:], comb):
                # print(f"{op=}")
                if op == "*":
                    check_result *= int(num)
                elif op == "+":
                    check_result += int(num)
                else:
                    print("problem")
                    break


            if check_result == result:
                # print(f"Found {comb=} {numbers=} -> {check_result} {result}")
                return True 
            
        return False


    def solve(self):
        # self.read_from_file("input_small.txt")
        self.read_from_file()
        print(f"{self.input_data=}")       

        total = 0
        for line in self.input_data:
            # print(f"{line}")
            result, amounts = line.split(": ")
            numbers = amounts.split(" ")
            result = int(result)

            if self.is_equation_true(result, numbers):

                total += int(result)  


        print(f"{total=}")


if __name__ == "__main__":
    App().solve()
