def declare_winner(fighter1, fighter2, first_attacker):
    """
    两人比武,参数1:人名,参数2:血量,参数3:杀伤力,
    :param fighter1:
    :param fighter2:
    :param first_attacker: 先出手的人
    :return:
    """
    a, b, c, d = fighter1[1], fighter2[1], fighter1[2], fighter2[2]
    if first_attacker == fighter2[0]:
        while True:
            a -= d
            if a <= 0:
                winer = fighter2[0]
                return winer
            b -= c
            if b <= 0:
                winer = fighter1[0]
                return winer

    else:
        while True:
            b -= c
            if b <= 0:
                winer = fighter1[0]
                return winer
            a -= d
            if a <= 0:
                winer = fighter2[0]
                return winer


if __name__ == "__main__":
    fighter1 = ('lew', 10, 2)
    fighter2 = ('harry', 5, 4)
    first_attacker = 'lew'
    winers = declare_winner(fighter1,fighter2,first_attacker)
    print(winers)
