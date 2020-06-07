# Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element.
# Both arrays will be length 1 or more.
def common_end(l1: list, l2: list) -> bool:
    if not isinstance(l1, list) or not isinstance(l2, list):
        print("Wrong type of value. Expected list type.")
        quit()
    elif len(l1) == 0 or len(l2) == 0:
        print('One or both arrays have length equal to 0.')
        quit()
    else:
        if l1[0] == l2[0] or l1[-1] == l2[-1]:
            return True
        return False


# Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will
# be length 1 or more.
def first_last6(nums: list) -> bool:
    if not isinstance(nums, list):
        print("Wrong type of value. Expected list type.")
        quit()
    elif len(nums) == 0:
        print("Given list is empty.")
        quit()
    else:
        if 6 in [nums[0], nums[-1]]:
            return True
        return False


# Given an int array length 2, return True if it contains a 2 or a 3.
def has23(nums: list) -> bool:
    if not isinstance(nums, list):
        print("Wrong type of value. Expected list type.")
        quit()
    elif len(nums) != 2:
        raise ValueError('Given array has no length equal 2.')
    else:
        if 2 in nums or 3 in nums:
            return True
        return False


# Given an array of ints, return a new array length 2 containing the first and last elements from the original array.
# The original array will be length 1 or more.
def make_ends(nums: list) -> list:
    if not isinstance(nums, list):
        print("Wrong type of value. Expected list type.")
        quit()
    elif len(nums) == 0:
        print("Given list is empty.")
        quit()
    else:
        return [nums[0], nums[-1]]


# Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.
from numpy import array
from math import pi


def make_pi(n: int):
    pi_num = [cipher for cipher in str(pi) if cipher.isdigit()]
    len_pi_num = len(pi_num)

    if not isinstance(n, int):
        print("Wrong type of value. Expected int type.")
        quit()
    elif n <= 0:
        print("Given number is too slow. Please enter the number higher than 0.")
    elif n > len_pi_num:
        print("Given number is too high. Available value must be lower than 17.")
    else:
        return "".join(pi_num[:n])


# Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set all the
# other elements to be that value. Return the changed array.
def max_end3(nums: list) -> list:
    if not isinstance(nums, list):
        print("Wrong type of value. Expected list type.")
        quit()
    elif len(nums) != 3:
        print("Wrong list size. Expected 3 element list.")
    else:
        if nums[0] > nums[-1]:
            max_val = nums[0]
        else:
            max_val = nums[-1]
        for i in range(len(nums)):
            nums[i] = max_val
        return nums


# Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.
def middle_way(l1: list, l2: list) -> list:
    if not isinstance(l1, list) or not isinstance(l2, list):
        print("Wrong type of one of the values. Expected list type.")
        quit()
    try:
        assert len(l1) == 3 or len(l2) != 3
    except AssertionError:
        print("One of the given lists has no required length.")
    else:
        return [l1[1], l2[1]]


# Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3}
# becomes {3, 2, 1}.
def reverse3(nums: list) -> list:
    if not isinstance(nums, list):
        print("Wrong type of value. Expected list type.")
        quit()
    elif len(nums) != 3:
        print("Wrong list size. Expected 3 element list.")
        quit()
    else:
        return nums[::-1]


# Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.
def rotate_left3(num_list: list) -> list:
    if not isinstance(num_list, list):
        print("Wrong type of value. Expected list type.")
        quit()
    elif len(num_list) != 3:
        print("Wrong list size. Expected 3 element list.")
        quit()
    else:
        return num_list[1:] + num_list[:1]


# Given an array of ints, return True if the array is length 1 or more, and the first element and the last element
# are equal.
def same_first_last(nums: list) -> bool:
    if not isinstance(nums, list):
        print("Wrong type of value. Expected list type.")
        quit()
    elif len(nums) >= 1 == nums[0] == nums[-1]:
        return True
    else:
        return False


# Given an array of ints, return the sum of the first 2 elements in the array. If the array length is less than 2, just
# sum up the elements that exist, returning 0 if the array is length 0.
def sum2(nums: list) -> (int, list):
    if not isinstance(nums, list):
        print("Wrong type of value. Expected list type.")
        quit()
    elif len(nums) == 0:
        return 0
    elif len(nums) < 2:
        return nums[0]
    else:
        return nums[0] + nums[1]


# Given an array of ints length 3, return the sum of all the elements.
import operator
from functools import reduce


def sum3(nums: list) -> list:
    for num in nums:
        if not str(num).isdigit():
            print("Value in list is not a number.")
            quit()

    if not isinstance(nums, list):
        print("Wrong type of value. Expected list type.")
        quit()
    else:
        return reduce(operator.add, nums)