class Array:
    def _check_len(self, a, b):
        if len(a) != len(b): raise ValueError("Arrays must have equal lengths")

    def add_arr(self, a, b):
        self._check_len(a, b)
        return [x + y for x, y in zip(a, b)]

    def sub_arr(self, a, b):
        self._check_len(a, b)
        return [x - y for x, y in zip(a, b)]

    def mul_arr(self, a, b):
        self._check_len(a, b)
        return [x * y for x, y in zip(a, b)]

    def div_arr(self, a, b):
        self._check_len(a, b)
        if any(y == 0 for y in b): raise ZeroDivisionError("Can't divide by zero")
        return [x / y for x, y in zip(a, b)]

    def pow_arr(self, a, b):
        self._check_len(a, b)
        return [x ** y for x, y in zip(a, b)]

    def pow_val(self, a, exp):
        return [x ** exp for x in a]

    def abs_arr(self, a):
        return [abs(x) for x in a]

    def negate_arr(self, a):
        return [-x for x in a]

    def sum_arr(self, a):
        return sum(a)

    def average_arr(self, a):
        if not a: raise ValueError("Empty Array")
        return sum(a) / len(a)

    def max_arr(self, a):
        if not a: raise ValueError("Empty Array")
        return max(a)

    def min_arr(self, a):
        if not a: raise ValueError("Empty Array")
        return min(a)

    def range_arr(self, a):
        if not a: raise ValueError("Empty Array")
        return max(a) - min(a)