#!/usr/bin/python3

INFILE = 'in'

def sum_fuel():
    return sum([mass_to_fuel(mass) for mass in get_input(INFILE)])

def mass_to_fuel(mass):
    return int(mass / 3) - 2

def get_input(infile):
    with open(infile) as file_in:
        for line in file_in.readlines():
            yield int(line)

if __name__ ==  '__main__':
    print(sum_fuel())
