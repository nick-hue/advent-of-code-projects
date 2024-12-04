class App():
    def read_from_file(self, filename="input.txt"):
        with open(filename, "r") as f:
            data = [line.strip() for line in f.readlines()]
        
        return data

    def solve(self):
        input_data = self.read_from_file("input.txt")
        # print(f"{input_data=}")       

        total = 0
        for line in input_data:
            split_up = line.split("mul")
            # print(f"{split_up=}")
            for compute in split_up:
                # print(f"{compute=}")
                num_string = ''
                num1 = 0
                num2 = 0
                possible_mul = False
                for char in compute:
                    if char == '(' and not possible_mul:
                        # print("open par")
                        possible_mul = True
                    elif char == ')' and possible_mul:
                        # print("close par")
                        # print(f"{num_string=}")
                        if num_string:
                            num2 = int(num_string)
                    elif char == ',' and possible_mul:
                        # print(f"{num_string=}")
                        if num_string:
                            num1 = int(num_string)
                        num_string = ''
                    elif char.isdigit() and possible_mul:
                        # print("put digit")
                        num_string += char
                    else:
                        possible_mul = False
                        num1 = num2 = 0
                        num_string = ''
                    print(char, end = '')
                if num1 != 0 and num2 != 0:
                    print(f"\n{num1=}, {num2=}")
                total += num1 * num2

        print(f"{total=}")
                    
            


if __name__ == "__main__":
    App().solve()

