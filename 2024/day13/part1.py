from dataclasses import dataclass
from typing import Tuple

@dataclass
class Field:
    x: int
    y: int
    cost: int

@dataclass
class Behavior:
    a: Field
    b: Field
    prize: Field


class App():
    def __init__(self):
        self.input_data = []

    def read_from_file(self, filename="input.txt"):
        with open(filename, "r") as f:
            data = [line.strip() for line in f.readlines()]

        self.input_data = data

    def get_stats(self, input_string, type, button_type = None) -> Tuple[int,int]:
        
        # print(input_string)
        x, y = input_string.split(": ")[1].split(", ")
        if type == "button":
            x, y = int(x.replace("X+", "")), int(y.replace("Y+", ""))
        elif type == "prize":
            x, y = int(x.replace("X=", "")), int(y.replace("Y=", ""))
        else:
            print("ERRORR")
            x, y = -1, -1

        # print(x, y)
        if button_type == "a":
            cost  = 3
        elif button_type == "b":
            cost = 1
        else:
            cost = None

        return Field(x, y, cost)
    
    def get_behavior_from_line(self, tmp_behavior) -> Behavior:
        a, b, prize = self.get_stats(tmp_behavior[0], "button", "a"), self.get_stats(tmp_behavior[1], "button", "b")\
                                , self.get_stats(tmp_behavior[2], "prize")
                
        return Behavior(a, b, prize)

    def get_behaviors(self):
        behaviors = []
        tmp_behavior = []
        for i, line in enumerate(self.input_data):
            if line == '':
                behaviors.append(self.get_behavior_from_line(tmp_behavior))
                
                tmp_behavior = []
                continue
            tmp_behavior.append(line)
        behaviors.append(self.get_behavior_from_line(tmp_behavior))
        return behaviors 

    def calculate_tokens(self, behavior: Behavior):
    
        cost = 0 
        current_x = 0
        current_y = 0
        a_tries = 0
        while a_tries < 101:
            # print(f"{a_tries=}")
            current_x = a_tries * behavior.a.x
            current_y = a_tries * behavior.a.y
            cost = a_tries * behavior.a.cost


            # checking b button for minimal tries
            tries = 0
            while current_x <= behavior.prize.x and tries <= 100:
                # print(f"{current_x=}-{current_y=}-{cost=}")
                if current_x == behavior.prize.x and current_y == behavior.prize.y:
                    return cost

                current_x += behavior.b.x
                current_y += behavior.b.y
                cost += behavior.b.cost
                tries += 1



            a_tries += 1
            current_x = 0 
            current_y = 0 
            cost = 0


        return



    def solve(self):
        # self.read_from_file("input_small.txt")
        self.read_from_file()
        # print(f"{self.input_data=}")       

        # 3 tokens to push the A button and 1 token to push the B button.

        behaviors = self.get_behaviors()
        
        costs = []
        for be in behaviors:
            print(f"{be}")
            costs.append(self.calculate_tokens(be))

        costs = [cost for cost in costs if cost]
        print(f"Total = {sum(costs)}")

if __name__ == "__main__":
    App().solve()

