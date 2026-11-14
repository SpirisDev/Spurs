class Basic:
    def add2(self, x: float, y: float):
        return x+y

    def sub2(self, x: float, y: float):
        return x-y

    def mul2(self, x: float, y: float):
        return x*y

    def div2(self, x: float, y: float):
        return x/y

    def mod2(self, x: float, y: float):
        return x%y

    def idiv2(self, x: int, y: int):
        return x//y


class MultiopBasic:
    def add(self, *args: float):
        return sum(args)

    def sub(self, *args: float):
        diff = args[0]
        modargs = args[1:]
        for n in modargs:
            diff -= n
        return diff

    def mul(self, *args: float):
        prod = 1
        for n in args:
           prod *= n
        return prod

    def div(self, *args: float):
        quo = args[0]
        modargs = args[1:]
        for n in modargs:
            quo /= n
        return quo

    def mod(self, *args: float):
        rem = args[0]
        modargs = args[1:]
        for n in modargs:
            rem %= n
        return rem

    def idiv(self, *args: int):
        quo = args[0]
        modargs = args[1:]
        for n in modargs:
            quo //= n
        return quo

class GeneralBasic:
    def pow(self, x: float, y: int):
        return x ** y

    def root(self, x: float, y: int):
        return x ** (1/y)

    def gcd(self, x: int, y: int):
        x, y = abs(x), abs(y)
        while y:
            x, y = y, x%y
        return x

    def lcm(self, x: int, y: int):
        x, y = abs(x), abs(y)
        return (x/(self.gcd(x,y)))*y

    def prime_factors(self, n: int):
        if n < 1: raise ValueError("n cannot be less than 1")
        factors = []
        while n % 2 == 0:
            factors.append(2)
            n //= 2
        d = 3
        while d*d <= n:
            while n % d == 0:
                factors.append(d)
                n //= d
            d += 2
        if n > 1:
            factors.append(n)
        return factors

    def divisors(self, n: int):
        divisors = []
        for d in range(1, n+1):
            if n%d == 0:
                divisors.append(d)
        return divisors

    def is_prime(self, n: int):
        if n < 2: return False
        if n == 2: return True
        if n % 2 == 0: return False
        d = 3
        while d * d <= n:
            if n % d == 0:
                return False
            d += 2
        return True

class DiscreteMaths:
    def fact(self, n: int):
        if n <= 1: raise ValueError("n must be greater than 1")
        i = n-1
        while i != 1:
            n *= i
            i -= 1
        return n

    def perm(self, n: int, r: int):
        return self.fact(n)//self.fact(n-r)

    def comb(self, n: int, r: int):
        return self.perm(n,r)//self.fact(r)

    def perm_rep(self, n: int, r: int):
        return n**r

    def comb_rep(self, n: int, r: int):
        return self.fact(n+r-1)//(self.fact(r)*self.fact(n-1))

    def pair_count(self, n):
        return n * (n - 1) // 2

    def fibonacci(self, n):
        if n < 0: raise ValueError("n must be non-negative")
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a