def array123(nums: list) -> bool:
    sets_array = [nums[i:i + 3] for i in range(len(nums) - 2)]
    if [1, 2, 3] in sets_array:
        return True
    else:
        return False


def array_count9(nums: list) -> int:
    return nums.count(9)


def array_front9(nums: list) -> bool:
    if 9 in nums[:4]:
        return True
    else:
        return False


def front_times(string: str, n: int) -> str:
    if not str(n).isdigit():
        print('Parameter n must be a number.')
        exit(1)

    if int(n) <= 0:
        raise ValueError('Parameter n must be greater than 0')
    return string[:3] * int(n)


def last2(string: str) -> int:
    set_array = [string[i:i + 2] for i in range(len(string) - 1)]
    last = set_array[-1]
    return set_array.count(last) - 1


def string_bits(string: str) -> str:
    return string[::2]


def string_match(a: str, b: str) -> int:
    a_set_array = [a[i:i + 2] for i in range(len(a) - 1)]
    b_set_array = [b[i:i + 2] for i in range(len(b) - 1)]
    sets_intersection = set(a_set_array).intersection(set(b_set_array))
    return len(sets_intersection)


def string_splosion(string: str) -> str:
    for i in range(len(string)):
        for j in range(i+1):
            return ''.join(string[j])


def string_times(string: str, n: int) -> str:
    if not str(n).isdigit():
        print('Parameter n must be a number.')
        exit(1)
    return string*n
