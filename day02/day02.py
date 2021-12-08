#!/usr/bin/env python

import re

class Instr:
    patt = re.compile(r"(.+) (\d+)")

    def __init__(self, direct, n):
        self.dir = direct
        self.n = n 

    def __repr__(self):
        return "Instr(dir={} n={})".format(self.dir, self.n)
     
    @classmethod
    def apply(cls, text):
        m = Instr.patt.match(text)
        if m:
            return Instr(m.group(1), int(m.group(2)))
        else:
            return None


def move(filename, debug=False):
    x = 0
    y = 0
    with open(filename, "r") as fh:
        for l in fh:
            ins = Instr.apply(l.strip())
            if ins.dir == 'forward':
                x += ins.n
            elif ins.dir == 'up':
                y -= ins.n
            elif ins.dir == 'down':
                y += ins.n
            if debug:
                print(ins, x, y)
    return x*y

def move2(filename, debug=False):
    x = 0
    y = 0
    aim = 0
    with open(filename, "r") as fh:
        for l in fh:
            ins = Instr.apply(l.strip())
            if ins.dir == 'forward':
                x += ins.n
                y += aim * ins.n
            elif ins.dir == 'up':
                aim -= ins.n
            elif ins.dir == 'down':
                aim += ins.n
            if debug:
                print(ins, x, y, aim)
    return x*y


print(move("test.txt", debug=True))

print(move("input.txt"))

print(move2("test.txt", debug=True))

print(move2("input.txt"))

        #m=patt.match(l.strip())
        #if m:
        #    print(m.group(1), m.group(2))
        #print(l.strip())


