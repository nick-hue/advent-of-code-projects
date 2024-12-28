from dataclasses import dataclass
import random

@dataclass
class Point:
    x: int
    y: int

class App():
    def __init__(self):
        self.input_data = []
        self.actions = {
            "up" : (-1,0),
            "down" : (1,0),
            "left" : (0,-1),
            "right" : (0,1),
            "activate" : (None,None),
        }

    def read_from_file(self, filename="input.txt"):
        with open(filename, "r") as f:
            data = [line.strip() for line in f.readlines()]
        self.input_data = data
        
        self.calc = [["7","8","9"],["4","5","6"],["1","2","3"],[" ","0","A"]]
        self.robot_keypad = [[" ", "^", "A"],["<", "v", ">"]]
        
    def index_2d(self, myList, character):
        for i, line in enumerate(myList):
            if character in line:
                return (i, line.index(character))        
        return (None, None)

    def get_vertical_string(self, distance) -> str:
        if distance == 0:
            return ""
        
        if distance < 0:
            return "^"*abs(distance)
        else:
            return "v"*abs(distance)
    
    def get_horizontal_string(self, distance) -> str:
        if distance == 0:
            return ""
        
        if distance < 0:
            return "<"*abs(distance)
        else:
            return ">"*abs(distance)


    def code_to_string(self, pad, code) -> str:
        '''
        returns a string that contains the motions need to be executed by the robot 
        to input the code
        '''
        final_strings = []
        # for i in range(10000):
                
        final_string = ""   
        current_i, current_j = self.index_2d(pad, "A")
        for character in code:
            dest_i, dest_j = self.index_2d(pad, character=character)
            # print(f"I am at {current_i},{current_j} go to -> {dest_i},{dest_j}")
            # print(f"{pad[current_i][current_j]} -> {character}")
            distance_i = dest_i - current_i
            distance_j = dest_j - current_j
            # print(f"Move {distance_i} vertically, {distance_j} horizontally")

            horizontal_string = self.get_horizontal_string(distance_j)
            vertical_string = self.get_vertical_string(distance_i)
            
            # print(f"{vertical_string}")
            # print(f"{horizontal_string}")
            
            # if random.uniform(0,1) < 0.5:
            #     code_string = horizontal_string+vertical_string+"A"
            # else:
            #     code_string = vertical_string+horizontal_string+"A"
            
            # if "<" in horizontal_string:
            #     code_string = horizontal_string+vertical_string+"A"    
            # else:
            #     code_string = vertical_string+horizontal_string+"A"
            
            code_string = vertical_string+horizontal_string+"A"

            final_string += code_string
            
            current_i = dest_i
            current_j = dest_j

        # final_strings.append(final_string)

        # print(final_strings)

        return final_string
        # return min(final_strings, key=len)
        
    def solve(self):
        self.read_from_file("input_small.txt")
        # self.read_from_file()

        for line in self.calc:
            print(" ".join(line))
        print()
        for line in self.robot_keypad:
            print(" ".join(line))

        total = 0 
        for code in self.input_data:
            # print(f"{code=}")
            keypad_string = self.code_to_string(self.calc, code)
            # print(f"{code} : {keypad_string}")
            keypad_radiation_string = self.code_to_string(self.robot_keypad, keypad_string)
            # print(f"{keypad_string} : {keypad_radiation_string}")
            cold_string = self.code_to_string(self.robot_keypad, keypad_radiation_string)
            # print(f"{keypad_radiation_string} : {cold_string}")
            print(f"{code} : {cold_string} : {len(cold_string)}")
            print(f'{int(code[:-1])} * {len(cold_string)}')
            total += int(code[:-1]) * len(cold_string)

        print(f"total is : {total}")
# 379A: <v<A>>^AvA^A <vA <AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A
# 379A: v<<A^>>AvA^A v<<A ^>>AAv<A<A^>>AA<Av>AA^Av<A^>AA<A>Av<A<A^>>AAA<Av>A^A : 68
if __name__ == "__main__":
    App().solve()

