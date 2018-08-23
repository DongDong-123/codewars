def card_is_sort(card):
    """

    :param card: list, len(card)==5
    :return:
    """
    num = 0
    if 'big' in card:
        card.remove('big')
        num -= 1
    if 'small' in card:
        card.remove('small')
        num -= 1

    card.sort()
    for i in range(1, len(card)):
        if card[i - 1] + 1 == card[i]:
            pass
        elif card[i - 1] + 2 == card[i]:
            num += 1
        elif card[i - 1] + 3 == card[i]:
            num += 2
        else:
            num = 4

    # print(num)
    if num <= 0:
        print('是顺子')
    else:
        print('不是顺子')


if __name__ == "__main__":
    import random
    card = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 'big', 'small']
    card1 = random.sample(card,  5)
    print('card', card1)
    card_is_sort(card1)
    """
    随机抽出5张牌，判断是不是顺子，大小王可以百搭
    """