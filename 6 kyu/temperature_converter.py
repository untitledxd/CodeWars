TO_KELVIN = {
    'C': (1, 273.15),
    'F': (5.0 / 9, 459.67 * 5.0 / 9),
    'R': (5.0 / 9, 0),
    'De': (-2.0 / 3, 373.15),
    'N': (100.0 / 33, 273.15),
    'Re': (5.0 / 4, 273.15),
    'Ro': (40.0 / 21, -7.5 * 40 / 21 + 273.15),
}


def convert_temp(temp, from_scale, to_scale):
    """ Thanks to 'jolaf' on CodeWars (much better than my solution) """
    if from_scale == to_scale:
        return temp
    if from_scale != 'K':
        (a, b) = TO_KELVIN[from_scale]
        temp = a * temp + b
        if to_scale == 'K':
            return int(round(temp))
    a, b = TO_KELVIN[to_scale]
    return int(round((temp - b) / a))

assert convert_temp(100, 'C', 'F') == 212
assert convert_temp(-30, 'De', 'K') == 393
assert convert_temp(40, 'Re', 'C') == 50
assert convert_temp(60, 'De', 'F') == 140
assert convert_temp(373.15, 'K', 'N') == 33
assert convert_temp(666, 'K', 'K') == 666
