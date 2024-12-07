import re

class App():
    def read_from_file(self, filename="input.txt"):
        with open(filename, "r") as f:
            data = [line.strip() for line in f.readlines()]
        
        return data


    def solve(self):
        input_data = self.read_from_file("input.txt")
        print(f"{input_data=}")       

        total = 0
        computing = True
        data = "".join(input_data)

        while data != "":
            if computing:
                split_result = re.split(r"don't\(\)", data, 1)
            else:
                split_result = re.split(r"do\(\)", data, 1)

            print(split_result)
            if len(split_result) > 1:
                compute_part, remain_part = split_result
            else:
                compute_part, remain_part = split_result[0], "" 

            if computing:
                matches = re.findall(r"mul\(\d+,\d+\)", compute_part)
                for compute in matches:
                    first, second = compute.split(",")
                    total += int(first.replace("mul(", "")) * int(second.replace(")", ""))
                computing = False
            else:
                computing = True

            data = remain_part

        print(f"Total is : {total}")



if __name__ == "__main__":
    App().solve()
