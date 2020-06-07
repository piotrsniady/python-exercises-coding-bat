from collections import Counter
import re


def cat_dog(string: str) -> bool:
    set_array = [string[i:i + 3] for i in range(len(string) - 2)]
    cats = Counter(set_array)['cat']
    dogs = Counter(set_array)['dog']
    if cats == dogs:
        return True
    return False


def count_code(string: str) -> int:
    count = 0
    set_array = [string[i:i + 4] for i in range(len(string) - 3)]
    for word in set_array:
        match = re.search("co.e", word)
        if match:
            count += 1
    return count


def count_hi(string: str) -> bool:
    set_array = [string[i:i + 2] for i in range(len(string) - 1)]
    return bool([True if 'hi' in set_array else False])


def double_char(string: str) -> str:
    return ''.join([char*2 for char in string])


def end_other(a: str, b: str) -> bool:
    if a[-3:].lower() == b.lower() or b[-3:].lower() == a.lower():
        return True
    return False


def xyz_there(string: str) -> bool:
    if '.' in string:
        return False
    else:
        if 'xyz' in string:
            return True
        return False
