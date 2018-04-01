#!/usr/bin/env python3

import sys

def tint(value, by_factor):
    return value + (255-value) * by_factor

f = float(sys.argv[1])
for color in sys.argv[2:]:
    r = int(color[0:2], 16)
    g = int(color[2:4], 16)
    b = int(color[4:6], 16)
    print("%.2x%.2x%.2x" % (tint(r, f), tint(g, f), tint(b, f)))
