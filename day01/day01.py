#!/usr/bin/env python

import itertools

def pairwise(d):
    for i in range(len(d)-1):
        yield(d[i], d[i+1])

def sliding(d, n):
    for i in range(len(d)-n+1):
        yield(d[i:i+n])

def readdata(filename):
    data=[]
    with open(filename, "r") as fh:
        for l in fh:
            data.append(int(l.strip()))
    return(data)

def countinc(d):
    return sum([x < y for x, y in pairwise(d)])

test=readdata("test.txt")
print(countinc(test))

inp=readdata("input.txt")
print(countinc(inp))

print(test)
for x in sliding(test, 3):
    print(x, sum(x))


print(countinc([sum(x) for x in sliding(test, 3)]))

print(countinc([sum(x) for x in sliding(inp, 3)]))
