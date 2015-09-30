from fractions import Fraction
from math import modf


class PriceDisplayFraction(object):
    def __init__(self, denominator=16):
        self.denom = denominator

    def to_display(self, cents):
        fractional, integer = modf(cents)
        f = Fraction(fractional).limit_denominator(self.denom)
        return '{}/{}'.format(integer / 100.0,
                              f.numerator * (self.denom / f.denominator))

    def to_internal(self, display):
        whole, numerator = (float(a) for a in display.split('/'))
        return whole * 100 + numerator / self.denom

pdf = PriceDisplayFraction(32)
assert pdf.to_internal("123.45/0") == 12345
assert pdf.to_display(12345) == "123.45/0"

pdf = PriceDisplayFraction(16)
assert pdf.to_internal("123.45/2") == 12345.125
assert pdf.to_display(12345.125) == "123.45/2"
