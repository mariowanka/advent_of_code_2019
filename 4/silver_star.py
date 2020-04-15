#!/usr/bin/python3

RANGE_FROM = 145852
RANGE_TO = 616942


class PassBreaker():
    def __init__(self):
        self.fitting = []

    def _fits(self, num):
        'Decide whether number meets friteria or not.'
        if num < RANGE_FROM or num > RANGE_TO:
            return False
        num = str(num)
        adj = False
        for i in range(1, len(num)):
            if num[i] < num[i-1]:
                return False
            if num[i] == num[i-1]:
                adj = True
        return adj

    def run(self):
        for num in range(RANGE_FROM+1, RANGE_TO):
            if self._fits(num):
                self.fitting.append(num)
        return len(self.fitting)


if __name__ == '__main__':
    pb = PassBreaker()
    print(pb.run())