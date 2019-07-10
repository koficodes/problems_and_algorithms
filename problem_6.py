import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """

    index = 0
    end = len(ints)-1
    max = ints[0]
    min = ints[0]
    while index < end:
        if ints[index] < ints[index+1]:
            temp_min = ints[index]
            temp_max = ints[index+1]
        else:
            temp_min = ints[index+1]
            temp_max = ints[index]

        if temp_min < min:
            min = temp_min
        if temp_max > max:
            max = temp_max
        index += 1
    return (min, max)


def test_input(start, end):
    samples = list(range(start, end))
    random.shuffle(samples)
    return samples


print("Pass" if ((0, 9) == get_min_max(test_input(0, 10))) else "Fail")
print("Pass" if ((5, 49) == get_min_max(test_input(5, 50))) else "Fail")
print("Pass" if ((2, 8) == get_min_max(test_input(2, 9))) else "Fail")
print("Pass" if ((0, 19) == get_min_max(test_input(0, 20))) else "Fail")
# Pass
# Pass
# Pass
# Pass
