class App():
    def read_from_file(self, filename="input.txt"):
        with open(filename, "r") as f:
            data = [line.strip() for line in f.readlines()]
        
        return data

    def is_order_good(self, nums):
        asc_nums = sorted(nums)
        desc_nums = sorted(nums, reverse=True)

        # print(f"{nums=}, {asc_nums=}, {desc_nums=}")
        return asc_nums == nums or desc_nums == nums
        
    def is_diff_good(self, num1, num2):
        return 1 <= abs(num1-num2) <= 3
    
    def check_order(self, numbers):
        return_list = []
        print(f"{numbers=}")
        for index in range(len(numbers)):
            tmp_nums = numbers.copy()
            tmp_nums.pop(index)
            for num in tmp_nums:
                if self.is_order_good(tmp_nums):
                    return_list.append(tmp_nums)
                    break
        
        print(f"{return_list=}")

        return return_list

    def check_diffs(self, numbers:list):
        # 8 6 4 4 1

        print(f"{numbers=}")
        for i, num in enumerate(numbers):
            tmp_nums = numbers.copy()
            if i == len(tmp_nums)-1: break
            if not self.is_diff_good(num, tmp_nums[i+1]):
                tmp_nums.pop(i)
                for j, number in enumerate(tmp_nums):
                    if j == len(tmp_nums)-1: break
                    if not self.is_diff_good(number, tmp_nums[j+1]):
                        return False
            return True

        return True
        


    def solve(self):
        input_data = self.read_from_file("input.txt")
        print(f"{input_data=}")       

        total = 0
        for report in input_data:
            
            numbers = [int(num) for num in report.split(" ")]

            # check if order is only increasing or only decreasing, 
            # if not check if one element is removed the order of the result list will only increase or decrease
            # if ordered continue to diff check
            level_safe = False
            
            if not self.is_order_good(numbers):
                other_orders = self.check_order(numbers)

                if len(other_orders) < 1:
                    continue

                for order in other_orders:
                    for i, num in enumerate(order):
                        print(f"Num : {num=}")
                        if i == len(order)-1:
                            level_safe = True
                            continue
                        if not self.is_diff_good(num, order[i+1]):
                            level_safe = False
                            break
                        level_safe = True
                    print()

            else:
                # case where order is good, check diff
                if self.check_diffs(numbers):
                    level_safe = True


            if level_safe:
                print("Safe")
                total +=1 
            else:
                print("not safe")
                print(numbers)

        print(f"{total=}")


if __name__ == "__main__":
    App().solve()

