import math
from spurs.constants import MathConstants as mc

class Algebra:
    pass

class Logarithms:
    def log(self, x, base):
        return math.log(x, base)

    def ln(self, x):
        return self.log(x, mc.e)

    def ilog(self, x, base):
        ex = 0
        while x % base == 0:
            x //= base
            ex += 1
        if x != 1: return None
        return ex

    def log2(self, x): return self.log(x, 2)

    def log10(self, x): return self.log(x, 10)

    def log1p(self, x, terms=100):
        t = 0.0
        pow = x
        for n in range(1, terms + 1):
            if n % 2: t += pow / n
            else: t -= pow / n
            pow *= x
        return t
