from itertools import product
from copy import deepcopy
import numpy as np

class App():
    def __init__(self):
        self.input_data = []
        self.symbols = "+*|"

    def read_from_file(self, filename="input.txt"):
        with open(filename, "r") as f:
            data = [line.strip() for line in f.readlines()]
        self.input_data = data

    def find(self, s, ch):
        return [i for i, ltr in enumerate(s) if ltr == ch]

    def remake_numbers_and_combs(self, numbers, comb):
        if "|" not in comb:
            return numbers, comb
        
        print(f"Current nums and combs {numbers=} - {comb=}")
        
        # indeces where the | operator is shown
        ii = self.find(comb, "|")
        print(ii)
        
        # new_numbers = []
        new_numbers = list(deepcopy(numbers))
        new_comb = list(deepcopy(comb))

        index = 0
        while "|" in new_comb:
            print(f"{new_numbers=}")
            print(f"{new_comb=}")
            if index in ii:
                new_numbers[index] = str(new_numbers[index]) + str(new_numbers[index+1])
                del new_numbers[index+1]
                del new_comb[index] 
            else:
                index += 1


        print(f"Changed nums and combs {new_numbers=} - {new_comb=}\n")

        return new_numbers, new_comb


    def is_equation_true(self, result, numbers):
        combinations_amount = len(numbers)-1
        possible_combinations = list(product(self.symbols, repeat=combinations_amount))

        print(f"For {len(numbers)} numbers there are : {possible_combinations}")

        for comb in possible_combinations:
            new_numbers, new_comb = self.remake_numbers_and_combs(numbers=numbers, comb=comb)
            
            check_result = int(new_numbers[0])            
            for num, op in zip(new_numbers[1:], new_comb):
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
        self.read_from_file("input_small.txt")
        # self.read_from_file()
        print(f"{self.input_data=}")       

        total = 0
        for line in self.input_data[:3]:
            # print(f"{line}")
            result, amounts = line.split(": ")
            numbers = amounts.split(" ")
            result = int(result)

            if self.is_equation_true(result, numbers):
                total += int(result)  


        print(f"{total=}")


if __name__ == "__main__":
    App().solve()
