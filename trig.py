from spurs.constants import MathConstants
import math

c = MathConstants()

class TrigUtils:
    def to_rad(self, deg: int):
        return deg*c.pi/180

    def to_deg(self, rad: int):
        return (rad*180)/c.pi

    def angle_norm(self, deg):
        return deg % 360

    def rad_norm(self, rad):
        return rad % (2*c.pi)

    def quadrant(self, angle):
        ang = self.angle_norm(angle)
        if ang == 0 or ang == 90 or ang == 180 or ang == 270: return None
        if 0 < ang < 90: return 1
        if 90 < ang < 180: return 2
        if 180 < ang < 270: return 3
        if 270 < ang < 360: return 4

class Trigonometry:
    def __init__(self):
        self.u = TrigUtils()

    def sin(self, angle, deg=False):
        if deg: angle = self.u.to_rad(angle)
        return math.sin(angle)

    def cos(self, angle, deg=False):
        if deg: angle = self.u.to_rad(angle)
        return math.cos(angle)

    def tan(self, angle, deg=False):
        if deg: angle = self.u.to_rad(angle)
        return math.tan(angle)

    def cosec(self, angle, deg=False):
        if deg: angle = self.u.to_rad(angle)
        return 1/self.sin(angle)

    def sec(self, angle, deg=False):
        if deg: angle = self.u.to_rad(angle)
        return 1/self.cos(angle)

    def cot(self, angle, deg=False):
        if deg: angle = self.u.to_rad(angle)
        return 1/self.tan(angle)

    def asin(self, value, deg=False):
        angle = math.asin(value)
        return self.u.to_deg(angle) if deg else angle

    def acos(self, value, deg=False):
        angle = math.acos(value)
        return self.u.to_deg(angle) if deg else angle

    def atan(self, value, deg=False):
        angle = math.atan(value)
        return self.u.to_deg(angle) if deg else angle

    def atan2(self, y, x, deg=False):
        angle = math.atan2(y, x)
        return self.u.to_deg(angle) if deg else angle

class Hyperbolic:
    def sinh(self, x):
        return math.sinh(x)

    def cosh(self, x):
        return math.cosh(x)

    def tanh(self, x):
        return math.tanh(x)

    def asinh(self, x):
        return math.asinh(x)

    def acosh(self, x):
        return math.acosh(x)

    def atanh(self, x):
        return math.atanh(x)