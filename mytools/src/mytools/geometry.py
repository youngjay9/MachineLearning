PI = 3.14


def circle(radius):
    area = "%.1f" % (radius * radius * PI)
    length = "%.1f" % (2 * radius * PI)
    return area, length


def square(side):
    return side * side, 4 * side