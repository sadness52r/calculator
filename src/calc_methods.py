def summ(a: int, b: int) -> int:
    return a + b


def sub(a: int, b: int) -> int:
    return a - b


def mult(a: int, b: int) -> int:
    return a * b


def div(a: int, b: int) -> float:
    if b == 0:
        return 999999999999999999999
    return a / b


def mod(a: int, b: int) -> int:
    if b == 0:
        return 999999999999999999998
    return a % b


def modulo(a: int) -> int:
    return abs(a)


def summFloat(a: float, b: float) -> float:
    return a + b


def subFloat(a: float, b: float) -> float:
    return a - b


def multFloat(a: float, b: float) -> float:
    return a * b


def divFloat(a: float, b: float) -> float:
    if b == 0:
        return 999999999999999999999
    return a / b


def moduloFloat(a: float) -> float:
    return abs(a)
