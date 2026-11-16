
"""
Spurs - Mathematical Framework for Python
"""

__version__ = "0.3.0"
__author__ = "Spiris"

from spurs.array import Array
from spurs.algebra import Algebra, Logarithms
from spurs.basics import (
    Basic,
    MultiopBasic,
    GeneralBasic,
    DiscreteMaths,
)
from spurs.constants import (
    MathConstants,
    PhysicalConstants,
    AstroConstants,
)
from spurs.conversion import (
    Length,
    Mass,
    Time,
    Area,
    Volume,
    Speed,
    Acceleration,
    Temperature,
    Pressure,
    Energy,
    Power,
    Force,
    Frequency,
    Angle,
    Data,
    DataRate,
)
from spurs.geometry import Shapes, Coordinates
from spurs.helpers import Helpers
from spurs.statistics import BasicStatistics, Dispersion
from spurs.trig import TrigUtils, Trigonometry, Hyperbolic
