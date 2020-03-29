#!/usr/bin/python3

from silver_star import INFILE, get_input, mass_to_fuel

def fuel_for_fuel(mass):
    fuel = mass_to_fuel(mass)
    if fuel > 0:
        addition = fuel_for_fuel(fuel)
        if addition > 0:
            fuel += addition
    return fuel

def sum_fuel():
    return sum([fuel_for_fuel(mass) for mass in get_input(INFILE)])

if __name__ ==  '__main__':
    print(sum_fuel())
