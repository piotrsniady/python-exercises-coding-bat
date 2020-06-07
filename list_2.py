# Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array.
# Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.
def big_diff(nums: list) -> (int, str):
    if not isinstance(nums, list):
        print("Wrong type of value. Expected list type.")
        quit()
    elif len(nums) == 0:
        print('Given list is empty.')
        exit(1)
    elif len(nums) >= 1:
        return max(nums) - min(nums)
    else:
        return 'Given list should have at least one element.'


# Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring
# the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one
# copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the
# array is length 3 or more.
def centered_average(nums: list) -> int:
    if not isinstance(nums, list):
        print("Wrong type of value. Expected list type.")
        quit()
    else:
        nums.remove(max(nums))
        nums.remove(min(nums))
        return sum(nums)/len(nums)


# Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.
def count_evens(nums: list) -> int:
    if not isinstance(nums, list):
        print("Wrong type of value. Expected list type.")
        quit()
    else:
        num_list = [num for num in nums if num % 2 == 0]
        return len(num_list)


# Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.
def has22(nums: list) -> bool:
    if not isinstance(nums, list):
        print("Wrong type of value. Expected list type.")
        quit()
    else:
        check_list = [2, 2]
        set_array = [nums[i:i + 2] for i in range(len(nums) - 1)]

        for i in set_array:
            if i == check_list:
                return True
        return False


# Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so
# it does not count and numbers that come immediately after a 13 also do not count.
def sum13(nums: list) -> int:
    if not isinstance(nums, list):
        print("Wrong type of value. Expected list type.")
        quit()
    else:
        if 13 not in nums:
            return sum(nums)
        idx_of_thirteen = nums.index(13)
        return sum(nums[:idx_of_thirteen])


# Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the
# next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.
def sum67(nums: list) -> int:
    if not isinstance(nums, list):
        print("Wrong type of value. Expected list type.")
        quit()
    else:
        if 6 not in nums or 7 not in nums:
            return sum(nums)
        idx_of_six = nums.index(6)
        idx_of_seven = nums.index(7)
        return sum(nums[:idx_of_six] + nums[idx_of_seven + 1:])