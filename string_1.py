def extra_end(string: str) -> str:
    return string[-2:] * 3


def first_half(string: str) -> str:
    if len(string) // 2 == 0:
        raise ValueError('Given string is not even')
    else:
        return string[:(int(len(string)/2))]


def first_two(string: str) -> str:
    return string[:2]


def hello_name(name: str) -> str:
    return 'Hello ' + name


def left2(string: str) -> str:
    start = string[:2]
    end = string[2:]
    return end + start


def make_abba(a: str, b: str) -> str:
    return ''.join((a, b, b, a))


def make_out_word(out: str, word: str) -> str:
    return out[:2] + word + out[-2:]


def make_tags(tag: str, word: str) -> str:
    return '<' + tag + '>' + word + '</' + tag + '>'


def without_end(string: str) -> str:
    return string[1:-1]