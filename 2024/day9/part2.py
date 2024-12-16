from collections import deque, Counter

class App():
    def __init__(self):
        self.input_data = []

    def read_from_file(self, filename="input.txt"):
        with open(filename, "r") as f:
            data = [line.strip() for line in f.readlines()]
        self.input_data = list(int(char) for char in data[0])

    def gaps_exist(self, result_string, last_block_index) -> bool:
        '''
        Returns True if no empty free spaces exist between file blocks
        '''
        # Convert deque to list for slicing or iterate without slicing
        for i in range(last_block_index + 1):
            if result_string[i] == ".":
                return False  # A gap exists
        return True  # No gaps exist

    def find_gap_ending(self, result_string, index):
        i = index
        while i < len(result_string):
            if result_string[i] != '.': return i
            i += 1

        return None

    def find_fitting_item(self, counter_dict, gap_len):
        while True:
            try: 
                item = counter_dict.popitem()
            except KeyError:
                return None
            if item[1] <= gap_len:
                return item
        

    def solve(self):
        self.read_from_file("input_small.txt")
        # self.read_from_file()

        # Create the initial result string as a list
        result_string = []
        is_file = True
        id_counter = 0

        # Populate the result string based on input data
        for char in self.input_data:
            if is_file:
                result_string.extend([str(id_counter)] * char)
                id_counter += 1
            else:
                result_string.extend(["."] * char)
            is_file = not is_file

        # Convert to deque for faster popping and appending
        result_string = deque(result_string)
        counter_string = dict(Counter(result_string))
        print(counter_string)


        index = 0
        while True:
            char = result_string[index]
            # find gap
            if char == ".":
                end_index = self.find_gap_ending(result_string, index)
                
                # gap -> index to end-index
                gap_length = end_index - index
                print(f"{gap_length=} from {index=} to {end_index=}")
                
                # find item that fits
                item = self.find_fitting_item(counter_string, gap_length)
                if not item:
                    break
                print(f"Found item that fits : {item=}")

                # place items in gap 
                replace_string = f"{str(item[0] * item[1]).ljust(gap_length, '.')}"
                result_string[index:end_index] = list(replace_string)

                index = end_index + 1
            else:
                index += 1

            print("".join(result_string))
            




if __name__ == "__main__":
    App().solve()
