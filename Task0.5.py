from math import sqrt

def area_of_triangle(side1, side2, side3):
    s = 0.5 * (side1 + side2 + side3)
    a = sqrt(s * (s - side1) * (s - side2) * (s - side3))
    return a + "sq.units"

area_of_triangle(3,4,5)
