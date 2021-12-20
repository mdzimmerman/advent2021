from dataclasses import dataclass
import json
import math
from typing import List

def window(xs, size):
    for i in range(len(xs)-size+1):
        yield xs[i:i+size]

@dataclass
class Value:
    value: int
    pos: int
    depth: int
    path: List[int]

class SnailNum:
    def __init__(self, values):
        self.values = values
        
    def __repr__(self):
        tree = self.to_tree()
        def step(node):
            if isinstance(node, list):
                return "[{},{}]".format(step(node[0]), step(node[1]))
            else:
                return str(node)
        return step(tree)
    
    def __add__(self, other):
        out = []
        for v in self.values:
            out.append(Value(v.value, v.pos, v.depth+1, [0]+v.path))
        for v in other.values:
            out.append(Value(v.value, v.pos, v.depth+1, [1]+v.path))
        return SnailNum(out).reduce(debug=True)
    
    def to_tree(self):
        tree = []
    
        for val in self.values:
            node = tree
            for p in val.path:
                if p == 0 and len(node) == 0:
                    node.append([])
                elif p == 1 and len(node) == 1:
                    node.append([])
                node = node[p]
            node.append(val.value)
        return tree
    
    def find_explode(self):
        """Find index in self.values array of first element of the pair to be exploded."""
        
        for i, (a, b) in enumerate(window(self.values, 2)):
            if a.path == b.path and a.depth >= 4:
                return i
        return -1
            
    def explode(self, ei=None):
        if ei is None:
            ei = self.find_explode()
        if ei == -1:
            return self
        else:
            pi = None
            ni = None
            if ei > 0:
                pi = ei-1
            if ei < len(self.values)-2:
                ni = ei+2
            a = self.values[ei].value
            b = self.values[ei+1].value
            out = []
            for i, val in enumerate(self.values):
                if i == pi:
                    out.append(Value(val.value+a, val.pos, val.depth, val.path))
                elif i == ei:
                    out.append(Value(0, val.path[-1], val.depth-1, val.path[:-1]))
                elif i == ei+1:
                    pass
                elif i == ni:
                    out.append(Value(val.value+b, val.pos, val.depth, val.path))
                else:
                    out.append(val)
            return SnailNum(out)
   
    def find_split(self):
        for i, v in enumerate(self.values):
            if v.value > 9:
                return i
        return -1
            
    def split(self, si=None):
        if si is None:
            si = self.find_split()
        if si == -1:
            return self
        else:
            out = []
            for i, val in enumerate(self.values):
                if i == si:
                    x = val.value/2
                    a = math.floor(x)
                    b = math.ceil(x)
                    out.append(Value(a, 0, val.depth+1, val.path+[val.pos]))
                    out.append(Value(b, 1, val.depth+1, val.path+[val.pos]))
                else:
                    out.append(val)
            return SnailNum(out)
        
    def reduce(self, debug=False):
        curr = self
        
        while True:
            if curr.find_explode() != -1:
                curr = curr.explode()
            elif curr.find_split() != -1:
                curr = curr.split()
            else:
                break

        return curr               
           
    @classmethod
    def from_string(cls, s):
        tree = json.loads(s)
        values = []
        def step(node, depth, path):
            for pos, subnode in enumerate(node):
                if isinstance(subnode, list):
                    step(subnode, depth+1, path+[pos])
                else:
                    values.append(Value(subnode, pos, depth, path.copy()))
        step(tree, 0, [])
        return SnailNum(values)