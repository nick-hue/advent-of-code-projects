from dataclasses import dataclass
from typing import Callable

@dataclass
class Register:
    id_num: int
    name: str
    value: int


@dataclass
class Instruction:
    opcode: int
    name: str
    func: Callable

class App():
    def __init__(self):
        self.input_data = []
        self.registers: list[Register] = []
        self.instructions: list[Instruction] = []
        self.output = []
        self.reg_a = None
        self.reg_b = None
        self.reg_c = None
        
    def read_from_file(self, filename="input.txt"):
        with open(filename, "r") as f:
            data = [line.strip() for line in f.readlines()]
        self.input_data = data

    def init_registers(self):
        self.reg_a = Register(4, "A", int(self.input_data[0].split(" ")[-1]))
        self.reg_b = Register(5, "B", int(self.input_data[1].split(" ")[-1]))
        self.reg_c = Register(6, "C", int(self.input_data[2].split(" ")[-1]))
        self.registers.extend([self.reg_a, self.reg_b, self.reg_c])


    def get_combo_value(self, inp):
        if inp == 4:
            return self.reg_a.value
        elif inp == 5:
            return self.reg_b.value
        elif inp == 6:
            return self.reg_c.value
        else:
            return inp


    def _adv(self):
        print("adv")
        self.reg_a.value = self.reg_a.value // (2 ** self.get_combo_value(self.operand))

    def _bxl(self):
        print("bxl")
        self.reg_b.value = self.reg_b.value ^ self.operand

    def _bst(self):
        print("bst")
        self.reg_b.value = self.get_combo_value(self.operand) % 8

    def _jnz(self):
        print("jnz")    
        if self.reg_a.value == 0: return
        self.instruction_pointer = self.operand
        
    def _bxc(self):
        print("bxc")
        self.reg_b.value = self.reg_b.value ^ self.reg_c.value

    def _out(self):
        self.output.append(str(self.get_combo_value(self.operand) % 8))

    def _bdv(self):
        self.reg_b.value = self.reg_a.value // (2 ** self.get_combo_value(self.operand))

    def _cdv(self):
        self.reg_c.value = self.reg_a.value // (2 ** self.get_combo_value(self.operand))

    def init_instructions(self):
        self.adv_instruction = Instruction(0, "adv", self._adv)
        self.bxl_instruction = Instruction(1, "bxl", self._bxl)
        self.bst_instruction = Instruction(2, "bst", self._bst)
        self.jnz_instruction = Instruction(3, "jnz", self._jnz)
        self.bxc_instruction = Instruction(4, "bxc", self._bxc)
        self.out_instruction = Instruction(5, "out", self._out)
        self.bdv_instruction = Instruction(6, "bdv", self._bdv)
        self.cdv_instruction = Instruction(7, "cdv", self._cdv)

        self.opcode_to_instr = {
            0 : self.adv_instruction,
            1 : self.bxl_instruction,
            2 : self.bst_instruction,
            3 : self.jnz_instruction,
            4 : self.bxc_instruction,
            5 : self.out_instruction,
            6 : self.bdv_instruction,
            7 : self.cdv_instruction
        }
        # self.opcode_to_instr = {
        #     0 : self._adv,
        #     1 : self._bxl,
        #     2 : self._bst,
        #     3 : self._jnz,
        #     4 : self._bxc,
        #     5 : self._out,
        #     6 : self._bdv,
        #     7 : self._cdv
        # }


    def solve(self):
        # self.read_from_file("input_small.txt")
        self.read_from_file()
        print(f"{self.input_data=}")       

        self.init_registers()
        self.init_instructions()
        self.program = [int(num) for num in self.input_data[-1].split(" ")[-1].split(",")]
        self.max_counter = len(self.program)

        print(self.reg_a)
        print(self.reg_b)
        print(self.reg_c)
        print(self.program)

        self.instruction_pointer = 0
        while True:
            if self.instruction_pointer + 1 >= self.max_counter:
                break
            self.opcode = self.program[self.instruction_pointer]
            self.operand = self.program[self.instruction_pointer+1]

            instruction: Instruction = self.opcode_to_instr[self.opcode]
            instruction.func()           
            # func: Callable = self.opcode_to_instr[self.opcode]
            # func()


            if self.opcode == 3 and self.reg_a.value != 0:
                continue
            self.instruction_pointer += 2

        print(self.reg_a)
        print(self.reg_b)
        print(self.reg_c)

        print(",".join(self.output))
        print(self.output)


if __name__ == "__main__":
    App().solve()

