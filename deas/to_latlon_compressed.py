import math
def to_latlon(easting, northing):
    K0 = 0.9996

    E = 0.00669438
    E2 = E * E
    E3 = E2 * E
    E_P2 = E / (1 - E)

    SQRT_E = math.sqrt(1 - E)
    _E = (1 - SQRT_E) / (1 + SQRT_E)
    _E2 = _E * _E
    _E3 = _E2 * _E
    _E4 = _E3 * _E
    _E5 = _E4 * _E

    M1 = (1 - E / 4 - 3 * E2 / 64 - 5 * E3 / 256)
    M2 = (3 * E / 8 + 3 * E2 / 32 + 45 * E3 / 1024)
    M3 = (15 * E2 / 256 + 45 * E3 / 1024)
    M4 = (35 * E3 / 3072)

    P2 = (3 / 2 * _E - 27 / 32 * _E3 + 269 / 512 * _E5)
    P3 = (21 / 16 * _E2 - 55 / 32 * _E4)
    P4 = (151 / 96 * _E3 - 417 / 128 * _E5)
    P5 = (1097 / 512 * _E4)

    R = 6378137

    zone_letter = "N"
    zone_number = 30

    x = easting - 500000
    y = northing

    m = y / K0
    mu = m / (R * M1)

    p_rad = (mu +
             P2 * math.sin(2 * mu) +
             P3 * math.sin(4 * mu) +
             P4 * math.sin(6 * mu) +
             P5 * math.sin(8 * mu))

    p_sin = math.sin(p_rad)
    p_sin2 = p_sin * p_sin

    p_cos = math.cos(p_rad)

    p_tan = p_sin / p_cos
    p_tan2 = p_tan * p_tan
    p_tan4 = p_tan2 * p_tan2

    ep_sin = 1 - E * p_sin2
    ep_sin_sqrt = math.sqrt(1 - E * p_sin2)

    n = R / ep_sin_sqrt
    r = (1 - E) / ep_sin

    c = E_P2 * p_cos**2
    c2 = c * c

    d = x / (n * K0)
    d2 = d * d
    d3 = d2 * d
    d4 = d3 * d
    d5 = d4 * d
    d6 = d5 * d

    latitude = (p_rad - (p_tan / r) *
                (d2 / 2 -
                 d4 / 24 * (5 + 3 * p_tan2 + 10 * c - 4 * c2 - 9 * E_P2)) +
                 d6 / 720 * (61 + 90 * p_tan2 + 298 * c + 45 * p_tan4 - 252 * E_P2 - 3 * c2))

    longitude = (d -
                 d3 / 6 * (1 + 2 * p_tan2 + c) +
                 d5 / 120 * (5 - 2 * c + 28 * p_tan2 - 3 * c2 + 8 * E_P2 + 24 * p_tan4)) / p_cos
    print("1",longitude)
    def zone_number_to_central_longitude():
        return (30 - 1) * 6 - 180 + 3

    def mod_angle(value):
        return (value + math.pi) % (2 * math.pi) - math.pi

    longitude = mod_angle(longitude + math.radians(zone_number_to_central_longitude()))
    print("2",longitude)

    print("3",math.degrees(longitude))

    return (math.degrees(latitude),
            math.degrees(longitude))

test = to_latlon(443123, 4475002)
print(test)
a = (40.42370631920457,-3.6704814712125287)
# print(test==a)
b = to_latlon(461786, 4547515)
# print("AA", b)