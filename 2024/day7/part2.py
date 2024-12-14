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
        if "|" not in list(comb):
            return numbers, comb
               
        # indeces where the | operator is shown
        ii = self.find(comb, "|")
        print(ii)
        
        # new_numbers = []
        new_numbers = list(deepcopy(numbers))
        new_comb = list(deepcopy(comb))
        # new_comb = [] 

        desired_length = len(numbers) - len(ii)
        print(f"{desired_length=}")
        print("Starting while...")
        
        current_length = 0 
        index = 0 

        while current_length != desired_length:
            print(f"{new_numbers=} - {new_comb=}")
            print(f"{index=}")
            if index in ii:
                new_numbers[index] = str(new_numbers[index]) + str(new_numbers[index+1])
                del new_numbers[index+1]
                del new_comb[index]
                current_length+=1
                continue
            current_length+=1
            index+=1

        return new_numbers, new_comb


    def is_equation_true(self, result, nums):
        combinations_amount = len(nums)-1
        possible_combinations = list(product(self.symbols, repeat=combinations_amount))

        print(f"For {len(nums)} numbers there are : {possible_combinations}")

        for i, com in enumerate(possible_combinations):
            print(f"Before processing: {nums=}, {com=}")
            new_numbers, new_comb = self.remake_numbers_and_combs(nums, com)
            print(f"After processing: {new_numbers=}, {new_comb=}")
            
            check_result = int(new_numbers[0])            
            for i, (num, op) in enumerate(zip(new_numbers[1:], new_comb)):
                # print(f"{op=}")
                if op == "*":
                    check_result *= int(num)
                elif op == "+":
                    check_result += int(num)
                elif len(new_comb) == 1 and op == "|":
                    check_result = int(new_numbers[i]+new_numbers[i+1])
                else:
                    print("problem")
                    break
            print()


            if check_result == result:
                # print(f"Found {comb=} {numbers=} -> {check_result} {result}")
                return True 
            
        return False


    def solve(self):
        self.read_from_file("input_small.txt")
        # self.read_from_file()
        print(f"{self.input_data=}")       

        total = 0
        for line in self.input_data:
        # for line in self.input_data:
            # print(f"{line}")
            result, amounts = line.split(": ")
            numbers = amounts.split(" ")
            result = int(result)

            if self.is_equation_true(result, numbers):
                total += int(result)  


        print(f"{total=}")


if __name__ == "__main__":
    App().solve()
