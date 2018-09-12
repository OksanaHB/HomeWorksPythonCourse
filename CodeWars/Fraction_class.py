def mcm(num1,num2):
    return  (num1 * num2) // mcd(num1,num2)
def mcd(num1,num2):
    return num1 if num2 == 0 else mcd(num2, num1%num2)
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
        fraction=mcm(self.bottom, other.bottom)
        top = int(self.top*fraction/self.bottom+other.top*fraction/other.bottom)

        return Fraction(top,fraction) if mcd(top,fraction) == 1 else Fraction(int(top/mcd(top,fraction)),int(fraction/mcd(top,fraction)))

