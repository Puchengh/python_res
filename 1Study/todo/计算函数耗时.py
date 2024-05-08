import timeit


def max_of_three_1(a, b, c):
    return max(a, b, c)


def max_of_three_2(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


def max_of_three_3(a, b, c):
    nums = [a, b, c]
    nums.sort()
    return nums[2]


if __name__ == "__main__":
    print(timeit.timeit("max_of_three_1(1, 2, 3)", setup="from __main__ import max_of_three_1"))
    print(timeit.timeit("max_of_three_2(1, 2, 3)", setup="from __main__ import max_of_three_2"))
    print(timeit.timeit("max_of_three_3(1, 2, 3)", setup="from __main__ import max_of_three_3"))
