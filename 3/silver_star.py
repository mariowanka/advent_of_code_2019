#!/usr/bin/python3

INFILE = 'in'


class Wires():
    def __init__(self):
        self.wire_a = None
        self.wire_b = None
        self.dir_map = {
            'U': (0, 1),  # possitive vertical
            'D': (0, -1),  # negative vertical
            'L': (-1, 0), # negative horizontal
            'R': (1, 0),  # possitive horizontal
        }

        self._parse_wires(INFILE)

    def _get_m_dist(self, coord):
        'Return Manhatton distance of point from centre of grid.'
        return abs(coord[0]) + abs(coord[1])

    def _parse_wires(self, path):
        'Parse text input into two lists of coords and store them to self.'
        with open(path) as file_in:
            self.wire_a = self._get_wire_map(file_in.readline().split(','))
            self.wire_b = self._get_wire_map(file_in.readline().split(','))

    def _get_wire_map(self, wire):
        'Return list of wire coords.'
        pos = (0, 0)
        wire_map = set()
        for command in wire:
            vector = self._translate_direction(command)
            step_dest = self._add_vector(pos, vector)
            wire_map = wire_map.union(self._get_path(pos, step_dest))
            pos = step_dest
        return wire_map

    def _translate_direction(self, command):
        'Translate Xa into vector.'
        direction = self.dir_map[command[0]]
        # multiply distance from cmd in horizontal and vertical pos, neg, zero by dir_map
        return (direction[0]*int(command[1:]), direction[1]*int(command[1:]))

    def _add_vector(self, pos, vector):
        'Return step destination by adding vector to current position.'
        return (pos[0]+vector[0], pos[1]+vector[1])

    def _get_path(self, pos, dest):
        'Return set of coords between possition and destination.'
        path = set()
        if pos[0] == dest[0]:
            path = path.union(set([(pos[0], i) for i in range(pos[1], dest[1], 1 if dest[1]>pos[1] else -1)]))
        elif pos[1] == dest[1]:
            path = path.union(set([(i, pos[1]) for i in range(pos[0], dest[0], 1 if dest[0]>pos[0] else -1)]))
        else:
            raise ValueError('Non-perpendicular vector.')
        path.add(dest)
        return path

    def _get_common(self, keep_zero=False):
        'Return set of common nodes from self wires.'
        common = self.wire_a.intersection(self.wire_b)
        if not keep_zero:
            common.remove((0, 0))
        return common

    def get_closest_manhatton(self):
        'Return M. distance of closest wire intersection.'
        return min(map(self._get_m_dist, self._get_common()))


if __name__ == '__main__':
    w = Wires()
    print(w.get_closest_manhatton())
