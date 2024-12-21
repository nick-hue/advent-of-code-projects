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
            return [1]
         
        string_num = str(num)
        if len(string_num) % 2 == 0: # if even number of digits
            split_index = len(string_num)//2
            return [int(string_num[:split_index]), int(string_num[split_index:])]

        return [2024*num]

    def solve(self):
        self.read_from_file("input_small.txt")
        # self.read_from_file()

        shift_matrix = deepcopy(self.input_data)
        print(shift_matrix)
        blink_times = 6
        blink = 0 
        mapper = {}

        for num_index, num in enumerate(self.input_data):
            
            shift_matrix = [num]
            while blink < blink_times:
                print(f"{blink=}")
                print(f"{shift_matrix=}")
                print(f"{mapper=}")
                tmp_matrix = [] 
            
                for number in shift_matrix:
                    if number not in mapper:
                        mapper.update({number:(1,[blink])})
                    else:
                        mapper[num]=(mapper[number][0]+1,mapper[number][1].append(blink))

                tmp_matrix.extend(self.process_number(number))

                blink += 1
                shift_matrix = tmp_matrix

        print(f"{mapper}")

        print(f"i will have {len(shift_matrix)} stones")            




if __name__ == "__main__":
    App().solve()
