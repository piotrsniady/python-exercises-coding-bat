# Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case
# just return 20.
def sorta_sum(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        print("Wrong type of one of the values. Expected string type.")
        quit()
    else:
        calc = [20 if int(a) + int(b) in range(10, 20) else int(a) + int(b)]
        return calc[0]


# The squirrels in Palo Alto spend most of the day playing. In particular, they play if the temperature is between 60
# and 90 (inclusive). Unless it is summer, then the upper limit is 100 instead of 90. Given an int temperature and a
# boolean is_summer, return True if the squirrels play and False otherwise.
def squirrel_play(temp: int, is_summer: bool) -> bool:
    if not isinstance(temp, int):
        print("Given values is not integer type.")
        quit()
    elif not isinstance(is_summer, bool):
        print("Given values is not bool type.")
        quit()
    else:
        if temp in range(60, 91) or is_summer:
            return True
        elif temp in range(60, 101) or not is_summer:
            return False


# Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on vacation,
# return a string of the form "7:00" indicating when the alarm clock should ring. Weekdays, the alarm should be "7:00"
# and on the weekend it should be "10:00". Unless we are on vacation -- then on weekdays it should be "10:00" and
# weekends it should be "off".
def alarm_clock(day: int, vacation: bool) -> str:
    days = [0, 1, 2, 3, 4, 5, 6]
    if not isinstance(day, int):
        print("Given values is not integer type.")
        quit()
    elif not isinstance(vacation, bool):
        print("Given values is not bool type.")
        quit()
    elif day not in days:
        print("Given option is not in list.")
        quit()
    else:
        if day in [1, 2, 3, 4, 5] and not vacation:
            return "7:00"
        elif day in [0, 6] and not vacation:
            return "10:00"
        elif day in [1, 2, 3, 4, 5] and vacation:
            return "10:00"
        else:
            return "off"


# You are driving a little too fast, and a police officer stops you. Write code to compute the result, encoded as an
# int value: 0=no ticket, 1=small ticket, 2=big ticket. If speed is 60 or less, the result is 0. If speed is between 61
# and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless it is your birthday -- on that
# day, your speed can be 5 higher in all cases.
def caught_speeding(speed: int, is_birthday: bool) -> int:
    if not isinstance(speed, int):
        print("Given values is not integer type.")
        quit()
    elif not isinstance(is_birthday, bool):
        print("Given values is not bool type.")
        quit()
    else:
        if is_birthday:
            speed += 5
        if speed <= 60:
            return 0
        elif 61 < speed <= 80:
            return 1
        else:
            return 2


# When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of
# cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number
# of cigars. Return True if the party with the given values is successful, or False otherwise.
def cigar_party(cigars: int, is_weekend: bool) -> bool:
    if not isinstance(cigars, int):
        print("Given values is not integer type.")
        quit()
    elif not isinstance(is_weekend, bool):
        print("Given values is not bool type.")
        quit()
    else:
        if cigars not in range(40, 61) and not is_weekend:
            return False
        return True


# You and your date are trying to get a table at a restaurant. The parameter "you" is the stylishness of your clothes,
# in the range 0..10, and "date" is the stylishness of your date's clothes. The result getting the table is encoded as
# an int value with 0=no, 1=maybe, 2=yes. If either of you is very stylish, 8 or more, then the result is 2 (yes). With
# the exception that if either of you has style of 2 or less, then the result is 0 (no). Otherwise the result is
# 1 (maybe).
def date_fashion(you: int, date: int) -> int:
    if not isinstance(you, int) or not isinstance(date, int):
        print("Wrong type of one of the values. Expected integer type.")
        quit()
    else:
        if you not in range(0, 11) and date not in range(0, 11):
            print('One or both variables are out of range. Only 0-10 range.')
            exit(1)
        elif you >= 8 <= date:
            return 2
        elif you <= 2 >= date:
            return 0
        return 1


# Given a number n, return True if n is in the range 1..10, inclusive. Unless outside_mode is True, in which case return
# True if the number is less or equal to 1, or greater or equal to 10.
def in1to10(n: int, outside_mode: bool) -> bool:
    if not isinstance(n, int):
        print("Wrong type of value. Expected int type.")
        quit()
    if not isinstance(outside_mode, bool):
        print("Wrong type of value. Expected bool type.")
        quit()
    else:
        if n in range(1, 11) and not outside_mode:
            return True
        elif n <= 1 or n >= 10 and outside_mode:
            return True
        else:
            return False


# The number 6 is a truly great number. Given two int values, a and b, return True if either one is 6. Or if their sum
# or difference is 6. Note: the function abs(num) computes the absolute value of a number.
def love6(a: int, b: int) -> bool:
    if not isinstance(a, int) or not isinstance(b, int):
        print("Wrong type of one of the values. Expected string type.")
        quit()
    else:
        if a == 6 or b == 6 or a + b == 6 or a - b == 6:
            return True
        return False
