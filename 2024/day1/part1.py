

class App():
    def read_from_file(self, filename="input.txt"):
        with open(filename, "r") as f:
            data = [line.strip() for line in f.readlines()]
        
        return data


    def solve(self):
        input_data = self.read_from_file()
        print(f"{input_data=}")       

        left_list:list[int] = [] 
        right_list:list[int] = [] 

        for line in input_data:
            left, right = int(line.split(" ")[0]), int(line.split(" ")[-1])
            print(left, right)

            left_list.append(left)
            right_list.append(right)

        left_list.sort()
        right_list.sort()

        total_distance = 0 
        for left, right in zip(left_list, right_list):
            total_distance += abs(left-right)

        print(f"{left_list=}")
        print(f"{right_list=}")

        print(f"{total_distance=}")
    

if __name__ == "__main__":
    App().solve()