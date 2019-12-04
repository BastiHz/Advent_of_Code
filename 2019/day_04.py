# https://adventofcode.com/2019/day/4


import collections


def check_increasing_digits(password):
    """Return True if, going from left to right, the values never decrease."""
    password = list(password)
    return password == sorted(password)


def check_adjacent_pairs(password):
    """Return True if there is a pair of values which are the same."""
    # I could have used collections.Counter() here but this works, too.
    return any(password[i] == password[i + 1] for i in range(len(password) - 1))


def check_adjacent_pairs_group(password):
    """Return True if there is a pair of two adjacent values which are the same
    but that is not part of a bigger group. Assumes that the values are sorted.
    """
    return 2 in collections.Counter(password).values()


assert check_increasing_digits("111111") and check_adjacent_pairs("111111")
assert not (check_increasing_digits("223450") and check_adjacent_pairs("223450"))
assert not (check_increasing_digits("123789") and check_adjacent_pairs("123789"))
assert check_increasing_digits("112233") and check_adjacent_pairs_group("112233")
assert not (check_increasing_digits("123444") and check_adjacent_pairs_group("123444"))
assert check_increasing_digits("111122") and check_adjacent_pairs_group("111122")

day_04_input = "178416-676461"
day_04_input = [int(i) for i in day_04_input.split("-")]
total_part_1 = 0
total_part_2 = 0
for pw in range(day_04_input[0], day_04_input[1] + 1):
    pw = str(pw)
    if not check_increasing_digits(pw):
        continue
    total_part_1 += check_adjacent_pairs(pw)
    total_part_2 += check_adjacent_pairs_group(pw)
print(total_part_1)  # 1650
print(total_part_2)  # 1129
