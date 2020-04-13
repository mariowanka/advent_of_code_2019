#!/usr/bin/python3

from silver_star import INFILE
from silver_star import Wires


class GoldWires(Wires):
    def _get_wire_map(self, wire):
        'Return dict of lengths on path.'
        pos = (0, 0)
        length = 0
        wire_map = {}
        for command in wire:
            vector = self._translate_direction(command)
            step_dest = self._add_vector(pos, vector)
            wire_map.update(self._get_path(pos, step_dest, length))
            pos = step_dest
            length = wire_map[step_dest]
        return wire_map

    def _get_path(self, pos, dest, length):
        'Return dict of lengths on coords between possition and destination.'
        path = {}
        if pos[0] == dest[0]:
            for i in range(pos[1], dest[1], 1 if dest[1]>pos[1] else -1):
                if (pos[0], i) not in path:
                    path[(pos[0], i)] = length
                length += 1
        elif pos[1] == dest[1]:
            for i in range(pos[0], dest[0], 1 if dest[0]>pos[0] else -1):
                if (i, pos[1]) not in path:
                    path[(i, pos[1])] = length
                length += 1
        else:
            raise ValueError('Non-perpendicular vector.')
        path[dest] = length
        return path

    def get_closest_length(self):
        'Return closest intersection by sum of length.'
        intersections = set()
        for step in self.wire_a:
            if step in self.wire_b:
                intersections.add(self.wire_a[step] + self.wire_b[step])
        intersections.remove(0)
        return min(intersections)

if __name__ == '__main__':
    w = GoldWires()
    print(w.get_closest_length())
