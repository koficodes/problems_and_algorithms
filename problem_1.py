def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number == 0 or number == 1:
        return number

    first = 1
    last = number

    while first <= last:
        mid = (first + last) // 2
        mid_square = mid * mid
        if mid_square == number:
            return mid

        if mid_square < number:
            first = mid + 1
            floor_answer = mid

        if mid_square > number:
            last = mid - 1

    return floor_answer


print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
print("Pass" if (9 == sqrt(81)) else "Fail")
