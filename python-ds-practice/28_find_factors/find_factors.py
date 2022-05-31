def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
    factors = []
    for i in range(1, num+1):
        if num%i == 0:
            factors.append(i)
    return factors

    
    # num_list = [n for n in range(1, num // 2 + 1) if num%n ==0]
    # print(num_list)
    # print(num)
    # # num // 2 is floored to the nearest whole number
    # # so for num=10, range(1, 6)
    # num_list.append(num)
    # return num_list

print(find_factors(10))
print(find_factors(11))
print(find_factors(111))
print(find_factors(321421))