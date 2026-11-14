# Spurs Math Framework

## What it is

**Spurs** is a general-purpose mathematical framework meant to be used like a _swiss army knife_. It is slower than raw python or optimized frameworks like _Numpy_ on operations it supports, but it's sheer amount of operations should be making up for that limit.

---

## Background

**Spurs** is the next generation of [Clawpy](https://pypi.org/project/clawpy/), which was my first framework. Due to it's success, I decided to retry it by hand. If you couldn't tell, Clawpy was made using AI, so I made Spurs by hand to learn Python even deeper and to redeem myself. If you still want to use Clawpy, feel free!

---

## API

Spurs provides a collection of mathematical tools designed to make working with mathematics in Python a little less tedious - and hopefully a little more enjoyable.

Whether you're dealing with logarithms, number theory, geometry, statistics, unit conversions, or trigonometry, Spurs aims to keep things organised and accessible.

The API is divided into several modules, each focusing on a particular area of mathematics.

### Modules

| Module       | Description                                                                   |
| ------------ | ----------------------------------------------------------------------------- |
| `algebra`    | Logarithmic operations and related algebraic utilities.                       |
| `basics`     | Arithmetic, number theory, prime factorisation, combinatorics, and sequences. |
| `constants`  | Mathematical, physical, and astronomical constants.                           |
| `conversion` | Unit conversions across several measurement categories.                       |
| `geometry`   | Geometrical calculations and coordinate utilities.                            |
| `helpers`    | Small utility functions for common mathematical checks.                       |
| `statistics` | Descriptive statistics and measures of dispersion.                            |
| `trig`       | Trigonometric, inverse trigonometric, and hyperbolic functions.               |

### Getting started

You don't need to import the entire mathematical universe just to calculate a logarithm.

Import the classes you need:

```py
from spurs import Logarithms, GeneralBasic, Trigonometry

log = Logarithms()
maths = GeneralBasic()
trig = Trigonometry()
```

And you're ready to go!

check [API.md](API.md) for the full functions list and APIs...

---
