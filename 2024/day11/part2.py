from copy import deepcopy

class App():
    def __init__(self):
        self.input_data = []
        
    def read_from_file(self, filename="input.txt"):
        with open(filename, "r") as f:
            data = [line.strip() for line in f.readlines()]
        self.input_data = [int(str_number) for str_number in data[0].split(" ")]

    def process_number(self, num):
        if num == 0:
            return 1
         
        string_num = str(num)
        if len(string_num) % 2 == 0: # if even number of digits
            split_index = len(string_num)//2
            return [int(string_num[:split_index]), int(string_num[split_index:])]

        return [2024*num]

    def solve(self):
        # self.read_from_file("input_small.txt")
        self.read_from_file()

        shift_matrix = deepcopy(self.input_data)
        print(shift_matrix)
        blink_times = 75
        blink = 0 
        mapper = {}

        while blink < blink_times:
            print(f"{blink=}")
            print(f"{shift_matrix=}")
            tmp_matrix = []
            
            for num_index, num in enumerate(shift_matrix):
                if num not in mapper:
                    mapper.update({num:(1,[blink])})
                    tmp_matrix.extend(self.process_number(num))
                else:
                    mapper.update(num=(mapper[num][0]+1,mapper[num][1].append(blink)))
                    tmp_matrix.extend(self.process_number(num))

            shift_matrix = tmp_matrix
            blink += 1

        print(f"{mapper}")

        print(f"i will have {len(shift_matrix)} stones")            




if __name__ == "__main__":
    App().solve()
