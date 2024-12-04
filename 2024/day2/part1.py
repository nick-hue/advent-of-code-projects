class App():
    def read_from_file(self, filename="input.txt"):
        with open(filename, "r") as f:
            data = [line.strip() for line in f.readlines()]
        return data


    def solve(self):
        input_data = self.read_from_file()
        print(f"{input_data=}")       

        total = 0
        for report in input_data:
            
            numbers = [int(num) for num in report.split(" ")]

            asc_numbers = sorted(numbers)
            desc_numbers = sorted(numbers, reverse=True)

            print(f"{asc_numbers=} , {desc_numbers=}, {numbers=}")

            if asc_numbers != numbers and desc_numbers != numbers:
                print("Unsafe")    
                continue
            level_surpass = False
            for i, number in enumerate(numbers):
                if i == len(numbers) - 1: continue
                diff = abs(number-numbers[i+1])
                if 1 <= diff <= 3:
                    print(f"{diff=} for {number}, {numbers[i+1]}")
                else:
                    level_surpass = True
                
            if not level_surpass:
                print("Safe")
                total +=1 

        print(f"{total=}")



if __name__ == "__main__":
    App().solve()

