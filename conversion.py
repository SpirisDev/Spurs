class Converter:
    BASE = ""
    UNITS = {}

    def units(self): return tuple(self.UNITS)
    def to_base(self, from_, val):
        if from_ not in self.UNITS: raise ValueError(f"Unknown unit: {from_}")
        return val * self.UNITS[from_]

    def from_base(self, to_, val):
        if to_ not in self.UNITS: raise ValueError(f"Unknown unit: {to_}")
        return val / self.UNITS[to_]

    def convert(self, from_, to_, val): return self.from_base(to_, self.to_base(from_, val))


class Length(Converter):
    BASE = "m"
    UNITS = {
        "pm": 1e-12, "nm": 1e-9, "um": 1e-6, "mm": 1e-3,
        "cm": 1e-2, "dm": 1e-1, "m": 1, "dam": 1e1, "hm": 1e2, "km": 1e3,
        "thou": 2.54e-5, "in": 0.0254, "ft": 0.3048, "yd": 0.9144,
        "mi": 1609.344, "nmi": 1852,
        "AU": 1.495978707e11, "ly": 9.460730472e15,
        "pc": 3.0856775814913673e16, "kpc": 3.0856775814913673e19,
        "Mpc": 3.0856775814913673e22, "Gpc": 3.0856775814913673e25
    }


class Mass(Converter):
    BASE = "kg"
    UNITS = {
        "ug": 1e-9, "mg": 1e-6, "g": 1e-3, "kg": 1,
        "tonne": 1e3, "t": 1e3, "oz": 0.028349523125, "lb": 0.45359237,
        "stone": 6.35029318, "short_ton": 907.18474, "long_ton": 1016.0469088,
        "u": 1.66053906660e-27, "Da": 1.66053906660e-27
    }


class Time(Converter):
    BASE = "s"
    UNITS = {
        "ns": 1e-9, "us": 1e-6, "ms": 1e-3, "s": 1,
        "min": 60, "h": 3600, "day": 86400, "week": 604800,
        "fortnight": 1209600, "year_julian": 31557600, "year_gregorian": 31556952
    }


class Area(Converter):
    BASE = "m2"
    UNITS = {
        "mm2": 1e-6, "cm2": 1e-4, "dm2": 1e-2, "m2": 1,
        "are": 100, "ha": 10000, "km2": 1e6,
        "in2": 0.00064516, "ft2": 0.09290304, "yd2": 0.83612736,
        "acre": 4046.8564224, "mi2": 2589988.110336
    }


class Volume(Converter):
    BASE = "m3"
    UNITS = {
        "mm3": 1e-9, "cm3": 1e-6, "uL": 1e-9, "mL": 1e-6,
        "dL": 1e-4, "L": 1e-3, "m3": 1, "km3": 1e9,
        "in3": 1.6387064e-5, "ft3": 0.028316846592, "yd3": 0.764554857984,
        "US_fl_oz": 2.95735295625e-5, "US_cup": 0.0002365882365,
        "US_pt": 0.000473176473, "US_qt": 0.000946352946,
        "US_gal": 0.003785411784, "UK_gal": 0.00454609
    }


class Speed(Converter):
    BASE = "m/s"
    UNITS = {
        "mm/s": 1e-3, "cm/s": 1e-2, "m/s": 1, "km/s": 1e3,
        "km/h": 1/3.6, "mph": 0.44704, "ft/s": 0.3048,
        "knot": 0.5144444444444445, "Mach": 340.29
    }


class Acceleration(Converter):
    BASE = "m/s2"
    UNITS = {
        "mm/s2": 1e-3, "cm/s2": 1e-2, "m/s2": 1,
        "ft/s2": 0.3048, "g0": 9.80665
    }


class Temperature:
    BASE = "K"
    UNITS = ("K", "C", "F", "R")

    def units(self): return self.UNITS

    def to_base(self, from_, val):
        if from_ == "K": result = val
        elif from_ == "C": result = val + 273.15
        elif from_ == "F": result = (val - 32) * 5/9 + 273.15
        elif from_ == "R": result = val * 5/9
        else: raise ValueError(f"Unknown temperature unit: {from_}")
        if result < 0: raise ValueError("Below absolute zero")
        return result

    def from_base(self, to_, val):
        if val < 0: raise ValueError("Below absolute zero")
        if to_ == "K": return val
        if to_ == "C": return val - 273.15
        if to_ == "F": return (val - 273.15) * 9/5 + 32
        if to_ == "R": return val * 9/5
        raise ValueError(f"Unknown temperature unit: {to_}")

    def convert(self, from_, to_, val): return self.from_base(to_, self.to_base(from_, val))


class Pressure(Converter):
    BASE = "Pa"
    UNITS = {
        "Pa": 1, "hPa": 100, "kPa": 1e3, "MPa": 1e6, "GPa": 1e9,
        "bar": 1e5, "mbar": 100, "atm": 101325, "torr": 101325/760,
        "mmHg": 133.322387415, "psi": 6894.757293168, "ksi": 6894757.293168
    }


class Energy(Converter):
    BASE = "J"
    UNITS = {
        "uJ": 1e-6, "mJ": 1e-3, "J": 1, "kJ": 1e3, "MJ": 1e6, "GJ": 1e9,
        "Wh": 3600, "kWh": 3.6e6, "MWh": 3.6e9,
        "cal": 4.184, "kcal": 4184, "eV": 1.602176634e-19,
        "keV": 1.602176634e-16, "MeV": 1.602176634e-13,
        "GeV": 1.602176634e-10, "erg": 1e-7, "BTU": 1055.05585262,
        "ft_lbf": 1.3558179483314
    }


class Power(Converter):
    BASE = "W"
    UNITS = {
        "uW": 1e-6, "mW": 1e-3, "W": 1, "kW": 1e3, "MW": 1e6, "GW": 1e9,
        "hp_mechanical": 745.6998715822702, "hp_metric": 735.49875,
        "BTU_per_h": 0.2930710701722222
    }


class Force(Converter):
    BASE = "N"
    UNITS = {
        "N": 1, "kN": 1e3, "MN": 1e6, "dyn": 1e-5,
        "kgf": 9.80665, "lbf": 4.4482216152605, "kip": 4448.2216152605
    }


class Frequency(Converter):
    BASE = "Hz"
    UNITS = {
        "uHz": 1e-6, "mHz": 1e-3, "Hz": 1, "kHz": 1e3,
        "MHz": 1e6, "GHz": 1e9, "THz": 1e12, "rpm": 1/60
    }


class Angle(Converter):
    BASE = "rad"
    UNITS = {
        "rad": 1, "deg": 3.141592653589793/180,
        "arcmin": 3.141592653589793/10800,
        "arcsec": 3.141592653589793/648000,
        "turn": 2*3.141592653589793,
        "grad": 3.141592653589793/200,
        "mas": 3.141592653589793/648000000
    }


class Data(Converter):
    BASE = "bit"
    UNITS = {
        "bit": 1, "B": 8, "kbit": 1e3, "Mbit": 1e6, "Gbit": 1e9, "Tbit": 1e12,
        "KB": 8e3, "MB": 8e6, "GB": 8e9, "TB": 8e12,
        "KiB": 8*1024, "MiB": 8*1024**2, "GiB": 8*1024**3, "TiB": 8*1024**4,
        "Kibit": 1024, "Mibit": 1024**2, "Gibit": 1024**3, "Tibit": 1024**4
    }


class DataRate(Converter):
    BASE = "bit/s"
    UNITS = {
        "bit/s": 1, "kbit/s": 1e3, "Mbit/s": 1e6, "Gbit/s": 1e9,
        "B/s": 8, "KB/s": 8e3, "MB/s": 8e6, "GB/s": 8e9,
        "KiB/s": 8*1024, "MiB/s": 8*1024**2, "GiB/s": 8*1024**3
    }