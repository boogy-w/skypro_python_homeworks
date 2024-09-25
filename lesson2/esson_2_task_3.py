import math


def square(side):
    area = side * side
    return math.ceil(area)


length = 4.5
print(f"Площадь квадрата со стороной {length} равна {square(length)}")
