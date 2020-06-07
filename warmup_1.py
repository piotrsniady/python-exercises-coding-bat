import datetime

now = datetime.datetime.now()
h = now.hour


def diff21(n: int) -> int:
    val_range = range(0, 22)
    if n in val_range:
        return abs(n - 21)
    return n - 21


def front3(string: str) -> str:
    return string[:3]*3


def front_back(string: str) -> str:
    return string[-1] + string[1:-1] + string[0]


def makes10(a: int, b: int) -> bool:
    if a == 10 or b == 10:
        return True
    elif a + b == 10:
        return True
    else:
        return False


def missing_char(string: str, n: int) -> str:
    if n-1 in range(0, len(string)):
        new_string = string.replace(string[n-1], '')
    else:
        new_string = 'Parameter n indicates the value beyond the maximum number of characters in the word.'
    return new_string


def monkey_trouble(a_smile: bool, b_smile: bool) -> bool:
    if a_smile and b_smile:
        return bool(True)
    return bool(False)


def near_hundred(n: int) -> bool:
    if abs(n) in range(90, 101) or abs(n) in range(190, 201):
        return True
    return False


def not_string(string: str) -> str:
    words = [word for word in string.split()]
    if words[0] == 'not':
        return string
    return 'not ' + string


def parrot_trouble(talking: bool, hour: int) -> bool:
    if talking and (hour < 7 or hour > 20):
        return True
    else:
        return False


def pos_neg(a: int, b: int, negative: bool) -> bool:
    if a == 0 or b == 0:
        print('WARNING! One or both values are equal to 0.')
        exit(1)
    elif (b < 0 > a) or (a < 0 > b) and not negative:
        return True
    elif a < 0 < b and negative:
        return True
    return False


def sleep_in(weekday: bool, vacation: bool) -> bool:
    if not weekday or vacation:
        return True
    else:
        return False


def sum_double(val_1: int, val_2: int) -> int:
    sum_of_values = sum([val_1, val_2])
    if val_1 != val_2:
        return sum_of_values
    return sum_of_values*2
