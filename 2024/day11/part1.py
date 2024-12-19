from copy import deepcopy

class App():
    def __init__(self):
        self.input_data = []
        
    def read_from_file(self, filename="input.txt"):
        with open(filename, "r") as f:
            data = [line.strip() for line in f.readlines()]
        self.input_data = [int(str_number) for str_number in data[0].split(" ")]

    def change_binary(self, num) -> int:
        return 0 if num == 1 else 1

    def solve(self):
        # self.read_from_file("input_small.txt")
        self.read_from_file()

        shift_matrix = deepcopy(self.input_data)
        blink_times = 25
        blink = 0 
        while blink < blink_times:
            print(f"{blink=}")
            # print(f"{shift_matrix=}")
            tmp_matrix = []
            for num_index, num in enumerate(shift_matrix):
                # if num = 0 or num = 1 swap 
                if num == 0:
                    tmp_matrix.append(1)
                elif len(str(num)) % 2 == 0: # if even number of digits
                    split_index = len(str(num))//2
                    str_left, str_right = str(num)[:split_index], str(num)[split_index:]
                    tmp_matrix.extend([int(str_left), int(str_right)])
                else:
                    tmp_matrix.append(2024 * num)

            shift_matrix = tmp_matrix

            blink+=1 

        print(f"i will have {len(shift_matrix)} stones")            




if __name__ == "__main__":
    App().solve()
