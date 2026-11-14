# Spurs API Reference

## 1. Algebra

The algebra module provides tools for working with logarithms and related operations.

It is a relatively small module at the moment, but it lays the groundwork for more advanced algebraic functionality in future releases

### Classes

**Logarithms**

Provides methods for calculating logarithms using different bases

Available methods:

- `log(x, base)` - Calculates the logarithm of x using the specified base
- `ln(x)` - Intended for calculating the natural logarithm of x
- `ilog(x, base)` - Finds the integer exponent when x is an exact power of the given base. Returns `None` if it is not
- `log2(x)` - Calculates the base 2 logarithm
- `log10(x)` - Calculates the base 10 logarithm
- `log1p(x, terms=100)` - Approximates a logarithmic value using a finite series

**Algebra**

Currently reserved for future algebraic functionality

## 2. Basics

The basics module handles everyday arithmetic and several useful mathematical operations. It also includes tools for number theory and discrete mathematics.

Think of it as the general-purpose toolbox. You will probably find yourself visiting this module quite often.

### Classes

**Basic**

Provides basic two-number arithmetic

Available methods:

- `add2(x, y)` - Adds two numbers
- `sub2(x, y)` - Subtracts the second number from the first
- `mul2(x, y)` - Multiplies two numbers
- `div2(x, y)` - Divides the first number by the second
- `mod2(x, y)` - Returns the remainder after division
- `idiv2(x, y)` - Performs floor division

**MultiopBasic**

Allows arithmetic operations involving multiple values.

The methods accept a collection of numbers rather than separate arguments

Available methods:

- `add(args)` - Adds all supplied values
- `sub(args)` - Subtracts subsequent values from the first value
- `mul(args)` - Multiplies all supplied values
- `div(args)` - Divides the first value by each subsequent value
- `mod(args)` - Applies modulo operations successively
- `idiv(args)` - Applies floor division successively

**GeneralBasic**

Provides additional mathematical operations, including number theory utilities

Available methods:

- `pow(x, y)` - Raises x to the power of y
- `root(x, y)` - Calculates the y-th root of x
- `gcd(x, y)` - Finds the greatest common divisor of two integers
- `lcm(x, y)` - Finds the least common multiple of two integers
- `prime_factors(n)` - Returns the prime factorisation of n
- `divisors(n)` - Returns the positive divisors of n
- `is_prime(n)` - Checks whether n is prime

**DiscreteMaths**

Provides tools for combinatorics and integer sequences

Available methods:

- `fact(n)` - Calculates the factorial of n
- `perm(n, r)` - Calculates permutations without repetition
- `comb(n, r)` - Calculates combinations without repetition
- `perm_rep(n, r)` - Calculates permutations with repetition
- `comb_rep(n, r)` - Calculates combinations with repetition
- `pair_count(n)` - Calculates the number of unique pairs that can be formed from n items
- `fibonacci(n)` - Returns the n-th Fibonacci number, with the sequence beginning at zero

## 3. Constants

The constants module provides a collection of predefined mathematical, physical, and astronomical constants.

No need to manually type out the speed of light or remember the value of pi every time cause I made sure Spurs has a great experience!

### Classes

**MathConstants**

Contains commonly used mathematical constants and numerical values

Some available attributes include:

- `pi`, `tau`, `e`
- `sqrt2`, `sqrt3`, `sqrt5`, `sqrt7`, `sqrt10`
- `ln2`, `ln3`, `ln10`
- `log2_e`, `log10_e`
- `golden_ratio`, `plastic_constant`
- `euler_gamma`, `catalan`, `apery`
- `inf`, `nan`
- `epsilon`, `max_float`, `min_float`

**PhysicalConstants**

Contains physical constants used in scientific calculations

Some available attributes include:

- `speed_of_light`
- `gravitational_constant`
- `planck_constant`
- `boltzmann_constant`
- `avogadro_constant`
- `gas_constant`
- `elementary_charge`
- `standard_gravity`
- `electron_mass`
- `proton_mass`
- `neutron_mass`

**AstroConstants**

Contains astronomical constants and reference values

Some available attributes include:

- `au`
- `light_year`
- `parsec`
- `kiloparsec`
- `megaparsec`
- `gigaparsec`
- `solar_mass`
- `solar_rad`
- `solar_luminosity`
- `earth_mass`
- `earth_mean_rad`
- `moon_mass`
- `jupiter_mass`

Values are stored numerically. Check the relevant physical units before using them in calculations.

## 4. Conversion

The conversion module makes switching between measurement units straightforward.

It supports everything from ordinary length and mass conversions to astronomical distances and digital storage units. Because apparently metres and megaparsecs are both things we need.

### Classes

**Converter**

The base class used by most conversion classes

Available methods:

- `units()` - Returns the supported units
- `to_base(from_, val)` - Converts a value into the class's base unit
- `from_base(to_, val)` - Converts a value from the base unit into the requested unit
- `convert(from_, to_, val)` - Converts directly between two supported units

**Available conversion classes**

- `Length` - Length and distance units, including metres, kilometres, astronomical units, light-years, and parsecs
- `Mass` - Mass units, including grams, kilograms, pounds, and atomic mass units
- `Time` - Time units, including seconds, minutes, hours, days, and years
- `Area` - Area units, including square metres, hectares, acres, and square miles
- `Volume` - Volume units, including litres, cubic metres, and gallons
- `Speed` - Speed units, including metres per second, kilometres per hour, and miles per hour
- `Acceleration` - Acceleration units, including metres per second squared and standard gravity
- `Temperature` - Temperature conversion between Kelvin, Celsius, Fahrenheit, and Rankine
- `Pressure` - Pressure units, including pascals, atmospheres, bar, and psi
- `Energy` - Energy units, including joules, calories, electronvolts, and watt-hours
- `Power` - Power units, including watts, kilowatts, and horsepower
- `Force` - Force units, including newtons, dynes, kilogram-force, and pound-force
- `Frequency` - Frequency units, including hertz and revolutions per minute
- `Angle` - Angular units, including radians, degrees, arcminutes, and arcseconds
- `Data` - Digital storage units, including bits, bytes, and binary prefixes
- `DataRate` - Data transfer rates, including bits per second and bytes per second

## 5. Geometry

The geometry module provides tools for calculating areas, perimeters, and working with two-dimensional coordinates.

From a simple square to an annulus, it handles a useful range of common geometric shapes.

### Classes

**Shapes**

Provides methods for calculating geometric properties

Available methods:

- `area(type, *args)` - Calculates the area of the specified shape
- `perimeter(type, *args)` - Calculates the perimeter of the specified shape

Supported shapes include:

- Square
- Rectangle
- Triangle
- Circle
- Parallelogram
- Trapezoid
- Rhombus
- Kite
- Ellipse
- Regular pentagon
- Regular hexagon
- Pentagon
- Hexagon
- Octagon
- Annulus

The required arguments depend on the selected shape. For example, a circle requires its radius, while a rectangle requires its length and width.

**Coordinates**

Provides basic utilities for working with Cartesian coordinates

Available methods:

- `in_quadrant(point)` - Determines which Cartesian quadrant contains the supplied point
- `distance(point1, point2)` - Calculates the Euclidean distance between two points

Points should be supplied as coordinate pairs containing x and y values.

## 6. Helpers

The helpers module contains small utility functions for common numerical checks.

Nothing particularly complicated here. Sometimes a simple function is all you need!

### Classes

**Helpers**

Available methods:

- `is_neg(n)` - Returns `True` if n is negative
- `is_pos(n)` - Returns `True` if n is positive
- `is_zero(n)` - Returns `True` if n is zero

These methods return Boolean values.

## 7. Statistics

The statistics module provides tools for analysing numerical datasets.

It covers common measures of central tendency as well as measures of dispersion. In other words, it helps you understand what your data is doing instead of just staring at a list of numbers.

### Classes

**BasicStatistics**

Provides descriptive statistical operations

Available methods:

- `mean(data)` - Calculates the arithmetic mean
- `median(data)` - Finds the median value
- `mode(data)` - Returns the value or values occurring most frequently
- `data_range(data)` - Calculates the difference between the maximum and minimum values
- `range_avg(data)` - Returns half of the data range
- `geo_mean(data)` - Calculates the geometric mean
- `harmonic_mean(data)` - Calculates the harmonic mean

**Dispersion**

Provides methods for measuring the spread of a dataset

Available methods:

- `variance(data)` - Calculates population variance
- `sample_variance(data)` - Calculates sample variance
- `std_deviation(data)` - Calculates population standard deviation
- `sample_std_deviation(data)` - Calculates sample standard deviation

The methods expect a non-empty dataset. Some calculations also have additional mathematical restrictions, such as the sample variance requiring more than one observation.

## 8. Trigonometry

The trigonometry module provides trigonometric, inverse trigonometric, and hyperbolic functions.

It also includes utilities for converting and normalising angles.

### Classes

**TrigUtils**

Provides utilities for working with angles

Available methods:

- `to_rad(deg)` - Converts degrees into radians
- `to_deg(rad)` - Converts radians into degrees
- `angle_norm(deg)` - Normalises an angle in degrees to the range from zero to less than 360
- `rad_norm(rad)` - Normalises an angle in radians to the range from zero to less than 2 pi
- `quadrant(angle)` - Determines the quadrant of an angle in degrees. Returns `None` for angles on the coordinate axes

**Trigonometry**

Provides standard and inverse trigonometric functions

Available methods:

- `sin(angle, deg=False)` - Calculates sine
- `cos(angle, deg=False)` - Calculates cosine
- `tan(angle, deg=False)` - Calculates tangent
- `cosec(angle, deg=False)` - Calculates cosecant
- `sec(angle, deg=False)` - Calculates secant
- `cot(angle, deg=False)` - Calculates cotangent
- `asin(value, deg=False)` - Calculates inverse sine
- `acos(value, deg=False)` - Calculates inverse cosine
- `atan(value, deg=False)` - Calculates inverse tangent
- `atan2(y, x, deg=False)` - Calculates the angle from the supplied Cartesian components

Angles are interpreted in radians by default. Set `deg=True` when supplying an angle in degrees or when you want an inverse trigonometric result in degrees.

**Hyperbolic**

Provides hyperbolic functions

Available methods:

- `sinh(x)` - Hyperbolic sine
- `cosh(x)` - Hyperbolic cosine
- `tanh(x)` - Hyperbolic tangent
- `asinh(x)` - Inverse hyperbolic sine
- `acosh(x)` - Inverse hyperbolic cosine
- `atanh(x)` - Inverse hyperbolic tangent

That's the current module lineup for you! More functionality will be added as Spurs grows, so this reference will evolve alongside the code rather than become a museum of outdated methods!
