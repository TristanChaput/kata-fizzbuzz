from types import FunctionType
from utils import is_multiple_of, is_odd, is_perfect_square

BUZZ = "buzz"
FIZZ = "fizz"
BIZZ = "bizz"
FUZZ = "fuzz"


def fizzbuzz(number: int):
    return fizzbuzz_logic(number, fizz_n=3, buzz_n=5)


def fizz_buzz_iter_2(number: int):
    return fizzbuzz_logic(number, fizz_n=7, buzz_n=11)


def fizz_buzz_iter_3(number: int):
    return fizzbuzz_logic(number, fizz_n=13, buzz_n=17, fuzz_n=19, bizz_n=23)


def super_fizz_buzz(number: int):
    return super_fizzbuzz_logic(
        number,
        fizz_f=lambda x: not is_multiple_of(x, 3),
        buzz_f=is_odd,
        fuzz_f=is_perfect_square,
    )


def fizzbuzz_logic(
    number: int,
    fizz_n: int = None,
    buzz_n: int = None,
    fuzz_n: int = None,
    bizz_n: int = None,
):
    return super_fizzbuzz_logic(
        number,
        lambda x: is_multiple_of(x, fizz_n) if fizz_n else None,
        lambda x: is_multiple_of(x, buzz_n) if buzz_n else None,
        lambda x: is_multiple_of(x, fuzz_n) if fuzz_n else None,
        lambda x: is_multiple_of(x, bizz_n) if bizz_n else None,
    )


def super_fizzbuzz_logic(
    number: int,
    fizz_f: FunctionType = None,
    buzz_f: FunctionType = None,
    fuzz_f: FunctionType = None,
    bizz_f: FunctionType = None,
):
    result = ""
    if fizz_f:
        if fizz_f(number):
            result += FIZZ
    if buzz_f:
        if buzz_f(number):
            result += BUZZ
    if fuzz_f:
        if fuzz_f(number):
            result += FUZZ
    if bizz_f:
        if bizz_f(number):
            result += BIZZ
    if result == "":
        return str(number)
    return result
