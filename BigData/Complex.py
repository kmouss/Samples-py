class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, OtherValue):
        return Complex(self.real + OtherValue.real, self.imaginary + OtherValue.imaginary)

    def __sub__(self, OtherValue):
        return Complex(self.real - OtherValue.real, self.imaginary - OtherValue.imaginary)

    def __mul__(self, OtherValue):
        return Complex(self.real * OtherValue.real - self.imaginary * OtherValue.imaginary,
                       self.real * OtherValue.imaginary + self.imaginary * OtherValue.real)

    def __truediv__(self, OtherValue):
        return Complex((self.real * OtherValue.real + self.imaginary * OtherValue.imaginary) / (
        OtherValue.real ** 2 + OtherValue.imaginary ** 2),
                       (self.real * (-OtherValue.imaginary) + self.imaginary * OtherValue.real) / (
                       OtherValue.real ** 2 + OtherValue.imaginary ** 2))

    def mod(self):
        return Complex((self.real ** 2 + self.imaginary ** 2) ** (1 / 2), 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result