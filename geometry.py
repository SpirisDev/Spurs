from spurs.constants import MathConstants
from spurs.basics import GeneralBasic
from spurs.helpers import Helpers

mc = MathConstants()
gb = GeneralBasic()
h = Helpers()

class Shapes:
    def area(self, type, *args):
        if type == "square": return args[0] * args[0]
        elif type == "rect" or type == "parallelogram": return args[0] * args[1]
        elif type == "triangle": return 0.5 * args[0] * args[1]
        elif type == "circle": return mc.pi * args[0] * args[0]
        elif type == "trapezoid": return 0.5 * (args[0] + args[1]) * args[2]
        elif type == "rhombus" or type == "kite": return 0.5 * args[0] * args[1]
        elif type == "ellipse": return mc.pi * args[0] * args[1]
        elif type == "reg_pentagon": return 0.25 * gb.root(5*(5+2*mc.sqrt5)*args[0]*args[0], 2)
        elif type == "reg_hexagon": return (3*mc.sqrt3)/2 * args[0] * args[0]
        elif type == "annulus": return mc.pi * (args[0]*args[0] - args[1]*args[1])
        else: raise ValueError(f"Unknown shape: {type}")

    def perimeter(self, type, *args):
        if type == "square": return 4 * args[0]
        elif type == "rect": return 2 * (args[0] + args[1])
        elif type == "triangle": return args[0] + args[1] + args[2]
        elif type == "circle": return 2 * mc.pi * args[0]
        elif type == "parallelogram": return 2 * (args[0] + args[1])
        elif type == "trapezoid": return args[0] + args[1] + args[2] + args[3]
        elif type == "rhombus": return 4 * args[0]
        elif type == "kite": return 2 * (args[0] + args[1])
        elif type == "ellipse": return mc.pi * (3 * (args[0] + args[1]) - mc.sqrt((3 * args[0] + args[1]) * (args[0] + 3 * args[1])))
        elif type == "pentagon": return 5 * args[0]
        elif type == "hexagon": return 6 * args[0]
        elif type == "octagon": return 8 * args[0]
        elif type == "annulus": return 2 * mc.pi * (args[0] + args[1])
        else: raise ValueError(f"Unknown shape: {type}")

class Coordinates:
    def in_quadrant(self, point):
        x, y = point
        if h.is_neg(x):
            if h.is_neg(y): return 3
        if not h.is_neg(x):
            if not h.is_neg(y): return 1
        if not h.is_neg(x):
            if h.is_neg(y): return 4
        if h.is_neg(x):
            if not h.is_neg(y): return 2

    def distance(self, point1, point2):
        x1, y1 = point1
        x2, y2 = point2
        return ((x2-x1)**2 + (y2-y1)**2)**0.5