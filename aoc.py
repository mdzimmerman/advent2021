def readlines(filename):
    lines = []
    with open(filename, "r") as fh:
        for l in fh:
            lines.append(l.strip())
    return lines

def splitlist(xs, sep):
    out = [[]]
    for x in xs:
        if x == sep:
            out.append([])
        else:
            out[-1].append(x)
    return out