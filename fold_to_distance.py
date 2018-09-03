def fold_to(distance):
    """
    0.0001翻倍多少次能大于或等于distance
    :param distance: int
    :return:
    """
    nums = 0.0001
    n = 0
    if distance < 0:
        return None
    while nums <= distance:
        nums = 2 * nums
        n += 1
    else:
        return n


if __name__ == "__main__":

    a = fold_to(1)
    print(a)
    a = fold_to(348000000)
    print(a)