def lcm(num1,num2):
    """least common multiple"""
    return  (num1 * num2) // gcd(num1,num2)
def gcd(num1,num2):
    """Greatest common divisor"""
    return num1 if num2 == 0 else gcd(num2, num1%num2)
class Fraction:
    def __init__(self, numerator, denominator):
        self.top = numerator
        self.bottom = denominator
    def __eq__(self, other):
        first_num = self.top * other.bottom
        second_num = other.top * self.bottom
        return first_num == second_num
    def __str__(self):
        return "%s/%s" % (self.top, self.bottom)
    def __add__(self, other):
        fraction=lcm(self.bottom, other.bottom)
        top = self.top*fraction//self.bottom+other.top*fraction//other.bottom
        return Fraction(top,fraction) if gcd(top,fraction) == 1 else Fraction(top//gcd(top,fraction),fraction//gcd(top,fraction))
