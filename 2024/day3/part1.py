import re

class App():
    def read_from_file(self, filename="input.txt"):
        with open(filename, "r") as f:
            data = [line.strip() for line in f.readlines()]
        return data


    def solve(self):
        input_data = self.read_from_file()
        print(f"{input_data=}")       

        total = 0
        for line in input_data:
            x = re.findall(r"mul\(\d+,\d+\)", line)
            for compute in x:
                print(f"{compute=}")
                first, second = compute.split(",")
                total += int(first.replace("mul(", "")) * int(second.replace(")", ""))

        print(f"{total=}")




if __name__ == "__main__":
    App().solve()
