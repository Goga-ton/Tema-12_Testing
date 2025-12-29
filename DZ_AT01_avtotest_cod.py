def remains(number, division):
    if division == 0:
        raise ValueError('На ноль делить нельзя')
    return number % division
