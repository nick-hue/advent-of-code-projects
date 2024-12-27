
class App():
    def __init__(self):
        self.input_data = []
        self.memo = {}

    def read_from_file(self, filename="input.txt"):
        with open(filename, "r") as f:
            data = [line.strip() for line in f.readlines()]
        split_index = data.index('')

        print(data)
        self.available_patterns = [char.strip() for char in data[:split_index][0].split(",")]
        self.designs = data[split_index+1:]
        
    # def check_design(self, des: str) -> int:
    #     result_check = '-'*len(des)
    #     # print(f"{result_check=} - for {des=}") 
    #     check_times = 0
    #     while check_times < len(self.available_patterns):    
            
    #         patterns = self.available_patterns[check_times:] + self.available_patterns[:check_times]
    #         # print(f"Design for check times {check_times} : {patterns=} :\n\t\t {self.available_patterns=}")
    #         tmp_design = des
    #         for pattern in patterns:
    #             # print(f"Checking {pattern=}")
    #             # print(pattern in tmp_design)
    #             if pattern not in tmp_design:
    #                 continue
                
    #             tmp_design = tmp_design.replace(pattern, "-"*len(pattern))
    #             # print(f"{tmp_design=}")
    #             if tmp_design == result_check:
    #                 # print("found possible...")
    #                 return 1
    #         # print()
    #         check_times += 1

    #     return 0
            

    def composable(self, string, words):
        if string == "":
            return True
        try:
            if self.memo[string]:
                return self.memo[string] 
        except KeyError:
            self.memo[string] = False

        for w in words:
            length = len(w)
            start = string[:length]
            rest = string[length+1:]
            if start == w and self.composable(rest, words):
                self.memo[string] = True # Memoize

        return self.memo[string]
    


    def solve(self):
        # self.read_from_file("input_small.txt")
        self.read_from_file()
    
        print(f"{self.available_patterns=}")
        print(f"{self.designs=}")

        total = 0 
        for des in self.designs:
            # total += self.check_design(des)
            if self.composable(des, self.available_patterns):
                total += 1
    
        print(f"Total designs possible : {total}")

if __name__ == "__main__":
    App().solve()

