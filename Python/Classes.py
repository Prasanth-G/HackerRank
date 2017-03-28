######1.Classes: Dealing with complex Numbers
'''
Sample Input
2 1
5 6
Sample Output
7.00+7.00i
-3.00-5.00i
4.00+17.00i
0.26-0.11i
2.24+0.00i
7.81+0.00i
'''
class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    def __add__(self, no):
        return Complex(no.real+self.real, no.imaginary+self.imaginary)
    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)
    def __mul__(self, no):
        return Complex(self.real*no.real - self.imaginary*no.imaginary, self.real*no.imaginary + self.imaginary*no.real)
    def __truediv__(self, no):
        m = Complex(self.real,self.imaginary)*Complex(no.real,-1 * no.imaginary)
        d = no.real**2 + no.imaginary**2
        return Complex(m.real/d , m.imaginary/d )
    def mod(self):
        return Complex(math.sqrt(self.real**2 + self.imaginary**2),0)
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

######2.Find the Torsional Angle
'''
Sample Input
0 4 5
1 7 6
0 5 9
1 7 2
Sample Output
8.19
'''
class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __sub__(self, no):
        return Points(no.x - self.x, no.y - self.y, no.z - self.z)
    def dot(self, no):
        return self.x * no.x + self.y * no.y + self.z * no.z
    def cross(self, no):
        return Points(self.y*no.z - self.z*no.y, self.z*no.x - self.x*no.z, self.x*no.y - self.y*no.x)
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)