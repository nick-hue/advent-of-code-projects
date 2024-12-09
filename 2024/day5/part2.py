class App():
    def __init__(self):
        self.rules = []
        self.updates = []
        
    def read_from_file(self, filename="input.txt"):
        with open(filename, "r") as f:
            file_data = [line.strip() for line in f.readlines()]

        split_index = file_data.index("")
        self.rules = file_data[:split_index]
        self.updates = file_data[split_index+1:]

    def make_rule_dict(self):
        rules_dic = {}

        for rule in self.rules:
            left, right = [int(num) for num in rule.split("|")]
            
            # if a list of befores exists for current page number just append the after page number,
            # else make a new list and append the first page number

            try:
                if rules_dic[left]:
                    rules_dic[left].append(right)
            except KeyError:
                rules_dic[left] = []
                rules_dic[left].append(right)

        return rules_dic
    
    def get_incorrect_updates(self, rules_dict):
        incorrect_updates = []
        for update in self.updates:
            # print(update)
            correctly_ordered = True
            page_numbers = [int(num) for num in update.split(",")]
            # print(f"{page_numbers=}")
            for i, page_number in enumerate(page_numbers):
                check_list = page_numbers[i+1:]
                # print(f"{check_list=} for number {page_number}")
                
                # if last element of update
                if len(check_list) == 0:
                    break

                for num in check_list:
                    try:
                        if page_number in rules_dict[num]:
                            correctly_ordered = False
                    except KeyError:
                        continue

            # print(f"Update {update} is {"not " if not correctly_ordered else ""}correctly ordered")
            if not correctly_ordered:
                incorrect_updates.append(page_numbers)
            
        return incorrect_updates
    
    def check_update(self, update, rules_dict):

        for i, page_number in enumerate(update):
                check_list = update[i+1:]
                # print(f"{check_list=} for number {page_number}")
                
                # if last element of update
                if len(check_list) == 0:
                    break

                for j, num in enumerate(check_list):
                    try:
                        if page_number in rules_dict[num]:
                            # print(f"returning {i},{update.index(num)}")
                            # print(f"{num=}")
                            return i, update.index(num)
                    except KeyError:
                        continue
                
        return -1, -1

    def solve(self):
        # self.read_from_file("input_small.txt")
        self.read_from_file()
        # print(f"{self.input_data=}")       

        print(f"{self.rules=}")
        print(f"{self.updates=}")

        rules_dict = self.make_rule_dict()

        print(f"{rules_dict=}")

        incorrect_updates = self.get_incorrect_updates(rules_dict)
        total = 0
        for update in incorrect_updates:
            print(f"{update}")
            
            # check update function returns the indeces of the current checking number and the one that 
            # is breaking the rule, it swaps them and check again till the update is correctly sorted (indeces == -1)
            # then it increments the total by the middle page number of the update
            ind1=ind2=0
            while True:
                print(f"{ind1=} - {ind2}")
                ind1, ind2 = self.check_update(update, rules_dict)
                if ind1 == -1 and ind2 == -1:
                    break
                update[ind1], update[ind2] = update[ind2], update[ind1]
            print(update)
            total += update[len(update)//2]


        print(f"{total=}")


if __name__ == "__main__":
    App().solve()
