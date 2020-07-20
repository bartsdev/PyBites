def sum_numbers(numbers=None):
    calc = 0
    if numbers is None:
        return sum(range(101))
    else:
        return sum(numbers)
    pass
