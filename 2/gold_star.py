#!/usr/bin/python3

from silver_star import INFILE
from silver_star import Processor

HIT = 19690720


class GoldProcessor(Processor):
    def __init__(self):
        super().__init__()
        self.initial_instr = self.instr.copy()

    def reset_instructions(self):
        self.instr = self.initial_instr.copy()
        self.pointer = 0


if __name__ == '__main__':
    p = GoldProcessor()
    for verb in range(100):
        for noun in range(100):
            p.reset_instructions()
            p.set_init_code(noun, verb)
            p.run()
            if p.get_zero_instruction() == HIT:
                print(100*noun+verb)
                exit()
