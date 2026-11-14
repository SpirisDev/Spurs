import math

class MathConstants:
    pi = math.pi
    tau = math.tau
    e = math.e

    sqrt2 = math.sqrt(2)
    sqrt3 = math.sqrt(3)
    sqrt5 = math.sqrt(5)
    sqrt7 = math.sqrt(7)
    sqrt10 = math.sqrt(10)

    ln2 = math.log(2)
    ln3 = math.log(3)
    ln10 = math.log(10)

    log2_e = math.log2(math.e)
    log10_e = math.log10(math.e)

    deg_to_rad = pi / 180
    rad_to_deg = 180 / pi

    pi_over_2 = pi / 2
    pi_over_3 = pi / 3
    pi_over_4 = pi / 4
    pi_over_6 = pi / 6

    golden_ratio = (1 + math.sqrt(5)) / 2
    plastic_constant = 1.324717957244746
    euler_gamma = 0.5772156649015329
    catalan = 0.915965594177219
    apery = 1.202056903159594
    khinchin = 2.685452001065306
    glaisher = 1.282427129100623

    inf = math.inf
    nan = math.nan
    max_float = float.fromhex("0x1.fffffffffffffp+1023")
    min_float = float.fromhex("0x0.0000000000001p-1022")
    epsilon = math.ulp(1.0)

class PhysicalConstants:
    speed_of_light = 299792458
    gravitational_constant = 6.67430e-11
    planck_constant = 6.62607015e-34
    reduced_planck_constant = planck_constant / (2 * math.pi)
    elementary_charge = 1.602176634e-19
    boltzmann_constant = 1.380649e-23
    avogadro_constant = 6.02214076e23
    gas_constant = 8.31446261815324
    faraday_constant = 96485.33212331001
    vacuum_permittivity = 8.8541878188e-12
    vacuum_permeability = 1.25663706127e-6
    standard_gravity = 9.80665
    standard_atmosphere = 101325
    stefan_boltzmann_constant = 5.670374419e-8
    coulomb_constant = 1 / (4 * math.pi * vacuum_permittivity)
    electron_mass = 9.1093837139e-31
    proton_mass = 1.67262192595e-27
    neutron_mass = 1.67492750056e-27
    atomic_mass_constant = 1.66053906892e-27
    fine_structure_constant = 7.2973525643e-3
    rydberg_constant = 10973731.568157
    bohr_radius = 5.29177210544e-11
    hartree_energy = 4.359744722206e-18
    electron_volt = 1.602176634e-19
    julian_year = 365.25 * 24 * 60 * 60

class AstroConstants:
    au = 149597870700
    light_year = PhysicalConstants.speed_of_light * PhysicalConstants.julian_year
    parsec = au / math.tan(math.pi / (180 * 3600))
    kiloparsec = 1000 * parsec
    megaparsec = 1e6 * parsec
    gigaparsec = 1e9 * parsec

    solar_mass = 1.98847e30
    solar_rad = 6.957e8
    solar_luminosity = 3.828e26
    solar_effective_temp = 5772
    solar_grav_param = 1.3271244e20

    earth_mass = 5.9722e24
    earth_mean_rad = 6.371e6
    earth_equatorial_rad = 6.378137e6
    earth_polar_rad = 6.3567523e6
    earth_grav_param = 3.986004418e14

    moon_mass = 7.342e22
    moon_mean_rad = 1.7374e6
    moon_grav_param = 4.9048695e12
    mean_earth_moon_dist = 3.844e8

    jupiter_mass = 1.89813e27
    jupiter_mean_rad = 6.9911e7
    jupiter_grav_param = 1.2668653e17

    astronomical_unit_km = au / 1000
    light_year_km = light_year / 1000
    parsec_km = parsec / 1000

    seconds_per_day = 86400
    days_per_julian_year = 365.25
    julian_century_days = 36525