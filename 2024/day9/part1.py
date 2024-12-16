from collections import deque

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

    def solve(self):
        self.read_from_file()

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
        
        # Identify initial positions of non-`.` characters
        not_free_space_indices = deque(i for i, value in enumerate(result_string) if value != ".")
        
        # Iterate to move file blocks to the front
        index = 0
        while len(not_free_space_indices) > 0 and not self.gaps_exist(result_string, not_free_space_indices[-1]):
            print(f"{index/len(result_string)=} %", end = "\r")
            char = result_string[index]
            if char == ".":
                # Swap with the last non-`.` character
                last_file_block_index = not_free_space_indices.pop()
                result_string[index], result_string[last_file_block_index] = result_string[last_file_block_index], "."
            index += 1

        # Calculate the total
        result_string = list(result_string)[:result_string.index(".")]
        total = sum(i * int(value) for i, value in enumerate(result_string))

        print(f"Total is {total}")


if __name__ == "__main__":
    App().solve()
