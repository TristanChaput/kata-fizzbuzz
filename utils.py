from math import sqrt


def is_perfect_square(number: int):
    x = int(sqrt(number))
    return (x * x) == number


def is_odd(number: int):
    return number % 2 != 0


def is_multiple_of(x: int, y: int):
    return x % y == 0
