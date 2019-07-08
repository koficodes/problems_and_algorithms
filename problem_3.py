def mergesort_reverse(items):

    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]

    left = mergesort_reverse(left)
    right = mergesort_reverse(right)

    return merge(left, right)


def merge(left, right):

    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """

    # sort the array
    input_list = mergesort_reverse(input_list)

    n = len(input_list)

    first = 0
    second = 0
    for i in range(n):

        if (i % 2 != 0):
            first = first * 10 + input_list[i]
        else:
            second = second * 10 + input_list[i]

    return [first, second]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_cases = [[[4, 6, 2, 5, 9, 8], [964, 852]],
              [[1, 2, 3, 4, 5], [542, 31]],
              [[2, 8, 6, 9, 2, 5, 6], [862, 9652]]]
for case in test_cases:
    test_function(case)

# Pass
# Pass
# Pass
