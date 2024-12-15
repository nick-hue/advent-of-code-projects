from collections import Counter

class App():
    def __init__(self):
        self.input_data = []

    def read_from_file(self, filename="input.txt"):
        with open(filename, "r") as f:
            data = [line.strip() for line in f.readlines()]
        self.input_data = list(int(char) for char in data[0])

    def gaps_exist(self, string) -> bool:
        '''
        functions that returns true if the string supplied has no
        empty free space between file blocks
        else returns false
        '''

        string_index = string.index('.')
        # split_string = list(string[string_index:])

        # Gets counter from the substring created by the first instance of a "."
        # then checks if this counter has one or more elements 
        # if it has it means that there are file blocks ahead -> false
        if any([True for char in string[string_index:] if char != '.']):
            return False
        
        counter = Counter(split_string)
        
        if len(counter.keys()) > 1:
            return False
        
        return True

    def get_last_file_block_indeces(self, result_string):
        '''
        returns the index of the first available file blocks starting from the end
        '''
        # for i in range(len(result_string)-1, current_index, -1):
        #     if result_string[i] != ".":
        #         return i


        
        return None
        


    def solve(self):
        # self.read_from_file("input_small.txt")
        self.read_from_file()
        # print(f"{self.input_data=}")     

        result_string = ''
        is_file = True
        id_counter = 0 
        for id, char in enumerate(self.input_data):
            if is_file:
                result_string += "".join([str(id_counter)]*char) 
                id_counter += 1
            else:
                result_string += "."*char
            is_file = not is_file

        # print(f"{result_string=}")
        result_string = list(result_string)
        # print("00...111...2...333.44.5555.6666.777.888899")

        index = 0 
        not_free_space_indeces = [index for index, value in enumerate(result_string) if value != '.']
        # print(f"{not_free_space_indeces}")
        # print(result_string)

        while len(not_free_space_indeces) > 0 and not self.gaps_exist(result_string):
            # print(f"{len(not_free_space_indeces)=}")
            print(f"{(index/len(result_string))*100}%", end = "\r")
            char = result_string[index]
            # print(f"{char=}")
            if char != ".":
                index += 1
                continue

            last_file_block_index = not_free_space_indeces[-1]
            del not_free_space_indeces[-1]
            
            result_string[index], result_string[last_file_block_index] = result_string[last_file_block_index], result_string[index]
            index += 1
            # print(f"{"".join(result_string)=}")


        result_string = result_string[:result_string.index(".")]
        total = 0
        for i, value in enumerate(result_string):
            total += i * int(value)

        print(f"Total is {total}")






if __name__ == "__main__":
    App().solve()

