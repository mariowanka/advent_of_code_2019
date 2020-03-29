#!/usr/bin/python3

from operator import add, mul

INFILE = "in"


class Processor():
    def __init__(self):
        self.instr_step = 4
        self.instr_set = {
            1: add,
            2: mul,
            99: None
        }
        self.pointer = 0
        self.instr = self._load_instructions(INFILE)

    def _load_instructions(self, path):
        "Return list of isntructions."
        with open(path) as file_in:
            instr = list(map(int, file_in.read().split(',')))
        return instr

    def set_init_code(self, noun, verb):
        """Set 100*noun+verb as initial instruction
        replace pos 1 with noun and pos 2 with verb.
        """
        self.instr[1] = int(noun)
        self.instr[2] = int(verb)

    def get_zero_instruction(self):
        return self.instr[0]

    def run(self):
        while(True):
            if self.instr[self.pointer] not in self.instr_set:
                exit('Out of magic smoke! Unknown instr {} on pos {}.'.format(self.instr[self. pointer], self.pointer))

            if self.pointer + 3 > len(self.instr) and self.instr_set[self.instr[self.pointer]] is not None:
                exit('Out of magic smoke! Index {} out of range {}.'.format(self.pointer, len(self.instr)))

            if self.instr_set[self.instr[self.pointer]] is None:
                break

            self.instr[self.instr[self.pointer + 3]] = self.instr_set[self.instr[self.pointer]](
                self.instr[self.instr[self.pointer + 1]],
                self.instr[self.instr[self.pointer + 2]]
            )

            self.pointer += self.instr_step


if __name__ == '__main__':
    p = Processor()
    p.set_init_code(12, 2)
    p.run()
    print(p.get_zero_instruction())
