#!/usr/bin/python3

from collections import Counter

from silver_star import RANGE_FROM, RANGE_TO
from silver_star import PassBreaker


class GoldPassBreaker(PassBreaker):
    def _fits(self, num):
        'Decide whether number meets friteria or not.'
        if num < RANGE_FROM or num > RANGE_TO:
            return False
        num = str(num)
        for i in range(1, len(num)):
            if num[i] < num[i-1]:
                return False
        return True if 2 in Counter(num).values() else False


if __name__ == '__main__':
    pb = GoldPassBreaker()
    print(pb.run())
